import socketserver
from http.server import SimpleHTTPRequestHandler
 
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/static/index.html'
        elif self.path == '/favicon.ico':
            self.path = '/static/favicon.ico'

        return SimpleHTTPRequestHandler.do_GET(self)

server = socketserver.TCPServer(('127.0.0.1', 8080), MyHandler)
server.serve_forever()