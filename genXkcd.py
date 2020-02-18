inp = open("assets/xkcd.txt", 'r')
out = open("assets/content/xkcd.md", 'w')
out.write(open("assets/content/xkcdStart.md", 'r').read())
for i in inp.read().split("\n")[0:-1]:
    n = i.split(" ")
    out.write("- [" + n[0] + "](https://xkcd.com/" + i.split(" ")[0] + ") - " + n[-1] + "\n")
