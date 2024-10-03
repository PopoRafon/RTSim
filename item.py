import xml.etree.ElementTree as ET

class Item:
    def __init__(self, id):
        self.id = id
        self.reiDamage = 0
        self.physDamage = 0
        self.bonusHealth = 0
        self.pvpProt = 0
        self.pvpModif = 0
        self.critChance = 0
        self.critStrike = 0
        self.castSpeed = 0
        self.attackSpeed = 0

        tree = ET.parse("items.xml")
        root = tree.getroot()

        xml_element = root.find(f"./item[@id='{self.id}']")
        if xml_element is not None:
            for attribute in xml_element.findall('attribute'):
                key = attribute.get('key')
                value = attribute.get('value')

                try:
                    int_value = int(value)
                except ValueError:
                    continue

                match(key):
                    case 'maxhitpoints':
                        self.bonusHealth = int_value
                    case 'boostpercentfire':
                        self.reiDamage = int_value
                    case 'pvemodifier':
                        self.pvpModif = int_value
                    case 'absorbpercentplayer':
                        self.pvpProt = int_value
                    case 'boostpercentphysical':
                        self.physDamage = int_value
                    case 'skillFist':
                        self.critChance = int_value
                    case 'skillDist':
                        self.critStrike = int_value
                    case 'skillAxe':
                        self.castSpeed = int_value
                    case 'skillClub':
                        self.attackSpeed = int_value
