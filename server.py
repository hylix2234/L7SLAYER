from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPRequestHandler):
    pass

server = ThreadingHTTPServer(("0.0.0.0", 9090), MyHandler)
server.socket.setsockopt(1, 2, 1)  # SO_REUSEADDR
server.serve_forever()
