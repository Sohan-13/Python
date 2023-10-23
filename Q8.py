# Note: use List comprehension
# create a list with the numbers from 1 to 20
# create one more list which should contain only odd numbers from the first list

a=[i for i in range(1,21)]
print(a)

b=[i for i in a if(i%2!=0)]
print(b)


