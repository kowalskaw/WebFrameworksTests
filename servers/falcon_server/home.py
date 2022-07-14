import falcon


class Home:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open('./falcon_server/templates/index.html') as f:
            resp.text = f.read()
