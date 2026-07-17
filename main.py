import random
'''
1 for snake
0 for gun
-1 for water
'''
computer=random.choice([-1,1,0])
youstr=input("Enter your Choice:")#ask s,w or g as input
youDict={"s":1,"w":-1,"g":0}#given key as well as value
reverseDict={1:"snake",-1:"water",0:"Gun"}#its for computer choice

you=youDict[youstr]#keyValue assigned in youNum

print(f"you choose:{reverseDict[you]}\nComputer choice:{reverseDict[computer]}")


if(computer==you):
    print("It's a draw!")

else:    
  if(computer==-1 and you==1):
    print("you win!")

  elif(computer==-1 and you==0):
    print("you lose!")

  elif(computer==1 and you==-1):
    print("You lose!")

  elif(computer==1 and you==0):
    print("you win!")

  elif(computer==0 and you==-1):
    print("you win!")

  elif(computer==0 and you==1):
    print("you lose!")

  else:
    print("Some thing went wrong")                        