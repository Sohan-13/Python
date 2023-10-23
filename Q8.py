# write a function to accept minimum 3 characters and maximum 5 characters. 
# 	[ use default arguments method ]

def myfun(k1):
    print(k1)
        

k = input("enter string")
if(len(k)>=3 and len(k)<=5):
    myfun(k)
else:
    print("invalid")