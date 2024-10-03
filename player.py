import math
import random
import bisect

from item import Item

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.soulLevel = 1
        self.reiSkill = 0
        self.weaponSkill = 10
        self.health = 1000
        self.transform = 0
        self.weapon = 0
        self.helmet = None
        self.armor = None
        self.legs = None
        self.boots = None
        self.shield = None

    def getHealth(self):
        transformHealth = [2000, 6000, 16000, 36000, 66000, 106000, 166000, 206000, 266000, 346000, 446000, 566000]
        return self.health + (100 * (self.level - 1)) + transformHealth[self.transform]

    def setTransform(self, transform):
        if transform == "auto":
            transforms = [1, 50, 100, 150, 200, 400, 600, 800, 900, 1000, 1200, 1400, 1600]
            index = bisect.bisect_right(transforms, self.level + self.soulLevel) - 1

            if index < 0:
                return None
            elif index >= len(transforms):
                index = len(transforms) - 1

            self.transform = index
        else:
            self.transform = transform

    def setWeapon(self, weapon):
        self.weapon = weapon

    def setLevel(self, level, soulLevel):
        self.level = min(level, 801)
        self.soulLevel = soulLevel

    def setSkills(self, rei, weapon):
        self.reiSkill = rei
        self.weaponSkill = weapon

    def setEquipement(self, helmetId, armorId, legsId, bootsId, shieldId):
        self.helmet = Item(helmetId)
        self.armor = Item(armorId)
        self.legs = Item(legsId)
        self.boots = Item(bootsId)
        self.shield = Item(shieldId)

    def getCriticalChanceValue(self):
        itemBonus = 0
        if self.helmet:
            itemBonus += self.helmet.critChance
        if self.armor:
            itemBonus += self.armor.critChance
        if self.legs:
            itemBonus += self.legs.critChance
        if self.boots:
            itemBonus += self.boots.critChance
        if self.shield:
            itemBonus += self.shield.critChance

        return itemBonus

    def getCriticalStrikeValue(self):
        return 50

    def getMaxWeaponDamage(self):
        weaponTable = [10, 20, 40, 60, 90, 150, 200, 280, 300]
        attackValue = weaponTable[self.weapon]
        return int(round((attackValue * 3 + self.weaponSkill + self.level / 2) * 3 +
                         ((self.level * 3 + self.soulLevel * 3) / 7.0) *
                         (1.0 + (attackValue / 100.0)) *
                         (math.pow(2.0, (self.weaponSkill - 10) / 48.0))))

    def getWeaponDamage(self):
        maxValue = self.getMaxWeaponDamage()
        if random.randint(0, 100) < self.getCriticalChanceValue():
            print("CRITICAL!")
            maxValue = maxValue * (1 + (self.getCriticalStrikeValue() / 100))

        return random.randint(int(maxValue * 0.75), int(maxValue))

    def getMeleeDamage(self):
        transformMultip = [1.0, 1.05, 1.1, 1.15, 1.21, 1.27, 1.34, 1.4, 1.47, 1.55, 1.62, 1.71, 1.79]
        weaponValue = self.getWeaponDamage()
        itemBonus = 0
        if self.helmet:
            itemBonus += self.helmet.physDamage
        if self.armor:
            itemBonus += self.armor.physDamage
        if self.legs:
            itemBonus += self.legs.physDamage
        if self.boots:
            itemBonus += self.boots.physDamage
        if self.shield:
            itemBonus += self.shield.physDamage

        return int(weaponValue * transformMultip[self.transform] * (1 + itemBonus / 1000))

    def getSpellDamage(self):
        baseSpellDamage = {
            5: {'damage': 80},
            25: {'damage': 200},
            40: {'damage': 400},
            80: {'damage': 800},
            120: {'damage': 1000},
            300: {'damage': 1200},
            320: {'damage': 1600},
            500: {'damage': 2400},
            600: {'damage': 3600},
            800: {'damage': 4000},
            1200: {'damage': 6500}
        }

        base_damage = 0

        for required_level in sorted(baseSpellDamage.keys()):
            if required_level <= self.level + self.soulLevel:
                base_damage = baseSpellDamage[required_level]['damage']
            else:
                break

        base = (base_damage + (self.level * 2) + (1200 * (math.pow(1.1, self.soulLevel / 100)) - 1200)) * (
            math.pow(2, (self.reiSkill / 65)))

        min_damage = base * 0.8
        max_damage = base

        transformMultip = [1.0, 1.05, 1.1, 1.15, 1.21, 1.27, 1.34, 1.4, 1.47, 1.55, 1.62, 1.71, 1.79]
        min_damage *= transformMultip[self.transform]
        max_damage *= transformMultip[self.transform]

        return random.randint(int(min_damage), int(max_damage))
