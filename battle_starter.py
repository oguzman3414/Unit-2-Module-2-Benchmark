"""
RPG Battle System - Starter Code
Fill in the TODOs to complete the classes benchmark.
"""


class Character:
    def __init__(self, name, health, attack_power):
        # TODO: store name, health (current), max_health, attack_power
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        # TODO: set self.weapon = None
        self.weapon = None

    def is_alive(self):
        # TODO: return True if health > 0
        return self.health > 0

    def take_damage(self, amount):
        # TODO: subtract amount from health, don't let it go below 0
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def attack(self, other):
        # TODO: deal self.attack_power damage to other, print a message
        other.take_damage(self.attack_power)
        print(f"{self.name} attacks {other.name} for {self.attack_power} damage!")

    def heal(self, amount):
        # TODO: increase health by amount, don't exceed max_health
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    def equip(self, weapon):
        # TODO: store the weapon, increase attack_power by weapon.bonus_damage,
        # print a message
        self.weapon = weapon
        self.attack_power += weapon.bonus_damage
        print(f"{self.name} equips {weapon.name}!")



class Weapon:
    def __init__(self, name, bonus_damage):
        # TODO: store name and bonus_damage
        self.name = name
        self.bonus_damage = bonus_damage


class Battle:
    def __init__(self, fighter_one, fighter_two):
        # TODO: store both fighters
        self.fighter_one = fighter_one
        self.fighter_two = fighter_two

    def run(self):
        # TODO: alternate turns (fighter_one attacks first),
        # stop when one fighter's is_alive() is False,
        # print the winner
        while self.fighter_one.is_alive() and self.fighter_two.is_alive():
            self.fighter_one.attack(self.fighter_two)
            if not self.fighter_two.is_alive():
                break
            self.fighter_two.attack(self.fighter_one)
        winner = self.fighter_one if self.fighter_one.is_alive() else self.fighter_two
        print(f"{winner.name} wins the battle!")    
        


if __name__ == "__main__":
    # TODO:
    # 1. Create two Character instances with different stats
    fighter_one = Character("Hero", 100, 25)
    fighter_two = Character("Villain", 125, 20)
    # 2. Create at least one Weapon and equip it to one character
    sword = Weapon("Sword", 10)
    fighter_one.equip(sword)
    # 3. Create a Battle with the two characters
    battle = Battle(fighter_one, fighter_two)
    # 4. Call .run()
    battle.run()
