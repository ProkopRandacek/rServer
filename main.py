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

import requestHandler, sys, traceback, time
from log import log

fastErrorCount = 0  # Number of errors that happend with less than 10 s apart
lastErrorTime = 0  # When the last error happed


def main(args):
    if args == []:
        pass
    elif args == ["--debug"]:
        # TODO
        log("Debug log enabled")
    else:
        log(f'Unknown argument "{args[0]}"')
        exit()
    log("Starting webserver")
    requestHandler.start()


if __name__ == "__main__":
    while True:  # Cool self restarting when something crashes
        try:
            if len(sys.argv) > 0:
                main(sys.argv[1:])
            else:
                main([])
        except KeyboardInterrupt:
            log("KeyboardInterrupt")
            break
        except Exception:
            log("Error:\n" + traceback.format_exc())
            if time.time() - lastErrorTime < 10:
                fastErrorCount += 1
            else:
                fastErrorCount = 0
            if fastErrorCount > 6:
                log("Too many error in the past 60 seconds")
                break
            lastErrorTime = time.time()

        log("Trying to restart")
    log("Exiting")
