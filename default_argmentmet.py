class Test:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print("The sum of 2 number:",a+b)
        else:
            print('please provide at least 2&3 arg')
t=Test()
t.sum(10,20)
t.sum(10,20,30)
t.sum(10)
