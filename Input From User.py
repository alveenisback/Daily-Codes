
n = input("enter a text of numbers : ")
# 10 20 30 50
list = n.split() # 10,20,40,60
sum = 0

for num in list:
    sum = sum + int (num)

print(sum)

numofwords = 0
numofletters = 0
numofdigits = 0

text = input("enter a text of numbers : ") #my name is 123

for x in text:
    x = x.lower()()
    if x >= "a" and x <= "z":
        numofletters = numofletters + 1
    elif x >= "0" and x <="9"