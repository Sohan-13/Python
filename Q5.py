# define a function to accept a number. This function should return 1 if a number passed is more than 0
# return -1 if a number passed is less than 0 , else it should return 0.

def myfun(k):
    if(k>0):
        return 1
    elif(k==0):
        return 0
    else:
        return -1
    
        
k1 = int(input("enter number"))
print(myfun(k1))

    