import time, random, json
from log import log
from config import c

base62 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']

class image():
    name = None
    creationTime = None

    def __init__():
        self.name = genId()
        self.creationTime = time.time()
        log(f"image {name} was created with time {time}", True)

    def __del__():
        log(f"deleting image {self.name}", True)
        # TODO

class imageDB():
    images = None

    def __init__(self):
        images = imageDB.load(c.path.imageDB)

    def __del__(self):
        imageDB.save(images)

    def clear(self):
        nowTime = time.time()
        log("clearing images")
        c = 0
        for i in images:
            if (nowTime - i.creationTime) > c.image.maxAge:
                c += 1
                del(i)
        log("clearing done", f"{c} images deleted in {time.time() - nowTime} seconds")

    def genId():
        while True:
            name = random.choices(base62, k=nameLen)
            for i in imageDB.images:
                if name == i.name:
                    break
            else:
                return name

    def getImage(Id):
        pass
        #TODO

    def uploadImage():
        pass
        #TODO

    def handleRequest(arg):
        if arg.startswith("upload"): pass
        #TODO

    @staticmethod
    def load(DB):
        log("loading image DB")
        #TODO

    @staticmethod
    def save(DB):
        log("saving image DB")
        #TODO
