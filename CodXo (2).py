import random
number=random.randint(1,100)
guess=0
while guess!=number:
    guess=int(input("enter guess:"))
    if(guess>number):
        print("guess higher!")
    elif(guess<number):
        print("guess lower!")
    else:
        print("good job")
