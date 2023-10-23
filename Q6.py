# accept 5 numbers, store them inside the list. now accept a position from user ,remove the element from that 
# position and  after removing it, display the list.

a=[]
for i in range(1,6):
    n=int(input("enter number"))
    a.append(n)
print(a)

n1 = int(input("now enter a number to remove it from the list"))
a.pop(n1)
print(a)