import time, random, json
from collections import namedtuple
from log import log
from config import c

base62 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']

class image():
    name = None
    creationTime = None

    def __init__(self, name, creationTime):
        self.name = name
        self.creationTime = creationTime
        log(f"image {self.name} was created with time {self.creationTime}", True)

    def delete(self):
        log(f"deleting image {self.name}", True)
        #TODO delete the file

class imageDB():
    images = [] 
    def __init__(self):
        self.load()

    def clear(self):
        nowTime = self.getTime();
        log("clearing images")
        n = 0
        for i in self.images:
            print(i.name, i.creationTime, nowTime - i.creationTime, (nowTime - i.creationTime) > c.image.maxAge)
            if (nowTime - i.creationTime) > c.image.maxAge:
                n += 1
                i.delete()
                self.images.remove(i)
        log(["clearing done", f"{n} images deleted in {int(1000*(time.time() - nowTime))/1000} seconds"])

    def genId(self):
        while True:
            name = random.choices(base62, k=c.image.idLen)
            for i in self.images:
                if name == i.name:
                    break
            else:
                return "".join(name)

    def getTime(self):
        return int(time.time())

    def getImage(self, Id):
        pass
        #TODO

    def uploadImage(self):
        #TODO
        if len(self.images) > 62*62*62/100: self.clear()
        self.images.append(image(self.genId(), self.getTime()))

    def save(self):
        log("saving image DB")
        with open(c.path.imageDB, "w") as data:
            for i in self.images:
                data.write(f"{i.name};{i.creationTime}\n")
        log("image DB saved")

    def load(self):
        log("loading image DB")
        data = open(c.path.imageDB, "r").read().split("\n")
        for i in data[:-1]: # last index is allways empty
            self.images.append(image(i[:3], int(i[4:])))
        log(["loading images done", f"{len(self.images)} images loaded"])

db = imageDB()

for i in db.images:
    print(i.name, i.creationTime)

input()

db.uploadImage()

for i in db.images:
    print(i.name, i.creationTime)

db.clear()
db.save()
