#  create a list , accept a number,name and a float value from user and store it inside the list.  
# now accept one more name from user and insert it at 2nd position.
# accept a number and append it at the end of the list.
# print the entire list.
a = [1,2,3,4,5]
print(a)
k = int(input("Enter a number"))
k1 = float(input("Enter a float number"))
k2 = input("Enter string")
a.append(k)
a.append(k1)
a.insert(2,k2)
print(a)