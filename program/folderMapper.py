import sys, os
from config import c


files = []
path = c.path.root + sys.argv[1]


def yesNoInput(text):
    while True:
        i = input(text + " [Y/n] ").lower()
        if i in ["yes", "y", "no", "n", ""]:
            break
        else:
            print("You did not enter a valid answer")
    return True if i in ["yes", "y", ""] else False


def r(path):
    ls = os.listdir(path)
    for i in ls:
        if i[0] == ".":
            continue
        if os.path.isfile(path + i):
            files.append(path + i)
        elif os.path.isdir(path + i):
            r(path + i + "/")


if not os.path.isdir(path):
    raise NotADirectoryError(f"{path} does not exist.")

r(path)

print("I found these files:\n" + "\n".join(files) + "\n(" + str(len(files)) + " files)")

start = input("Exclude files that start with (Leave empty to skip): ")
end = input("Exclude files that end with (Leave empty to skip): ")
if start == "":
    start = " "  # I assume that files cannot start nor end with a space
if end == "":
    end = " "

for i in files:
    if i.startswith(start) or i.endswith(end):
        del files[files.index(i)]

urls = files

if not yesNoInput("Do you want to include file extensions in url?"):
    newurls = []
    for i in urls:
        toadd = ".".join(i.split(".")[:-1])
        if toadd == "":
            newurls.append(i)
        else:
            newurls.append(toadd)
    urls = newurls

if yesNoInput("Do you want to replace something in the urls?"):
    a = input("Replace this: ")
    b = input("With this: ")
    for i in range(len(files)):
        urls[i] = urls[i].replace(a, b)

rules = []
for (p, r) in zip(urls, files):
    rules.append(p[len(c.path.root) :] + " = " + r)

print("Generated rules:\n" + "\n".join(rules))
if not yesNoInput("Continue?"):
    exit()
