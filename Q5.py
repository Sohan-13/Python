# accept 5 numbers, store them inside the list. now accept a number from user which he would like to remove 
# from the list and  after removing it, display the list.

a=[]
for i in range(1,6):
    n=int(input("enter number"))
    a.append(n)
print(a)

n1 = int(input("now enter a number to remove it from the list"))
a.remove(n1)
print(a)