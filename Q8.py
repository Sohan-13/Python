#accept a character and display whether it is upper case or lower case or not an alphabet
k = input("Enter a single character")
if(ord(k)>=65 and ord(k)<91):
    print("upper case")
elif(ord(k)>=97 and ord(k)<123):
    print("lower case")
else:
    print("invalid")








