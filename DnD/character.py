
class CharacterDescription: 
    def __init__(self, Class, STR, CON, DEX, INT, WIS, CHA, HP, AC, SF): 
        self.Class = Class 
        self.STR = STR
        self.CON = CON
        self.DEX = DEX
        self.INT = INT
        self.WIS = WIS
        self.CHA = CHA 
        self.HP = HP
        self.AC = AC
        self.SF = SF

    def __str__(self):
        return (
            f"Class: {self.Class}, STR: {self.STR}, CON: {self.CON}, "
            f"DEX: {self.DEX}, INT: {self.INT}, WIS: {self.WIS}, CHA: {self.CHA}, HP:{self.HP}"
        )
    
    @classmethod
    def select(cls, attributes):
        if len(attributes) != 10:
            raise ValueError("List must contain exactly 10 elements.")
        return cls(
            Class=attributes[0],
            STR=attributes[1],
            CON=attributes[2],
            DEX=attributes[3],
            INT=attributes[4],
            WIS=attributes[5],
            CHA=attributes[6],
            HP=attributes[7],
            AC=attributes[8],
            SF=attributes[9]
        )
    

    def has_attribute(self, attribute_name):
      return hasattr(self, attribute_name)
    

    def getStat(self, stat):
      return getattr(self, stat)


    def addStats(self, attribute_name, number):
        if self.has_attribute(attribute_name):
            current_value = getattr(self, attribute_name)          #gets the current values

            setattr(self, attribute_name, current_value + number)  #add number to current value
            return getattr(self, attribute_name)
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attribute_name}'")


    def subStats(self, attribute_name, number):
        if self.has_attribute(attribute_name):
            current_value = getattr(self, attribute_name)          #gets the current value

            setattr(self, attribute_name, current_value - number)  #add number to current value
            return getattr(self, attribute_name)
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attribute_name}'")


    def highestStat(self):
        stats = {
            "STR": self.STR,
            "CON": self.CON,
            "DEX": self.DEX,
            "INT": self.INT,
            "WIS": self.WIS,
            "CHA": self.CHA
        }
        highest_stat_name = max(stats, key=stats.get)
        highest_stat_value = stats[highest_stat_name]
        
        return highest_stat_name, highest_stat_value
    
    """
    def calculateAC(self):
        className = getattr(self.Class)
        if className == "Warrior":
    """
    
    