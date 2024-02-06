# 2 + 4 + .......+n
# int for numbers
#str for letters

n = int(input("enter the last digit : "))
sum = 0
i = 1
while i <= n :
    sum = sum + i
    i = i + 2

print(sum)