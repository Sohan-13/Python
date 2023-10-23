# first create list empty. accept numbers till user enters 0 and store them inside the list. Print the list and its length

a = []
n=1
while(n!=0):
    n = int(input("Enter element"))
    if(n!=0):
        a.append(n)
print(a)
print("length is ", len(a))


