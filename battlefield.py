from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self ):
        self.robot = Robot("Robot BenMax")
        self.dinosaur = Dinosaur("Dinosaur tyrant", 100, 30)
        self.attack_power = 30, 20
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
    def display_welcome(self):
        print("Welcome to the epic battle between Robot and Dinosaur!")
        print("The Robot is named " + self.robot.name + "!")
        print("The Dinosaur is named " + self.dinosaur.name + "!")
        print("The Robot has " + str(self.robot.health) + " health!")
        print("The Dinosaur has " + str(self.dinosaur.health) +  " health!")
        print("The Robot uses " + str(self.robot.active_weapon.name) + " and " + str(self.robot.active_weapon.name2)+" weapon!")
        print("The Dinosaur uses " + str(self.dinosaur.active_weapon.name) + " and  "  + str(self.dinosaur.active_weapon.name2) + " weapon!")
        print("The Robot has " + str(self.robot.active_weapon.attact_power) + " attacting power!")
        print("The Dinosaur has " + str(self.dinosaur.active_weapon.attact_power) + " attacting power!")
        print("Only one side can win!")
        print(" ")
    def battle_phase(self):
        print(" ")
        print(self.robot.name + " attacks " + self.dinosaur.name + " with " + self.robot.active_weapon.name + " for " + str(self.robot.active_weapon.attact_power) + " attacting power!")
        while self.dinosaur.health == 100:
            self.dinosaur.health -= self.robot.active_weapon.attact_power
            print(f"{self.dinosaur.name} has {self.dinosaur.health} health left.")
        print(self.dinosaur.name + " attacks " + self.robot.name + " with a " + self.dinosaur.active_weapon.name + " for " + str(self.dinosaur.active_weapon.attact_power) + " attacting power!")
        while self.robot.health == 100:
            self.robot.health -= self.dinosaur.active_weapon.attact_power

            print(f"{self.robot.name} has {self.robot.health} health left.")


        print(" ")
        print(self.dinosaur.name + " attacks " + self.robot.name + " with a " + self.dinosaur.active_weapon.name + " for " + str(self.dinosaur.active_weapon.attact_power2) + " attacting power!")
        while self.robot.health == 80:
            self.robot.health -= self.dinosaur.active_weapon.attact_power2
            print(f"{self.robot.name} has {self.robot.health} health left.")

        print(self.robot.name + " attacks " + self.dinosaur.name + " with " + self.robot.active_weapon.name2 + " for " + str(self.robot.active_weapon.attact_power2) + " attacting power!")
        while self.dinosaur.health == 70:
            self.dinosaur.health -= self.robot.active_weapon.attact_power2
            print(f"{self.dinosaur.name} has {self.dinosaur.health} health left.")
    def display_winner(self):
        if self.robot.health > 0:
            print("The Robot has won!")
        elif self.dinosaur.health > 0:

            print("The Dinosaur has won!")
    
        else:
            print("The Robot has won!")
        print(" ")
        print("BenMax has " + str(self.robot.health) + " health left!")
        print("tyrant " + str(self.dinosaur.health) + " health left!")
