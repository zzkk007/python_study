from time import ctime, sleep

def timefun(func):
    def wrappedfunc():
        print("%s called at %s"%(func.__name__, ctime()))
        return func()
    return wrappedfunc

@timefun
def getInfo():
    return '----hahah---'


print(getInfo())

