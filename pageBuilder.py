import subprocess, markdown2
from config import c 

def build(path): # builds and sends html page from markdown file
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
    return html.encode("utf8"), "text/html" # returns data
