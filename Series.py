#1 x 2 3 x ..... x n

n = int(input("Enter the last number : "))
sum = 1

for x in range(2,n+1,1):
    sum = sum * x

print(sum)