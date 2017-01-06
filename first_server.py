import tornado.ioloop
import tornado.web
import random

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<form method ='get' action ='/hello'><input name='name' /></form>")

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("name", "Анон")
        self.write("<h1>Привет, " + name + "</h1>")


class CatsHandler(tornado.web.RequestHandler):
    def get(self):
        cats = [
            ('Васька', 'http://img1.liveinternet.ru/images/attach/c/5/86/352/86352251_samuye_krasivuye_fotografii_kotov__4_.jpg'),
            ('Петька', 'http://vesti.dp.ua/wp-content/uploads/2016/09/%D0%BA%D0%BE%D1%82%D1%8B.jpg'),

        ]
        cat = random.choice(cats)
        self.render("cats.html", cat_name=cat[0], cat_adress=cat[1])


settings = [
    ('/', MainHandler),
    ('/hello', HelloHandler),
    ('/cats', CatsHandler)
]
# http://host:port/page/page?param=value&param1=value

app = tornado.web.Application(settings)  # создали веб приложение
app.listen(8888)  # слушаем 8888 порт
tornado.ioloop.IOLoop.current().start()  # не отрубаем программу, пока господин этого не захочет