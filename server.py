import datetime, markdown2, json
from collections import namedtuple
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
        self.wfile.write(open(conf.paths.css, "r").read().encode("utf8"))

    def sendIco(self):
        self.send_response(200)
        self.send_header("Content-type", "image/png")
        self.end_headers()
        self.wfile.write(open(conf.paths.ico, "rb").read())

    def sendImg(self, path):
        self.send_response(200)
        self.send_header("Content-type", "image/png")
        self.end_headers()
        self.wfile.write(open(path, "rb").read())

    def send(self, message):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(message.encode("utf8"))

    def do_GET(self):
        arg = self.path[1:].split(";")
        print("[" + str(datetime.datetime.now()) + "]", "GET request -", ":".join(map(str, self.client_address)), "- arg:", arg)
        if arg[0] == "":
            self.send(Build(conf.navbar.paths[0]))
        elif arg[0] in conf.navbar.paths:
            self.send(Build(arg[0]))
        elif arg[0] == "css":
            self.sendCss()
        elif arg[0] in ["ico", "favicon.ico"]:
            self.sendIco()
        elif arg[0] == "setup":
            self.sendImg(conf.paths.setup)
        else:
            self.send(Build("404"))

def Build(path):
    html = template

    navbar = ""
    navbarNum = conf.navbar.paths.index(path) if path in conf.navbar.paths else -1
    for i in range(len(conf.navbar.names)):
        navbar += conf.navbar.item.pre
        navbar += conf.navbar.item.current if i == navbarNum else ""
        navbar += conf.navbar.item.prepath
        navbar += conf.navbar.paths[i]
        navbar += conf.navbar.item.separator
        navbar += conf.navbar.names[i]
        navbar += conf.navbar.item.pos
        navbar += "" if i == len(conf.navbar.names) - 1 else conf.navbar.separator

    content = markdown2.markdown(open(conf.paths.content + path + ".md", 'r').read())

    title = conf.navbar.names[navbarNum] if not navbarNum == -1 else path
    
    html = html.replace("*title*", title).replace("*navbar*", navbar).replace("*content*", content)

    return html

conf = json.loads(open('conf.json').read(), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

template = open(conf.paths.template, 'r').read()

server_address = (conf.address, conf.port)

httpd = HTTPServer(server_address, S)
httpd.serve_forever()
