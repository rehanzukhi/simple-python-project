import random
user_id = 1101
database=[{"Question":"What is the captial of India?","Options":["1)New Delhi","2)Hyderabad","3)Dubai"],"Correct":1},
          {"Question":"What is the captial of China?","Options":["1)New Delhi","2)Hyderabad","3)Beijing"],"Correct":3},
          {"Question":"What is the captial of UAE?","Options":["1)Dubai","2)Hyderabad","3)Abu Dhabi"],"Correct":3},
          {"Question":"What is the captial of Germany?","Options":["1)New Delhi","2)Berlin","3)Dubai"],"Correct":2},
          {"Question":"What is the captial of Australia?","Options":["1)New Delhi","2)Hyderabad","3)Melbourne"],"Correct":3},
          {"Question":"What is the captial of Srilanka?","Options":["1)New Delhi","2)Hyderabad","3)Columbo"],"Correct":3},
          {"Question":"What is the captial of Saudi Arabia?","Options":["1)Riyadh","2)Hyderabad","3)Dubai"],"Correct":1},
          {"Question":"What is the captial of Japan?","Options":["1)Bangalore","2)Tokyo","3)Dubai"],"Correct":2},
          {"Question":"What is the captial of lATVIA?","Options":["1)Riga","2)Rezkne","3)Dubai"],"Correct":1}]
print("Let's BEGIN the Quiz!")
def teacher():
  ui=int(input("Enter your user id : \n"))
  if ui==user_id:
    q=input("Would you like to add new Questions? Y/N \n")
    if q=="Y":
      new_que=input('Enter Question : ' )
      newdict={"Question":new_que}
      print(newdict)
      choices=input("Enter choices in a list : ")
      choice_list=[choices]
      newdict["Options"]=choice_list
      print(newdict)
      correct_ans=int(input("Enter the correct Answer : "))
      newdict["Correct"]=correct_ans
      print(newdict)
      database.append(newdict)
  else:
    print("You are not authorized to make any Modifications!")
    
#      database.append()
def game():
  score=0
  question=0
  while question in range(5):
      a=random.randint(0,len(database)-1)
      print(database[a]["Question"])
      print(database[a]["Options"])
      b=int(input("Enter the Right Option - 1/2/3:\n"))
      if b==database[a]["Correct"]:
        print("Right Answer")
        score+=1
        print(f"Your Score is {score}")
        question+=1
        print(f"{question} Question Answered\n")
      else:
        print("Wrong answer")  
        question+=1
        print(f"{question} Question Answered\n")
      if question==5:
        break
def playagain():
  playagain=input("Do you want to Play Again? (Y/N) \n")
  if playagain=="Y":
    game()
  elif playagain=="N":
    print("Thank you for Playing!")
  else:
    print("Wrong INPUT Recieved !")

while True:
  userinput=input('Welcome, Are you a teacher, or Do you want to take the Quiz?\n Enter "T" if you are a teacher \n "Enter "Q if you want to take the quiz! \n')
  if userinput=="T":
    teacher()
  elif userinput=="Q":
    game()
    playagain()
  else:
    break