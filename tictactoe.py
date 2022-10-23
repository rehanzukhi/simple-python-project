import random
def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile == True:
        print("True")
        return True
    elif a_smile and b_smile ==False:
        print("True")
        return True
    else: 
        print("False")
        return False
monkey_trouble(a_smile=random.choice([True, False]), b_smile=random.choice([True, False]))