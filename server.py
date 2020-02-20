import datetime
import markdown2
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
            self.send(Build("home"))
        elif arg[0] in navbarPaths:
            self.send(Build(arg[0]))
        elif arg[0] == "css":
            self.sendCss()
        elif arg[0] in ["ico", "favicon.ico"]:
            self.sendIco()
        elif arg[0] == "setup":
            self.sendImg("assets/setup.png")
        else:
            self.send(Build("404"))

navbarNames = ["Home", "My fav xkcd", "Tools", "Contact", "Portfolio", "Log"]
navbarPaths = ["home", "xkcd",        "tools", "contact", "portfolio", "log"]
template = open("assets/template.html", 'r').read()

def Build(path):
    html = template

    navbar = ""
    navbarNum = navbarPaths.index(path) if path in navbarPaths else -1
    for i in range(len(navbarNames)):
        navbar += "<span"
        navbar += " class=\"current\"" if i == navbarNum else ""
        navbar += "><a href=\""
        navbar += navbarPaths[i]
        navbar += "\">"
        navbar += navbarNames[i]
        navbar += "</a></span>"
        navbar += "" if i == len(navbarNames) - 1 else "<span> | </span>"

    content = markdown2.markdown(open("assets/content/" + path + ".md", 'r').read())

    title = navbarNames[navbarNum] if not navbarNum == -1 else path
    
    html = html.replace("*title*", title).replace("*navbar*", navbar).replace("*content*", content)

    return html

server_address = ("192.168.0.173", 8000)
httpd = HTTPServer(server_address, S)
httpd.serve_forever()
