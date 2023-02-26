import random

use=input("Enter your name:")

print("Rock and paper game :")

print("Enter")



rock='''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)

stone
'''

scissor='''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)

scissor
'''  

papper='''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)

paper
'''

comp=0
user=0
i=3
while i>0:
    numbyus=int(input("\n\n1:ROCK\n2:SCISSOR\n3:PAPPER\n"))

    print("You choosen\n")

    if numbyus==1:
        print(rock)
    elif numbyus==2:
        print(scissor)
    elif numbyus==3:
        print(papper)
    else:
        print("invalid input")
    
    print("\nComputer choosen\n")

    num_comp=random.randint(1,3)

    if num_comp==1:
        print(rock)
    elif num_comp==2:
        print(scissor)
    elif num_comp==3:
        print(papper)


    if numbyus==num_comp:
        print("No points")
    elif numbyus==1 and num_comp==2:
        comp=comp+1
        print("computer get point ")
        i=i-1
    elif numbyus==1 and num_comp==3:
        user=user+1
        print("user get point")
        i=i-1
    elif numbyus==2 and num_comp==1:
        comp=comp+1
        print("computer get point ")
        i=i-1
    elif numbyus==2 and num_comp==3:
        user=user+1
        print("user get point")
        i=i-1
    elif numbyus==3 and num_comp==2:
        comp=comp+1
        print("computer get point ")
        i=i-1
    elif numbyus==3 and num_comp==1:
        user=user+1
        print("user get point")
        i=i-1


if comp>user:
    print("\n\nwinner is computer")
else:
    print(F"\n\n wineer is {use}")
