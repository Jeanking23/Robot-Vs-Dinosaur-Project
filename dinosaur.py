from weapon import Weapon

class Dinosaur:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.active_weapon = Weapon("Dark Knight's Arm", "cheru-pattern" , 20 , 30)

