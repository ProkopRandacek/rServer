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

import datetime, inspect
from config import c

open(c.path.log, "w").write("")
logfile = open(c.path.log, "a")


def log(m, d=False):
    if d and not c.debug:
        return
    if not isinstance(m, list):
        m = [m]
    filename = inspect.stack()[1][0].f_code.co_filename.split("/")[-1][:-3]
    m = f"{c.log.timepre}{datetime.datetime.now()}{c.log.timepos}{c.log.separator}{filename:<14}{c.log.separator}{c.log.separator.join(m)}"
    print(m)
    if c.log.saveToFile:
        logfile.write(m + "\n")
