from player import Player


if __name__ == '__main__':
    gracz = Player("Mlodziutki")

    gracz.setLevel(50, 0)
    gracz.setTransform("auto")
    gracz.setWeapon(2)
    gracz.setSkills(80, 80)

    totalDPS = gracz.calculateDamagePerSecond(60)

    print(f'Damage per second: {totalDPS}')
    print(f'Melee damage: {gracz.getMeleeDamage()}')
    print(f'Spell damage: {gracz.getSpellDamage()}')
