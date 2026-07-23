#constructor overloding
class Test:
    def __init__(self,a=None,b=None):
        print("no-arg constructor")
    def __init__(self,a):
        print("one-arg constru")
    def __init__(self,a,b):
        print("Two-arg constru")
t1=Test(10,20)

      