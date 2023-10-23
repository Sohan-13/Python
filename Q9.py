#display fibonicii series of 10 numbers
a=0
b=1
s=1
print(a)
print(b)
for i in range(0,9):
    print(s)
    a=b
    b=s
    s=a+b  