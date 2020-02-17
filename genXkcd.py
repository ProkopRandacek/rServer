inp = open("xkcd.txt", 'r')
out = open("xkcd.md", 'w')
for i in inp.read().split("\n")[0:-1]:
	out.write("- [" + i + "](https://xkcd.com/" + i.split(" ")[0] + ")\n")
