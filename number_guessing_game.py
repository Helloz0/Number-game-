import random
secret_num=random.randint(1,100)
print("welcome to the guessing game ")
while True:
    num=int(input("enter your guess: "))
    if secret_num==num:
        print("you won")
        break
    elif num>secret_num:
        print("too high ")
    else :
        print("too low ")
     

   