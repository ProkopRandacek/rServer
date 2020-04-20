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

import subprocess, markdown2, re, os.path
from config import c

template = open(c.path.template, "r").read()  # loads html template


def navbarer(navbarNum):
    navbar = ""
    for i in range(len(c.navbar.names)):  # builds navbar
        navbar += c.navbar.item.pre
        navbar += (
            c.navbar.item.current if i == navbarNum else ""
        )  # current item is highlighted
        navbar += c.navbar.item.prepath
        navbar += c.navbar.paths[i]
        navbar += c.navbar.item.separator
        navbar += c.navbar.names[i]
        navbar += c.navbar.item.pos
        navbar += (
            "" if i == len(c.navbar.names) - 1 else c.navbar.separator
        )  # last item doesnt have separator after
    return navbar


def contenter(table):
    html = template
    for i in table:
        html = html.replace(i[0], i[1])
    return html


def generate(path):
    navbarNum = c.navbar.paths.index(path) if path in c.navbar.paths else -1
    title = path if navbarNum == -1 else c.navbar.names[navbarNum]
    navbar = navbarer(navbarNum)
    content = markdown2.markdown(open(c.path.content + path + ".md", "r").read())
    html = contenter([["{title}", title], ["{navbar}", navbar], ["{content}", content]])


def build(path):  # builds and sends html page from markdown file
    if path == "stuff/":
        path = "stuff"
    elif path.startswith("stuff/"):
        return stuffReader(path)
    if path == "":
        path = "home"
    html = generate(path)
    return html.encode("utf8")  # returns data


def stuffReader(rawpath):
    path = rawpath.split("/")
    if os.path.isfile(c.path.stuff + rawpath + ".md"):
        pass
