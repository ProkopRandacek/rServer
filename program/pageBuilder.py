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
from config import c, navbar, rules

template = open(c.path.root + c.path.template, "r").read()  # loads html template
navbarPaths = []
for link in navbar["links"]:  # get filepaths of files that are linked in navbar
    if link in rules:
        navbarPaths.append(c.path.root + rules[link])


def navbarer(navbarNum):
    n = ""
    for i in range(len(navbar["names"])):  # builds navbar
        n += navbar["pre"]
        n += navbar["current"] if i == navbarNum else ""  # current item is highlighted
        n += navbar["prepath"]
        n += navbar["links"][i]
        n += navbar["itemSeparator"]
        n += navbar["names"][i]
        n += navbar["pos"]
        n += (
            "" if i == len(navbar["names"]) - 1 else navbar["separator"]
        )  # last item doesnt have separator after
    return n


def contenter(table):
    html = template
    for i in table:
        html = html.replace(i[0], i[1])
    return html


def buildMD(path):
    content = markdown2.markdown(open(path, "r").read())
    return build(path, content)


def build(path, content=None):
    if content == None:
        content = open(path, "r").read()
    content = content.replace("{usetemplate}", "")
    navbarNum = navbarPaths.index(path) if path in navbarPaths else -1
    title = path if navbarNum == -1 else navbar["names"][navbarNum]
    n = navbarer(navbarNum)
    html = contenter([["{title}", title], ["{navbar}", n], ["{content}", content]])
    return html
