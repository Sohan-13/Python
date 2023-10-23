#accept marks from the user. Using if…….elif….  Else,  display whether result is  fail, pass, second class , first class, Distinction etc.
k = int(input("Enter marks"))
if(-1<k<36):
    print("Fail")
elif(35<k<50):
    print("Pass")
elif(49<k<60):
    print("Second class")
elif(59<k<75):
    print("First class")
elif(74<k<101):
    print("Distinction")
else:
    print("Invalid")
    