
from Stats import enemyDict
import random
import math

#lvl of dif on mob is not based on your lvl but per round
def lvlDif(foeName, foeAC, foeHP, foeAP, turn):
      level = math.floor((foeAC + foeHP + foeAP) / 10)
      while level/3 >= turn:
        foeName, foeAC, foeHP, foeAP = foeGenerator()
        level = math.floor((foeAC + foeHP + foeAP) / 10)
      return foeName, foeAC, foeHP, foeAP

def foeGenerator():
      randomEnemy = random.randint(0, len(enemyDict) - 1)
      names_of_Enemies = list(enemyDict.keys())
      foeKey = names_of_Enemies[randomEnemy]

      # Example: goblinStats": {"Type": "Goblin", "AC": 15, "hp": ...}
      foeStats = enemyDict[foeKey]
      foeName = foeStats['Type']
      foeAC = foeStats['AC']
      foeHP = foeStats['HP']
      foeAP = foeStats['AP']

      return foeName, foeAC, foeHP, foeAP


class Enemy: 
    def __init__(self, foeName, AC, HP, AP): 
        self.foeName = foeName
        self.AC = AC
        self.HP = HP
        self.AP = AP
    
    def __str__(self):
        return f"You have encountered a -{self.foeName}- with Armor Class of [{self.AC}] and HP of [{self.HP}]."
    

    def has_attribute(self, attribute_name):
      return hasattr(self, attribute_name)


    def getStat(self, stat):
        return getattr(self, stat)

    def subStats(self, attribute_name, number):
        if self.has_attribute(attribute_name):
            current_value = getattr(self, attribute_name)          #gets the current value

            setattr(self, attribute_name, current_value - number)  #add number to current value
            return getattr(self, attribute_name)
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attribute_name}'")

   
         
        