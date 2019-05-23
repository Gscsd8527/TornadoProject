import tornado.web
import tornado.ioloop
import tornado.httpserver
from APISets.weatherAPI import *

import logging
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("./logs/log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class MainHandler(tornado.web.RequestHandler):
    """主路由处理类"""
    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        """对应HTTP的请求方式"""
        try:
            print('----------开始进入程序-------------')
            logger.info("[Request]:" + self.request.query)
            data = search_api(self)
            # self.write(data)
            self.finish(data)
        except Exception as e:
            logger.error("[Response]:" + str(e))

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("node health check success!")

application = tornado.web.Application([
    (r'/checkinfo/', MainHandler),
    (r'/index/', IndexHandler)
])

if __name__ == '__main__':
    server = tornado.httpserver.HTTPServer(application)
    server.listen(8000)
    tornado.ioloop.IOLoop.current().start()

# 测试url: http://127.0.0.1:8000/checkinfo/?city=北京
