htmlStart = """
<!doctype html>
<html>
<head>
<title>randacek.dev - """
htmlHeader = """
</title>
<link rel="stylesheet" href="css">
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
navbarNames = ["Home", "My fav xkcd", "Tools", "Social Media"]
navbarPaths = ["home", "xkcd",        "tools", "sm"]
navbarPre = "<div class=\"navbar\">"
navbarSeparator = "<span> | </span>"
navbarCurrentItemPre = "<span class=\"current\"><a href=\""
navbarItemPre = "<span><a href=\""
navbarItemPrePosSeparator = "\">"
navbarItemPos = "</a></span>"
navbarPos = "</div>"

contentPre = "<p>"
contentPos = "</p></div>"

footer = """
<div class="footer">
<a href="https://github.com/ProkopRandacek/randacek.dev">source</a>
</div>
</body>
</html>"""

def Build(ID):
    ID = navbarPaths.index(ID)
    html = htmlStart + navbarNames[ID] + htmlHeader + navbarPre
    for i in range(len(navbarNames)):
        html += navbarCurrentItemPre if i == ID else navbarItemPre
        html += navbarPaths[i]
        html += navbarItemPrePosSeparator
        html += navbarNames[i]
        html += navbarItemPos
        html += "" if i == len(navbarNames) - 1 else navbarSeparator
    html += navbarPos
    html += contentPre
    html += "test generated lol"
    html += contentPos
    html += footer
    return html
