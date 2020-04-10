# randacek.dev - my personal webserver software
# Copyright (C) 2020  Prokop Randáček
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import re, ssl
from http.server import HTTPServer, BaseHTTPRequestHandler
from log import log
from config import c
from image import imageDB
from pageBuilder import build

ansi_filter = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
template = open(c.path.template, "r").read() # loads html template

class S(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass
    
    def send(self, data, contentType): # universal data sending function
        self.send_response(200)
        self.send_header("Content-type", contentType)
        self.end_headers()
        self.wfile.write(data)


    def do_GET(self): # is called when server receives get request
        arg = self.path[1:]
        log(["GET REQUEST", str(self.client_address), "arg: " + arg])
        if   arg == "":                     self.send(build("home"))
        elif arg == "css":                  self.send(open(c.path.css  , "r" ).read().encode("utf8"), "text/css" )
        elif arg == "font":                 self.send(open(c.path.font , "rb").read()               , "font/ttf" )
        elif arg == "setup":                self.send(open(c.path.setup, "rb").read()               , "image/png")
        elif arg in ["ico", "favicon.ico"]: self.send(open(c.path.ico  , "rb").read()               , "image/png")
        elif arg == "info":                 self.send(build("nf"))
        elif arg in c.navbar.paths:         self.send(build(arg))
        else:                               self.send(build("404"))
    
    def do_POST(self):
        pass

def start():
    httpd = HTTPServer((c.address, c.port), S)
    httpd.socket = ssl.wrap_socket(httpd.socket,
                                   server_side=True,
                                   certfile='/etc/letsencrypt/live/randacek.dev/fullchain.pem',
                                   keyfile='/etc/letsencrypt/live/randacek.dev/privkey.pem',
                                   ssl_version=ssl.PROTOCOL_TLSv1)
    httpd.serve_forever()
