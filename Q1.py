# create 3 functions "show1()","show2()" and "show3()"
# now define a function "caller" in such a way that it can accept any function as an argument and invoke the same

def show1():
    print("show1")
def show2():
    print("show2")
def show3():
    print("show3")
def caller(k):
    k()
    
caller(show1)



