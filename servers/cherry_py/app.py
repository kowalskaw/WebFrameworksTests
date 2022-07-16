import cherrypy
import json
import uuid


class HomePage(object):
    @cherrypy.expose
    def index(self):
        cherrypy.log('jep')
        with open('./templates/index.html') as f:
            return f.read()


@cherrypy.expose
@cherrypy.tools.json_out()
class Books(object):
    def __init__(self):
        self.books = json.load(open('./../../data/books.json'))

    def POST(self):
        book_dict = json.loads(cherrypy.serving.request.body.read())
        book_dict['id'] = str(uuid.uuid4())
        self.books += [book_dict]
        cherrypy.response.status = 201
        cherrypy.log(str(self.books))
        return {"data": book_dict}

    def PUT(self, book_id):
        book_dict = json.loads(cherrypy.serving.request.body.read())
        for i, book in enumerate(self.books):
            if book['id'] == book_id:
                self.books[i] = book_dict
                self.books[i]['id'] = book_id
                cherrypy.response.status = 200
                return {"data": book_dict}
        cherrypy.response.status = 204
        return {}

    def GET(self, book_id=None):
        if(book_id):
            for book in self.books:
                if book['id'] == book_id:
                    cherrypy.response.status = 200
                    return {"data": book}
        else:
            cherrypy.response.status = 200
            return {"data": self.books}

    def DELETE(self, book_id):
        for i, book in enumerate(self.books):
            if book['id'] == book_id:
                del self.books[i]
                cherrypy.response.status = 200
                return {}
        cherrypy.response.status = 204
        return {}


#cherrypy.config.update({'server.socket_port': 8000})
cherrypy.tree.mount(Books(), '/books', {
    '/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
})
cherrypy.tree.mount(HomePage(), '/', {'/': {}})
cherrypy.engine.start()
cherrypy.engine.block()
