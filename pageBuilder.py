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

import subprocess, markdown2, re
from config import c 

ansi_filter = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
template = open(c.path.template, "r").read() # loads html template

def build(path): # builds and sends html page from markdown file
    r = False
    if path[-1] == "r":
        path = path[:-1]
        r = True
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
    if r: html = html.replace("font", "rukopis")
    return html.encode("utf8") # returns data
