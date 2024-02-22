from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from qfluentwidgets.components import (BodyLabel, ElevatedCardWidget, FlyoutViewBase, TableWidget, TeachingTip,
                                       TeachingTipTailPosition, TeachingTipView)


class CardFlyoutTableView(QWidget):
    """
    CardFlyoutTableView
    ---

    通过传入父窗口和父控件，创建一个带有表格的卡片飞出窗口
    调用show_flyout方法显示飞出窗口
    调用get_table方法获取表格控件
    """

    def __init__(self, parent_window: QWidget, parent_widget: QWidget):
        super().__init__(parent=parent_window)
        self.parent_window = parent_window
        self.parent_widget = parent_widget
        self.is_closeable = True
        self.content: str = ''
        self.title: str = ''
        self.table = TableWidget()
        self.table.setFixedSize(500, 300)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)  # 设置表格不可编辑
        # 令表格的最后一列填充整个空白
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setSortingEnabled(True)

    def set_content(self, content: str) -> None:
        """设置飞出窗口的内容"""
        self.content = content

    def set_title(self, title: str) -> None:
        """设置飞出窗口的标题"""
        self.title = title

    def set_is_closeable(self, is_closeable: bool) -> None:
        """设置飞出窗口是否可以关闭"""
        self.is_closeable = is_closeable

    def get_table(self) -> TableWidget:
        """获取表格控件"""
        return self.table

    def get_view(self) -> FlyoutViewBase:
        """获取飞出窗口的视图"""
        self.flyout_view = TeachingTipView(
                title=self.title,
                content=self.content,
                isClosable=self.is_closeable,
                tailPosition=TeachingTipTailPosition.TOP
                )

        self.flyout_view.addWidget(self.table)
        return self.flyout_view

    def show_flyout(self) -> None:
        """显示飞出窗口"""
        self.flyout_window = TeachingTip.make(
                target=self.parent_widget,
                view=self.get_view(),
                duration=-1,
                tailPosition=TeachingTipTailPosition.BOTTOM,
                parent=self.parent_window
                )

        self.flyout_view.closed.connect(self.flyout_window.close)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Teaching Tip Example")
        self.setGeometry(100, 100, 800, 600)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.e1 = ElevatedCardWidget()
        self.lb1 = BodyLabel()
        self.lb1.setText("Click the button to show the teaching tip.")
        self.e1_layout = QVBoxLayout()
        self.e1_layout.addWidget(self.lb1)
        self.e1.setLayout(self.e1_layout)
        self.main_layout.addWidget(self.e1)

        self.e1.clicked.connect(self.e_clicked)

    def e_clicked(self) -> None:
        print('被点击')
        c = CardFlyoutTableView(self, self.e1)
        c.table.setRowCount(20)
        c.table.setColumnCount(4)
        c.table.setHorizontalHeaderLabels(['Name', 'Age', 'email', 'password'])
        c.table.setItem(0, 0, QTableWidgetItem('Tom'))
        c.table.setItem(0, 1, QTableWidgetItem('18'))
        c.table.setItem(1, 0, QTableWidgetItem('Jerry'))
        c.table.setItem(1, 1, QTableWidgetItem('19'))
        c.table.setItem(2, 0, QTableWidgetItem('Mickey'))
        c.table.setItem(2, 1, QTableWidgetItem('20'))
        c.show_flyout()


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
