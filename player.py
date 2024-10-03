import math
import random
import bisect

from item import Item

class Transform:
    def __init__(self, level, multi, health):
        self.level = level
        self.multi = multi
        self.health = health

class Player:
    transforms = [
        Transform(1, 1.0, 0),
        Transform(50, 1.05, 2000),
        Transform(100, 1.1, 6000),
        Transform(150, 1.15, 16000),
        Transform(200, 1.21, 36000),
        Transform(400, 1.27, 66000),
        Transform(600, 1.34, 106000),
        Transform(800, 1.4, 166000),
        Transform(900, 1.47, 206000),
        Transform(1000, 1.55, 266000),
        Transform(1200, 1.62, 346000),
        Transform(1400, 1.71, 446000),
        Transform(1600, 1.79, 566000)
    ]
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

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.soulLevel = 1
        self.reiSkill = 0
        self.weaponSkill = 10
        self.health = 1000
        self.transform = 0
        self.weapon = 0
        self.equipment: dict[str, None | Item] = {
            'helmet': None,
            'armor': None,
            'legs': None,
            'boots': None,
            'shield': None
        }

    def getHealth(self):
        return self.health + (100 * (self.level - 1)) + self.transforms[self.transform].health

    def setTransform(self, transform):
        if transform == "auto":
            index = bisect.bisect_right([transform.level for transform in self.transforms], self.level + self.soulLevel) - 1

            if index < 0:
                return None
            elif index >= len(self.transforms):
                index = len(self.transforms) - 1

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

    def setEquipment(self, equipmentIds: dict[str, None | int]={}):
        for key in equipmentIds:
            if key in self.equipment.keys():
                assert isinstance(equipmentIds[key], int), 'Equipment id must be an integer'
                self.equipment[key] = Item(equipmentIds[key])

    def getCriticalChanceValue(self):
        itemBonus = 0

        for piece in self.equipment.values():
            if isinstance(piece, Item):
                itemBonus += piece.critChance

        return itemBonus

    def getCriticalStrikeValue(self):
        itemBonus = 50

        for piece in self.equipment.values():
            if isinstance(piece, Item):
                itemBonus += piece.critStrike

        return itemBonus

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
        weaponValue = self.getWeaponDamage()
        itemBonus = 0

        for piece in self.equipment.values():
            if isinstance(piece, Item):
                itemBonus += piece.physDamage

        return int(weaponValue * self.transforms[self.transform].multi * (1 + itemBonus / 1000))

    def getSpellDamage(self):
        base_damage = 0

        for required_level in sorted(self.baseSpellDamage.keys()):
            if required_level <= self.level + self.soulLevel:
                base_damage = self.baseSpellDamage[required_level]['damage']
            else:
                break

        base = (base_damage + (self.level * 2) + (1200 * (math.pow(1.1, self.soulLevel / 100)) - 1200)) * (
            math.pow(2, (self.reiSkill / 65)))

        min_damage = base * 0.8
        max_damage = base

        min_damage *= self.transforms[self.transform].multi
        max_damage *= self.transforms[self.transform].multi

        return random.randint(int(min_damage), int(max_damage))

    def setTalents(self):
        raise Exception('Not Implemented')

    def setSoulTalents(self):
        raise Exception('Not Implemented')
