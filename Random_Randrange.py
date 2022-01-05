import random

x1=random.randrange(10,30)
x2=random.randrange(10,30)
rand_x2="The second random number is: {}"
print(f"The first random number is: {x1}")
print(rand_x2.format(x2))

inp=int(input("Please enter the sum of these two numbers: "))
print(inp)

if inp==x1+x2:
    print("Your answer is correct")
else:
     print("Your answer is not correct")  

