import datetime, markdown2, json, threading
from collections import namedtuple
from http.server import HTTPServer, BaseHTTPRequestHandler

class S(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass # I dont like default log style
    
    def send(self, data, contentType): # universal data sending function
        self.send_response(200)
        self.send_header("Content-type", contentType)
        self.end_headers()
        self.wfile.write(data)

    def build(self, path): # builds and sends html page from markdown file
        path      = "home" if path == "" else path
        navbarNum = conf.navbar.paths.index(path) if path in conf.navbar.paths else -1
        title     = path if navbarNum == -1 else conf.navbar.names[navbarNum]
        content   = markdown2.markdown(open(conf.path.content + path + ".md", "r").read()) # reads markdown file and converts it into html
        navbar    = ""
        for i in range(len(conf.navbar.names)): # builds navbar
            navbar += conf.navbar.item.pre
            navbar += conf.navbar.item.current if i == navbarNum else "" # current item is highlighted
            navbar += conf.navbar.item.prepath
            navbar += conf.navbar.paths[i]
            navbar += conf.navbar.item.separator
            navbar += conf.navbar.names[i]
            navbar += conf.navbar.item.pos
            navbar += "" if i == len(conf.navbar.names) - 1 else conf.navbar.separator
        html = template.replace("{title}", title).replace("{navbar}", navbar).replace("{content}", content) # insert contents into html template
        self.send(html.encode("utf8"), "text/html")

    def do_GET(self): # is called when server receives get request
        arg = self.path[1:]
        print("{0}{1}{2}{4}{3}{4}arg: {5}".format(conf.log.timepre, datetime.datetime.now(), conf.log.timepos, str(self.client_address), conf.log.separator, arg))
        if   arg == "css":                    self.send(open(conf.path.css  , "r" ).read().encode("utf8"), "text/css" )
        elif arg == "setup":                  self.send(open(conf.path.setup, "rb").read().encode("utf8"), "image/png")
        elif arg in ["ico", "favicon.ico"]:   self.send(open(conf.path.ico  , "rb").read().encode("utf8"), "image/png")
        elif arg in conf.navbar.paths + [""]: self.build(arg)
        else:                                 self.build("404")

template = open(conf.path.template, "r").read() # loads html template
conf = json.loads(open("conf.json").read(), object_hook=lambda d: namedtuple("X", d.keys())(*d.values())) # read config.json and convert it into object
print("Starting webserver")
HTTPServer((conf.address, conf.port), S).serve_forever() # start http server
