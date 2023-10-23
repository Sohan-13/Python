# define "myfun1()" with a print statement. now define "myfun2()" which should invoke "myfun1()" function. 
# invoke myfun2()

def myfun1():
    print("In myfun1")
def myfun2():
    print("In myfun2")
    myfun1()
myfun2()