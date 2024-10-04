from typing import Literal
import math
import random
import bisect

from transforms import transforms
from talents import Talents
from item import Item

class Player:
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
        self.talents = Talents()
        self.equipment: dict[str, None | Item] = {
            'helmet': None,
            'armor': None,
            'legs': None,
            'boots': None,
            'shield': None
        }

    def getHealth(self):
        baseHealth = self.health + (100 * (self.level - 1)) + transforms[self.transform].health
        talentsBonusHealth = self.talents.health + (self.soulLevel * self.talents.healthPerSoulLevel) + (baseHealth * (self.talents.healthPercent / 100))

        return baseHealth + talentsBonusHealth

    def setTransform(self, transform):
        if transform == "auto":
            index = bisect.bisect_right([transform.level for transform in transforms], self.level + self.soulLevel) - 1

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

    def setEquipment(self, equipmentIds: dict[Literal['helmet', 'armor', 'legs', 'boots', 'shield'], None | int]={}):
        for key in equipmentIds:
            if key in self.equipment.keys():
                assert isinstance(equipmentIds[key], int), 'Equipment id must be an integer'
                self.equipment[key] = Item(equipmentIds[key])

    def getCriticalChanceValue(self):
        itemBonus = 0

        for piece in self.equipment.values():
            if isinstance(piece, Item):
                itemBonus += piece.critChance

        itemBonus += self.talents.criticalStrikeChance

        return itemBonus

    def getCriticalStrikeValue(self):
        itemBonus = 50

        for piece in self.equipment.values():
            if isinstance(piece, Item):
                itemBonus += piece.critStrike

        itemBonus += self.talents.criticalStrikeDamage

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
            maxValue = maxValue * (1 + (self.getCriticalStrikeValue() / 100))

        return random.randint(int(maxValue * 0.75), int(maxValue))

    def getMeleeDamage(self):
        weaponValue = self.getWeaponDamage()
        itemBonus = sum([piece.physDamage if isinstance(piece, Item) else 0 for piece in self.equipment.values()])
        itemBonus += self.talents.meleeDamage * 10
        talentsTotalDamageMulti = 1 + (self.talents.totalDamage / 100)

        return int((weaponValue * transforms[self.transform].multi * (1 + itemBonus / 1000)) * talentsTotalDamageMulti)

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

        min_damage *= transforms[self.transform].multi
        max_damage *= transforms[self.transform].multi

        itemBonus = sum([piece.reiDamage if isinstance(piece, Item) else 0 for piece in self.equipment.values()])
        itemBonus += self.talents.reiatsuDamage * 10
        talentsTotalDamageMulti = 1 + (self.talents.totalDamage / 100)

        return int((random.randint(int(min_damage), int(max_damage)) * (1 + itemBonus / 1000)) * talentsTotalDamageMulti)

    def getAttackSpeed(self):
        baseAttackSpeed = 2000
        attackSpeedReduction = 1000
        itemsAttackSpeed = sum([piece.attackSpeed if isinstance(piece, Item) else 0 for piece in self.equipment.values()])
        talentsBonusAttackSpeed = 1 + (self.talents.attackSpeed / 100)
        totalAttackSpeed = (attackSpeedReduction / round(baseAttackSpeed - itemsAttackSpeed)) * talentsBonusAttackSpeed

        return totalAttackSpeed

    def getSpellCooldown(self):
        baseSpellCooldown = 2
        itemsCastSpeed = sum([piece.castSpeed if isinstance(piece, Item) else 0 for piece in self.equipment.values()])
        castingReduction = 1 + ((itemsCastSpeed + self.talents.castingSpeed) / 100)
        totalSpellCooldown = baseSpellCooldown / castingReduction

        return totalSpellCooldown

    def calculateDamagePerSecond(self, time):
        totalMeleeDamage = sum([self.getMeleeDamage() for _ in range(math.floor(self.getAttackSpeed() * time))])
        totalSpellDamage = sum([self.getSpellDamage() for _ in range(math.floor(time / self.getSpellCooldown()))])
        damagePerSecond = totalMeleeDamage + totalSpellDamage

        return round(damagePerSecond / time)

    def setTalents(self, talents: list[Literal[1, 2, 3]]=[]):
        """
            8% max hp and 4% healing, 4% melee damage, 4% reiatsu damage\n
            8% attack speed, 15% critical strike chance, 15% casting speed\n
            16% max hp and 8% healing, 32% melee damage, 32% reiatsu damage\n
            10% physical damage, 10% reiatsu damage, 4% healing\n
            4% armor value, 3% player protection, 150 hp per slvl\n
            15% physical damage, 15% reiatsu damage, 8% healing\n
            15% critical strike chance, 15% casting speed, 8% attack speed\n
            15% critical damage, 25% dot damage, 8% total damage\n
            6% armor value, 4% player prot, 100k hp\n
            40% physical damage, 40% reiatsu damage, 16% healing\n
        """
        self.talents = Talents()
        self.talents.setTalents(talents)
