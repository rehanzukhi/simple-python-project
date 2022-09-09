database = {}


def main(id,name):
    global database

    database[id] = {}
    temp = {}
    temp["name"] = name
    temp["account"] = 0 
    temp["history"] = [0]
    database[id] = temp
    print("You Account Has been Created Succesfully.")

def deposit(id,amount):
    global database

    database[id]["account"] += amount
    database[id]["history"].append(amount)

def withdraw(id,amount):
    global database

    database[id]["account"] -= amount
    database[id]["history"].append(-amount)

def display(id):
    global database

    print(database[id])

def history(id):
    global database

    print(database[id]["history"])


while True:
    user_input = input("Welcome, Hope You are Having a Good day!!!\n Select from the below options, how may we help you?\n0.Create an Account(Type- create)\nA. View Balance(Type - display)\nB. Deposit Cash(Type - deposit)\nC. Withdraw Cash(Type -withdraw)\nD. View Previous Transaction(Type -history)\nE. Exit(Type -quit)\n ")
    if user_input == "quit":
        break

    if user_input == "display":
        id = int(input("Please Enter your id for displaying account details!\n"))
        if id in database:
            display(id)
           
        else:
            print("invalid id")


    if user_input == "create":
        id = int(input("Enter your id\n"))
        name = input("Enter your name\n")

        if id not in database:

            main(id,name)
        else:
            print("Id already used.")

    if user_input == "deposit":
        id = int(input("enter id"))
        if id in database:
            amount = int(input("Please Enter amount to be deposited."))
            deposit(id,amount)
        else:
            print("invalid id")

    if user_input == "withdraw":
        id = int(input("enter id"))
        if id in database:
            amount = int(input("Please Enter amount to be withdrawn."))
            withdraw(id,amount)
        else:
            print("invalid id")

    if user_input == "history":
        id = int(input("enter id"))
        if id in database:
            history(id)
        else:
            print("invalid id")




    