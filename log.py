import datetime, inspect
from config import c

open(c.path.log, "w").write("")
logfile = open(c.path.log, "a")

def log(m, d=False):
    if d and not c.debug: return
    if not isinstance(m, list): m = [m]
    filename = inspect.stack()[1][0].f_code.co_filename.split("/")[-1][:-3]
    m = f"{c.log.timepre}{datetime.datetime.now()}{c.log.timepos}{c.log.separator}{filename:<14}{c.log.separator}{c.log.separator.join(m)}"
    print(m)
    if c.log.saveToFile: logfile.write(m + "\n")
