"""
QtThreadPoolExecutor
====================
该类通过QThreadPool实现了一个类似于concurrent.futures.ThreadPoolExecutor的线程池
你可以通过submit()方法提交任务,通过map()方法提交多个任务,通过shutdown()方法关闭线程池
所有的方法都和官方的ThreadPoolExecutor类似

QtFutures
=========
该类是一个自定义的Future类,用于保存任务的执行结果,并且可以通过add_done_callback()方法添加回调函数
该类的接口和concurrent.futures.Future类似,使用方法可以直接参考官方文档
"""

from concurrent.futures import CancelledError, TimeoutError
from typing import Optional

from PySide6.QtCore import QRunnable, QThreadPool, Signal, QObject


class QtFutures(QRunnable, QObject):
    """线程池任务类
    该类的接口和concurrent.futures.Future类似,使用方法可以直接参考官方文档
    https://docs.python.org/zh-cn/3.10/library/concurrent.futures.html?highlight=threadpool#future-objects
    """
    finished = Signal(object)

    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self._result = None
        self._exception = None
        self._done = False
        self._cancelled = False
        self.callbacks = []
        self.setAutoDelete(False)

    def run(self):
        """执行任务"""
        if not self._cancelled:
            try:
                self._result = self.func(*self.args, **self.kwargs)
            except Exception as e:
                self._exception = e
            finally:
                self._done = True
                # self.finished.emit(self._result)
                for callback in self.callbacks:
                    callback(self)

    def cancel(self):
        """取消任务

        该方法和官方的Future.cancel()方法最大的区别就是,它不会真正的取消任务,而是标记任务为取消状态
        所有已经被执行的任务都不会被取消,他们实际上都被真正的执行了
        只是在调用result()方法的时候会抛出CancelledError异常
        """
        if self._done:
            return False
        self._cancelled = True
        return True

    def add_done_callback(self, fn):
        """添加回调函数"""
        self.callbacks.append(fn)
        if self._done:
            fn()
        # self.finished.connect(fn)

    @property
    def done(self):
        """任务是否已经执行完成"""
        return self._done

    @property
    def result(self):
        """获取任务的执行结果"""
        if self._cancelled:
            raise CancelledError()
        if not self._done:
            raise TimeoutError()
        if self._exception:
            raise self._exception
        return self._result

    @property
    def cancelled(self):
        """任务是否被取消"""
        return self._cancelled

    @property
    def running(self):
        """任务是否还在执行中"""
        return not self._done and not self._cancelled

    @property
    def exception(self):
        """获取任务的异常"""
        return self._exception


class QtThreadPoolExecutor:
    """Qt中的线程池

    该类通过QThreadPool实现了一个类似于concurrent.futures.ThreadPoolExecutor的线程池
    你可以通过submit()方法提交任务,通过map()方法提交多个任务,通过shutdown()方法关闭线程池

    你可以前往官方文档查看更多信息:
    https://docs.python.org/zh-cn/3.10/library/concurrent.futures.html?highlight=threadpool#threadpoolexecutor
    """

    def __init__(self, max_workers=3):
        """初始化线程池

        该方法默认会使用全局的线程池,整个项目中只会有一个线程池

        Args:
            max_workers: 线程池的最大线程数(默认为3)
        """
        self.pool = QThreadPool()
        self.futures = []

        if max_workers:
            self.pool.setMaxThreadCount(max_workers)

    def submit(self, fn, *args, **kwargs):
        """提交任务"""
        self.future = QtFutures(fn, *args, **kwargs)
        self.futures.append(self.future)
        self.pool.tryStart(self.future)
        return self.future

    def map(self, func, *iterables, timeout: Optional[int] = None):
        """提交多个任务"""
        self.pool.setExpiryTimeout(timeout)
        futures = [self.submit(func, *args) for args in zip(*iterables)]
        for future in futures:
            yield future.result

    def shutdown(self, wait=True, cancel_futures=False):
        """关闭线程池"""
        if cancel_futures:
            self.pool.clear()
        if wait:
            self.pool.waitForDone()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.shutdown(wait=True)
        return False


if __name__ == '__main__':
    from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QLabel, QPlainTextEdit


    class MyWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.e = QtThreadPoolExecutor(7)
            self.main_layout = QVBoxLayout()

            self.lb = QLabel("点击按钮开始")
            self.btn = QPushButton("Start", self)
            self.pte = QPlainTextEdit()
            self.btn.clicked.connect(self.waste_time)

            self.main_layout.addWidget(self.lb)
            self.main_layout.addWidget(self.btn)
            self.main_layout.addWidget(self.pte)
            self.setLayout(self.main_layout)

        def waste_time(self):
            self.pte.clear()
            self.lb.setText("任务开始")
            for i in range(6):
                print(f'添加了一个任务{i}')
                future = self.e.submit(self.do_something, i)
                future.add_done_callback(self.done_callback)

        def do_something(self, name):
            import time
            time.sleep(2)
            print(f'完成了一个任务{name}')
            self.pte.appendPlainText(str(name))
            self.lb.setText("任务完成")
            return f"任务完成 {name}"

        def done_callback(self, future):
            self.lb.setText("任务完成")
            self.pte.appendPlainText(future.result)
            print(f'完成了一个任务{future.result}')


    app = QApplication([])
    w = MyWindow()
    w.show()
    app.exec()
