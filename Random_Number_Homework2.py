import random
x=random.randrange(1,15)

print(x)
text=input("Could you guess the random number, please put a number: ")
while int(text)!=x:

    if int(text)>x:
        print("You haven't guessed it,It's greater than the random number please try again")
    elif int(text)<x:
         print("You haven't guessed it,It's less than the random number please try again")   
    text=input()
print("Congratulations, you have guessed it !!!!!!!")
