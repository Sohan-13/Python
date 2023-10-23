# accept 5 names and store them in list. Now sort the list in ascending order display and then in descending order.
a=[]
for i in range(1,6):
    n = input("enter name")
    a.append(n)
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
