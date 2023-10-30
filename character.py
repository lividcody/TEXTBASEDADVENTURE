class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 10
        self.maxHealth = 10
        self.mana = 1
        self.maxMana = 1
        self.strength = 1
        self.defense = 1
        self.magic = 1
        self.magicDefense = 1
        self.exp = 0
        self.expNeeded = (10 * self.level)
        self.pClass = ''
        self.inventory = []
        self.variables = {
            "levelIntro":True
            }

    def __str__(self):
        stats = f'Name:\t  {self.name}'
        stats += f'\nClass:    {self.pClass}'
        stats += f'\nLevel:    {self.level}'
        stats += f'\nEXP:      {self.exp}/{self.expNeeded}'
        stats += '\n'
        stats += f'\nHealth:   {self.health}/{self.maxHealth}'  
        stats += f'\nMana:     {self.mana}/{self.maxMana}'
        stats += '\n'
        stats += f'\nStrength: {self.strength}'
        stats += f'\nMagic:    {self.magic}'
        stats += f'\nDefense:  {self.defense}'
        stats += f'\nMag Def:  {self.magicDefense}'
        stats += '\n'
        stats += f'\nInventory'
        inv_count = len(self.inventory)
        if inv_count > 0:
            for x in self.inventory:
                stats += "\n\t\t" + f'{x}'
        else:
            stats += "\n\tEmpty"
        return stats

    def hurt(self,damage):
        self.health - damage
    
    def heal(self,amount):
        self.health + amount