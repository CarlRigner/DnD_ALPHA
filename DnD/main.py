import random
import time
import math
from character import CharacterDescription
from enemies import Enemy, lvlDif, foeGenerator
from Stats import enemyDict, classDict


dice = 0
turnCounter = 0

def modifier(value):
   modifier = int(( value - 10) /2)
   return modifier


#ClassSelection
User = input("\n Choose a class: ")
classDict = classDict[f"{User.lower()}Stats"]
classSelected = list(classDict.values())
characterMem = CharacterDescription.select(classSelected)
time.sleep(0.6)

print("________________________________________________________\n")
print(f"you have chosen: {characterMem} \n")
print("________________________________________________________\n")

#initate encounters loop
while True:
    turnCounter += 1
    time.sleep(1)

    #GENERATE FOE/ENEMY HERE
    #____________________________________________#
  
    foeName, foeAC, foeHP, foeAP = foeGenerator()
    foeName, foeAC, foeHP, foeAP = lvlDif(foeName, foeAC, foeHP, foeAP, turnCounter)
    foe = Enemy(foeName, foeAC, foeHP, foeAP)
   
    #____________________________________________#
    print(f"{foe}\n") 
    time.sleep(1)


   
    #First check if player want to roll dice
    UserAccept = input("type 'r' to roll: ").lower()
    if UserAccept != "r".lower():
        raise ValueError("Is it so hard to roll a dice?")
    

    #Loop for current battle
    #____________________________________________________________________________________________________________________________________#
    while UserAccept == "r":
     
     #Player's turn
     #_________________________________________________________________________#
     #_________________________________________________________________________#
     
     dice = random.randint(1, 20)

     print("____________________________________________________\n")
     print(f"\n you rolled {dice}\n")
 
     highest_stat_name, highest_stat_value = characterMem.highestStat()
    
     bonusScore = modifier(highest_stat_value)
     totalScore = dice + bonusScore
     print(f"\n Total attack power of {totalScore}\n")
     print("____________________________________________________\n")
     time.sleep(2)

     if totalScore >= foe.getStat("AC"):
       print(f"\n successful hit! \n")
       foe.subStats("HP", totalScore)
       time.sleep(1)

       if foe.HP <= 0:
          print("____________________________________________________\n")
          print(f"a {foe.foeName} has been slayed! \n")
          print("____________________________________________________\n")
          break 
       
       else:
         print("____________________________________________________\n")
         print(f"{foe.foeName} has {foe.HP}HP left \n")
         print("____________________________________________________\n")
     else:
       print(f"\n you missed! \n")
     time.sleep(1)
      

     #Foe's turn
     #__________________________________________________________________________#
     #__________________________________________________________________________#
     




     #Sec check if player want to roll dice
     UserAccept = input("type 'r' to roll: ").lower()
     time.sleep(0.5)
     if UserAccept != "r".lower():
       raise ValueError("stopped rolling, why?")
     
  #end for current battle
    #_____________________________________________________________________________________________________________________________________#

    
    
   

    #Stat adder 
    attriubute = "DEX"
    number = 2 
    new_value = characterMem.addStats(attriubute, number)
    
    

