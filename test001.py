from time import ctime, sleep


def timefunc_age(pre="hello"):
    def timefunc(func):
        def wrappedfunc():
            print("%s called at %s %s" % (func.__name__, ctime(), pre))
            return func()
        return  wrappedfunc
    return timefunc


@timefunc_age('world')
def foo():
    print('I am foo')

foo()

