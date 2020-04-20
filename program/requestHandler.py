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

import ssl
from http.server import HTTPServer, BaseHTTPRequestHandler
from log import log
from config import c
from image import imageDB
from pageBuilder import build


class S(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def send(self, data, contentType):  # universal data sending function
        self.send_response(200)
        self.send_header("Content-type", contentType)
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):  # is called when server receives get request
        arg = self.path[1:]
        log(["GET REQUEST", str(self.client_address), "arg: " + arg])
        if arg == "css":
            self.send(open(c.path.css, "r").read().encode("utf8"), "text/css")
        elif arg == "robots.txt":
            self.send(open(c.path.robots, "r").read().encode("utf8"), "text/plain")
        elif arg == "sitemap.xml":
            self.send(open(c.path.sitemap, "r").read().encode("utf8"), "text/xml")
        elif arg == "font":
            self.send(open(c.path.font, "rb").read(), "font/ttf")
        elif arg == "rukopis":
            self.send(open(c.path.rukopis, "rb").read(), "font/ttf")
        elif arg == "setup":
            self.send(open(c.path.setup, "rb").read(), "image/png")
        elif arg in ["ico", "favicon.ico"]:
            self.send(open(c.path.ico, "rb").read(), "image/png")
        elif arg in c.navbar.paths + [""] or arg.startswith("stuff"):
            self.send(build(arg), "text/html")
        else:
            self.send(build("404"), "text/html")

    def do_POST(self):
        pass


def start():
    httpd = HTTPServer((c.address, c.port), S)
    httpd.socket = ssl.wrap_socket(
        httpd.socket,
        server_side=True,
        certfile="/etc/letsencrypt/live/randacek.dev/fullchain.pem",
        keyfile="/etc/letsencrypt/live/randacek.dev/privkey.pem",
        ssl_version=ssl.PROTOCOL_TLSv1_2,
    )
    httpd.serve_forever()
