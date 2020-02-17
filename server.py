import datetime
from pageBuilder import Build
from http.server import HTTPServer, BaseHTTPRequestHandler

class S(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def set_headers404(self):
        self.send_response(404)
        self.end_headers()
    
    def sendCss(self):
        self.send_response(200)
        self.send_header("Content-type", "text/css")
        self.end_headers()
        self.wfile.write(open("assets/styles.css", "r").read().encode("utf8"))

    def sendIco(self):
        self.send_response(200)
        self.send_header("Content-type", "image/png")
        self.end_headers()
        self.wfile.write(open("assets/favicon.png", "rb").read())

    def send(self, message):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(message.encode("utf8"))

    def do_GET(self):
        arg = self.path[1:].split(";")
        print("[" + str(datetime.datetime.now()) + "]", "GET request -", ":".join(map(str, self.client_address)), "- arg:", arg)
        if arg[0] == "":
            self.send(Build("home"))
        elif arg[0] in ["home", "xkcd", "tools", "contact"]:
            self.send(Build(arg[0]))
        elif arg[0] == "css":
            self.sendCss()
        elif arg[0] == "ico":
            self.sendIco()
        else:
            self.send(Build("404"))

server_address = ("localhost", 8000)
httpd = HTTPServer(server_address, S)

print(f"Starting server")
httpd.serve_forever()
