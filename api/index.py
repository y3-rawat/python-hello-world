from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def ge():
        return "asd"
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        
        self.wfile.write(g().encode('utf-8'))
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return
