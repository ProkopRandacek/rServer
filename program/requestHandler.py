# rServer - simple webserver
# Copyright (C) 2020  Prokop Randáček
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import ssl, os.path
from http.server import HTTPServer, BaseHTTPRequestHandler
from log import log
from config import c, rules, contentTypes
from pageBuilder import build

if not os.path.isfile(c.path.root + c.path.notfound):
    raise FileNotFoundError(
        f"There is no such file {c.path.root + c.path.notfound} (from conf.json; path.notfound)."
    )


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
        path = ""
        header = ""
        for (rule, p) in rules.items():
            if rule == arg:
                path = c.path.root + p
                break
        else:
            path = c.path.root + c.path.notfound
        if not os.path.isfile(path):
            path = c.path.root + c.path.notfound
        for (ct, h) in contentTypes.items():
            if path.endswith(f".{ct}"):
                header = h
                break
        else:
            header = "text/plain"
        if path.endswith(".md"):
            data = build(path)
        else:
            data = open(data, "r").read()
        if header.split("/")[0] == "text":
            data = data.encode("utf-8")
        self.send(data, header)

    def do_POST(self):
        pass


def start():
    httpd = HTTPServer((c.address, c.port), S)
    """httpd.socket = ssl.wrap_socket(
        httpd.socket,
        server_side=True,
        certfile=c.path.certfile,
        keyfile=c.path.keyfile,
        ssl_version=ssl.PROTOCOL_TLSv1_2,
    )"""
    httpd.serve_forever()
