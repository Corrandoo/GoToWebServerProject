import tornado.ioloop
import tornado.web

app = tornado.web.Application([])
app.listen(8888)
tornado.ioloop.IOLoop.current().start()