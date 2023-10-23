#display prime numbers from 3 to 30

for i in range(3,31):
    for j in range(2,i-1):
        if(i%j==0):
            break
    
    else:
        print(i ,"Prime")