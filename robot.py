from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("laser","lethal autonomous", 30, 70)
        self.attack_power = 50
