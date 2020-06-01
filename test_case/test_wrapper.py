def extend(fuc):
    def hello(*args,**kwargs):
        print("hello")
        fuc(*args,**kwargs)
        print("good bye")
    return hello()

@extend
def tep():
    print("tmp")

@extend
def tep1():
    print("tmp1")


def test_wrapper():
    tep()
    tep1