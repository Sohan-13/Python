# accept 5 numbers, store them inside the list and display it. Now add 3 more numbers [hardcoded] at the end of the
# list using "extend" method.
k=[]
for i in range(1,6):
    n = int(input("enter number"))
    k.append(n)
print(k) 
k.extend([6,7,8]) 
print(k)  