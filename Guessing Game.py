from random import randint

for x in range(1,6):

 guessnumbers = int(input("enter you guess between 1 to 5 : "))
randomnumber = randint(1,5)

if guessnumbers == randomnumber:
    print("you have won!")
else:
    print("you have lost!")
    print("you have lost! : ",randomnumber)