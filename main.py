from player import Player


if __name__ == '__main__':
    gracz = Player("Mlodziutki")

    gracz.setLevel(50, 0)
    gracz.setTransform("auto")
    gracz.setWeapon(2)
    gracz.setSkills(80, 80)

    print(gracz.getMeleeDamage())
    print(gracz.getSpellDamage())
