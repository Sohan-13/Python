# define a function in such a way that it can accept n number of values and print their sum. [ variable number of arguments]


total = 0
def myfun(*vars):
    for i in vars:
        global total
        total = total + i
    print(total)
myfun(10,20,30)

        

