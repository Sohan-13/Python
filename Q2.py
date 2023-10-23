# define nested function and show how will you invoke it.

def myfun():
    def myfun1():
        print("inside myfun1")
    return myfun1
    
myfun()()
k = myfun()
k()