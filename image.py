import time, random, json
from collections import namedtuple
from log import log
from config import c

base62 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']

class image():
    name = None
    creationTime = None

    def __init__(self, name):
        self.name = name
        self.creationTime = time.time()
        log(f"image {self.name} was created with time {self.creationTime}", True)

    def __del__(self):
        log(f"deleting image {self.name}", True)
        # TODO

class imageDB():
    images = [] 
    def __init__(self):
        #self.images = imageDB.load(c.path.imageDB)
        self.images = [image(self.genId()), image(self.genId())]

    def __del__(self):
        imageDB.save(self.images)

    def clear(self):
        nowTime = time.time()
        log("clearing images")
        c = 0
        for i in self.images:
            if (nowTime - i.creationTime) > c.image.maxAge:
                c += 1
                del(i)
        log("clearing done", f"{c} images deleted in {time.time() - nowTime} seconds")

    def genId(self):
        while True:
            name = random.choices(base62, k=c.image.idLen)
            for i in self.images:
                if name == i.name:
                    break
            else:
                return "".join(name)

    def getImage(self, Id):
        pass
        #TODO

    def uploadImage(self):
        pass
        #TODO

    def handleRequest(arg):
        if arg.startswith("upload"): pass
        #TODO

    @staticmethod
    def load(DB):
        log("loading image DB")
        return json.loads(open(c.path.imageDB, "r").read(), object_hook=lambda d: namedtuple("X", d.keys())(*d.values()))

    @staticmethod
    def save(DB):
        log("saving image DB")
        open(c.path.imageDB, "w").write(json.dumps(DB, default=lambda x: x.__dict__))
