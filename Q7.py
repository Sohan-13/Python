#accept numbers till user enters 0 and display the total of all the numbers entered
sum = 0
for i in iter(int,True):
    k = int(input("Enter number"))
    if(k==0):
        break
    sum+=k
print(sum)
