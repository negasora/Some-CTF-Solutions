
import time

secret2 = "aaaaaaaaaaaaaaaaaaa"

class other(object):
    def __init__(self, a):
        self.a = a

class pls(object):
    def __init__(self):
        self.id = 123
        self.rating = 123
        self.author = ""
        self.comments = list()
        pass
    def f(self):
        self.comments.append(other("what"))
        print("{a[comments].__dir__}".format(a=self.__dict__))
        a = self.comments[0].__init__.__globals__
        print(a)
        print(dir(a))
    

def aaa():
    a = pls()
    a.f()

