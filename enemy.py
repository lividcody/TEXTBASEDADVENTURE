class Enemy:
    def __init__(self,name,level,description,totalHealth,strength,magic,defense,magicDefense,weakness):
        self.name = name
        self.level = level
        self.description = description
        self.totalHealth = totalHealth
        self.strength = strength
        self.magic = magic
        self.defense = defense
        self.magicDefense = magicDefense
        self.weakness = weakness
        self.currentHealth = totalHealth
        self.experience = level

    def damage(amount):
        self.currentHealth -= amount