import markdown2

htmlStart = """
<!doctype html>
<html>
<head>
<title>randacek.dev - """
htmlHeader = """
</title>
<link rel="stylesheet" href="css">
<link rel="icon" type="image/png" href="ico">
<meta charset="utf-8">
<meta name="author" content="Prokop Randáček">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<div class="header">
<h1>randacek.dev</h1>
<p class="textik">Prokop Randáček's web.</p>
</div>
<div class="content">"""

navbarNames = ["Home", "My fav xkcd", "Tools", "Social Media", "404"]
navbarPaths = ["home", "xkcd",        "tools", "sm",           "404"]
navbarPre = "<div class=\"navbar\">"
navbarSeparator = "<span> | </span>"
navbarCurrentItemPre = "<span class=\"current\"><a href=\""
navbarItemPre = "<span><a href=\""
navbarItemPrePosSeparator = "\">"
navbarItemPos = "</a></span>"
navbarPos = "</div>"

footer = """
</div>
<div class="footer">
<a href="https://github.com/ProkopRandacek/randacek.dev">source</a>
</div>
</body>
</html>"""

def Build(ID):
    ID = navbarPaths.index(ID)
    html = htmlStart + navbarNames[ID] + htmlHeader

    html += navbarPre
    for i in range(len(navbarNames[:-1])):
        html += navbarCurrentItemPre if i == ID else navbarItemPre
        html += navbarPaths[i]
        html += navbarItemPrePosSeparator
        html += navbarNames[i]
        html += navbarItemPos
        html += "" if i == len(navbarNames) - 2 else navbarSeparator
    html += navbarPos

    html += markdown2.markdown(open("assets/content/" + navbarPaths[ID] + ".md", 'r').read())

    html += footer
    return html
