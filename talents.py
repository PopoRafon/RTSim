class Talents:
    def __init__(self):
        self.health = 0
        self.healthPerSoulLevel = 0
        self.healthPercent = 0
        self.meleeDamage = 0
        self.reiatsuDamage = 0
        self.attackSpeed = 0
        self.castingSpeed = 0
        self.criticalStrikeChance = 0
        self.criticalStrikeDamage = 0
        self.totalDamage = 0
        self.playerProtection = 0

    def setTalents(self, talents):
        talentsLength = len(talents)

        if talentsLength >= 1:
            if talents[0] == 1:
                self.healthPercent += 8
            elif talents[0] == 2:
                self.meleeDamage += 4
            elif talents[0] == 3:
                self.reiatsuDamage += 4

        if talentsLength >= 2:
            if talents[1] == 1:
                self.attackSpeed += 8
            elif talents[1] == 2:
                self.criticalStrikeChance += 15
            elif talents[1] == 3:
                self.castingSpeed += 15

        if talentsLength >= 3:
            if talents[2] == 1:
                self.healthPercent += 16
            elif talents[2] == 2:
                self.meleeDamage += 32
            elif talents[2] == 3:
                self.reiatsuDamage += 32

        if talentsLength >= 4:
            if talents[3] == 1:
                self.meleeDamage += 10
            elif talents[3] == 2:
                self.reiatsuDamage += 10

        if talentsLength >= 5:
            if talents[4] == 2:
                self.playerProtection += 3
            elif talents[4] == 3:
                self.healthPerSoulLevel += 150

        if talentsLength >= 6:
            if talents[5] == 1:
                self.meleeDamage += 15
            elif talents[5] == 2:
                self.reiatsuDamage += 15

        if talentsLength >= 7:
            if talents[6] == 1:
                self.criticalStrikeChance += 15
            elif talents[6] == 2:
                self.castingSpeed += 15
            elif talents[6] == 3:
                self.attackSpeed += 8

        if talentsLength >= 8:
            if talents[7] == 1:
                self.criticalStrikeDamage += 15
            elif talents[7] == 3:
                self.totalDamage += 8

        if talentsLength >= 9:
            if talents[8] == 2:
                self.playerProtection += 4
            elif talents[8] == 3:
                self.health += 100000

        if talentsLength >= 10:
            if talents[9] == 1:
                self.meleeDamage += 40
            elif talents[9] == 2:
                self.reiatsuDamage += 40
