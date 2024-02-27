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

from src.constant import PYECHART_ASSETS


class HttpServer:
    def __init__(self, host: str, port: int, local_dir: Path = PYECHART_ASSETS):
        self.host = host
        self.port = port
        self.local_dir = local_dir
        self.httpd = None
        self.server_thread = None

    def run(self):
        handler = partial(http.server.SimpleHTTPRequestHandler, directory=self.local_dir)
        handler.directory = str(self.local_dir)

        self.httpd = socketserver.TCPServer((self.host, self.port), handler)
        self.server_thread = threading.Thread(target=self.httpd.serve_forever)
        self.server_thread.start()
        loguru.logger.info(f"图表线程启动在 {self.host}:{self.port} 上")

    def stop(self):
        if self.httpd is not None:
            self.httpd.shutdown()
            self.httpd.server_close()
            self.server_thread.join()
            self.httpd = None
            self.server_thread = None
            loguru.logger.debug("图表线程关闭")
