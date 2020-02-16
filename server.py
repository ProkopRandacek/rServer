import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler

class S(BaseHTTPRequestHandler):
    def set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def set_headers404(self):
        self.send_response(404)
        self.end_headers()

    def html(self, message, notFound=False):
        print("sending html message", message)
        content = '<html><style>*{font-family:"Courier New";}</style><body><h1>' + message + '</h1></body></html>'
        self.send(content)
    
    def sendCss(self):
        print("sending css")
        self.send_response(200)
        self.send_header("Content-type", "text/css")
        self.end_headers()
        self.wfile.write(open("styles.css", "r").read().encode("utf8"))

    def sendFile(self, path):
        print("sending file", path)
        self.send(open(path, "r").read())

    def send(self, message):
        self.set_headers()
        self.wfile.write(message.encode("utf8"))
        print("send")

    def log_message(self, format, *args):
        pass

    def do_GET(self):
        print("=== GET Request recieved ===")
#        print(" Client address", self.client_address)
        arg = self.path[1:].split(";")
        print("arg:", arg)

        if arg[0] == "":
            self.sendFile("index.html")
        elif arg[0] == "ping":
            self.send("pong")
        elif arg[0] == "pingPage":
            self.sendFile("pingPage.html")
        elif arg[0] == "css":
            self.sendCss()
        else:
            print("unknown arg")
            self.html("404")

    def do_HEAD(self):
        self.set_headers()

    def do_POST(self):
        self.set_headers()
        self.wfile.write(self._html("POST!"))

server_address = ("localhost", 8000)
httpd = HTTPServer(server_address, S)

print(f"Starting httpd server")
httpd.serve_forever()
