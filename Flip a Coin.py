import random

sides=["Heads","Tails"]
def main():
    print("Let's flip a coin!")
    a=input("Which side you choose? \n Heads or Tails?")
    if a=="Heads":
        print("You chose heads!")
    else:
        print("You chose tails!")
    computer=random.choice(sides)
    if computer=="Heads" and a=="Heads":
        print("You won!")
    elif computer=="Tails" and a=="Tails":
        print("You won!")
    elif computer=="Heads" and a=="Tails":
        print("You lost!")
    elif computer=="Tails" and a=="Heads":
        print("You lost!")
main()