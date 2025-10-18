print("WELCOME TO MY QUIZ GAME \n LET'S PLAY AND UNWIND THE GAME")
player=input("Do you want to play the game? (yes or no) \n")
if player.lower()=='no':
    print("GOOD BYE, HAVE A NICE DAY!")
    quit()
    
name_of_player= input("ENTER YOUR NAME PLEASE: ")

print("LET'S START ", name_of_player)

score=0

question1=input('WHAT IS DNA STANDs FOR? \n')
if question1.lower()=='deoxyribonucleic acid':
    print("CORRECT")
    score+=1
else:
    print("WRONG")

question2=input('WHAT IS RNA STANDs FOR? \n')
if question2.lower()=='ribonucleic acid':
    print("CORRECT")
    score+=1
else:
    print("WRONG")
    
question3=input('WHAT IS GMOs STANDs FOR? \n')
if question3.lower()=='genetically modified organisms':
    print("CORRECT")
    score+=1
else:
    print("WRONG")
    
question4=input('SCIENTIFIC NAME OF WHEAT? \n')
if question4.lower()=='triticum aestivum':
    print("CORRECT")
    score+=1
else:
    print("WRONG")

question5=input('WHAT IS PCR STANDS for? \n')
if question5.lower()=='polymerase chain reaction':
    print("CORRECT")
    score+=1
else:
    print("WRONG")
    
print("You got the " + str(score) + "correct answers")
print("YOUR SCORE PERCENTAGE is:",(score / 5) * 100, '%')

if score==5:
  print("Hurrah, You got all right.You will get a 'CASHBACK' of 50 rupees")
else:
  print("Sorry,BETTER LUCK NEXT TIME")
    