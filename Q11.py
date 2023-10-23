#accept a number and display whether it is prime or not
k = int(input("Enter number"))
if(k==0 or k==1):
    print("Neither prime nor composite")
else:
    for i in range(2,k-1):
        if(k%i==0):
            print(k ,"Not prime")
            break
    else:
        print(k , "Prime")