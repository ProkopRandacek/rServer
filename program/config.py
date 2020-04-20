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

rules = {}
contentTypes = {}


def rulesReader(path):
    f = open(path).read().split("\n")
    for line in rulesfile:
        line = line.replace(" ", "").split("#")[0].split("=")
        if not len(line) == 2:
            continue
        rules[line[0]] = line[1]


c = json.loads(
    open("conf.json").read(),
    object_hook=lambda d: namedtuple("X", d.keys())(*d.values()),
)


rules = rulesReader(c.path.rules)
contentTypes = rulesReader(c.path.contentTypes)
