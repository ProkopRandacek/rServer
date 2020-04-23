# randacek.dev - my personal webserver software
# Copyright (C) 2020  Prokop Randáček
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import json
from collections import namedtuple


configPath = "../config/conf.json"


rules = {}
contentTypes = {}


def rulesReader(path):
    d = {}
    f = open(path).read().split("\n")
    for line in f:
        line = line.split("#")[0].split("=")
        if not len(line) == 2:
            continue
        if ";" in line[1]:
            line[1] = list(
                map(
                    lambda x: x.strip().replace("&e", "=").replace("&s", " "),
                    line[1].split(";"),
                )
            )
        else:
            line[1] = line[1].strip().replace("&e", "=").replace("&s", " ")
        d[line[0].strip()] = line[1]
    return d


c = json.loads(
    open(configPath).read(),
    object_hook=lambda d: namedtuple("X", d.keys())(*d.values()),
)


rules = rulesReader(c.path.root + c.path.rules)
contentTypes = rulesReader(c.path.root + c.path.contentTypes)
navbar = rulesReader(c.path.root + c.path.navbar)
