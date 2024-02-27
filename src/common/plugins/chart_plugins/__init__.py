from src.common.plugins.chart_plugins.chart.chart_local_server import HttpServer

server = HttpServer("127.0.0.1"
                    , 8000)
server.run()
