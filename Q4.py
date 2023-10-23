# accept a number,string,decimal,boolean value and a character from the user and store it inside the list. 
# First print the list from the beginning and then from the end

k = int(input("Enter number"))
k1 = input("Enter string")
k2 = float(input("Enter float"))
k3 = bool(input("Enter bool"))
k4 = input("Enter character")
a=[k,k1,k2,k3,k4]
print(a)
print(a[::-1])