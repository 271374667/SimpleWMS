"""
在程序开始的时候就会被创建,作为一个子线程一直跟随主线程运行

因为pyecharts的图表需要使用本地服务器进行渲染,所以需要在本地搭建一个服务器,然后将服务器的地址设置到CurrentConfig.ONLINE_HOST中
"""

import http.server
import socketserver
import threading
from functools import partial
from pathlib import Path

import loguru
from pyecharts.globals import CurrentConfig

from src.constant import PYECHART_ASSETS


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """
    因为pyinstaller的无控制台模式下,send_resopnse方法没有办法正常运行
    send_response函数更换成send_response_only
    """

    def send_response(self, code, message=None):
        self.send_response_only(code, message)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        http.server.SimpleHTTPRequestHandler.end_headers(self)


class ChartLocalServer:
    def __init__(self, host: str, port: int, local_dir: Path = PYECHART_ASSETS):
        self.host = host
        self.port = port
        self.local_dir = local_dir
        self.httpd = None
        self.server_thread = None
        self.is_running = False

    def run(self):
        # handler = partial(http.server.SimpleHTTPRequestHandler, directory=self.local_dir)
        handler = partial(CustomHTTPRequestHandler, directory=self.local_dir)
        handler.directory = str(self.local_dir)
        loguru.logger.debug(f"获取图表资源的路径: {self.local_dir}")
        while not self.is_running:
            try:
                self._start_server(handler)
                self.is_running = True

            except OSError as e:
                self._retry_server(e, handler)

    # 本来不是很想把逻辑拆分成这么多个函数,但是Sourcey一直给我警告,所以我就拆分了
    def _retry_server(self, e, handler):
        loguru.logger.error(f"图表线程启动失败,正在切换端口,错误信息: {e}")
        self.port += 1
        self._start_server(handler)

    def _start_server(self, handler):
        self.httpd = socketserver.TCPServer((self.host, self.port), handler)
        self.server_thread = threading.Thread(target=self.httpd.serve_forever)
        self.server_thread.start()
        loguru.logger.info(f"图表线程启动在 {self.host}:{self.port} 上")
        CurrentConfig.ONLINE_HOST = f"http://127.0.0.1:{self.port}/"

    def stop(self):
        if self.httpd is not None:
            self.httpd.shutdown()
            self.httpd.server_close()
            self.server_thread.join()
            self.httpd = None
            self.server_thread = None
            loguru.logger.debug("图表线程关闭")
