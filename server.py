import datetime, markdown2, json, subprocess, re
from collections import namedtuple
from http.server import HTTPServer, BaseHTTPRequestHandler

ansi_filter = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

def log(m):
    m = f"{c.log.timepre}{datetime.datetime.now()}{c.log.timepos}{c.log.separator}" + m
    print(m)
    logfile.write(m)

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
        navbarNum = c.navbar.paths.index(path) if path in c.navbar.paths else -1
        title     = path if navbarNum == -1 else c.navbar.names[navbarNum]
        if path   == "nf": subprocess.call(['./nf.sh'])
        content   = open(c.path.content + path + ".md", "r").read()
        content   = ansi_filter.sub("", content.replace("\n", "<br>").replace(" ", "&nbsp;")) if path == "nf" else markdown2.markdown(open(c.path.content + path + ".md", "r").read())
        navbar    = ""
        for i in range(len(c.navbar.names)): # builds navbar
            navbar += c.navbar.item.pre
            navbar += c.navbar.item.current if i == navbarNum else "" # current item is highlighted
            navbar += c.navbar.item.prepath
            navbar += c.navbar.paths[i]
            navbar += c.navbar.item.separator
            navbar += c.navbar.names[i]
            navbar += c.navbar.item.pos
            navbar += "" if i == len(c.navbar.names) - 1 else c.navbar.separator # last item doesnt have separator after
        html = template.replace("{title}", title).replace("{navbar}", navbar).replace("{content}", content) # insert contents into html template
        self.send(html.encode("utf8"), "text/html") # sends data

    def do_GET(self): # is called when server receives get request
        arg = self.path[1:] # self.path always starts with "/"
        log(f"{str(self.client_address)}{c.log.separator}arg: {arg}")
        if   arg == "":             self.build("home")
        elif arg == "css":          self.send(open(c.path.css  , "r" ).read().encode("utf8"), "text/css" )
        elif arg == "font":         self.send(open(c.path.font , "rb").read()               , "font/ttf" )
        elif arg == "setup":        self.send(open(c.path.setup, "rb").read()               , "image/png")
        elif arg in "ico":          self.send(open(c.path.ico  , "rb").read()               , "image/png")
        elif arg == "info":   self.build("nf")
        elif arg in c.navbar.paths: self.build(arg)
        else:                       self.build("404")

c = json.loads(open("conf.json").read(), object_hook=lambda d: namedtuple("X", d.keys())(*d.values())) # read cig.json and convert it into object

logfile = open(c.path.log, "w")
template = open(c.path.template, "r").read() # loads html template

log("Starting webserver")
HTTPServer((c.address, c.port), S).serve_forever() # start http server
