class Sets:
    itemIdToSet = {
        13100: 1,  # HIYORI MASK
        12350: 1,  # HIYORI JACKET
        13240: 1,  # HIYORI LEGS
        13238: 1,  # HIYORI TRAINERS
        13252: 1,  # UBER HIYORI MASK
        13253: 1,  # UBER HIYORI JACKET
        13254: 1,  # UBER HIYORI LEGS
        13255: 1,  # UBER HIYORI TRAINERS

        12348: 2,  # URAHARA HAT
        12417: 2,  # URAHARA JACKET
        13093: 2,  # URAHARA LEGS
        10594: 2,  # URAHARA SANDALS
        13244: 2,  # UBER URAHARA HAT
        13245: 2,  # UBER URAHARA JACKET
        13246: 2,  # UBER URAHARA LEGS
        13247: 2,  # UBER URAHARA SANDALS

        12349: 3,  # YAMMY MASK
        12363: 3,  # YAMMY ARMOR
        13767: 3,  # YAMMY LEGS
        13768: 3,  # YAMMY BOOTS
        13250: 3,  # UBER YAMMY MASK
        13251: 3,  # UBER YAMMY ARMOR
        13795: 3,  # UBER YAMMY
        13796: 3,  # UBER YAMMY

        10683: 4,  # AS
        10667: 4,  # AS
        13204: 4,  # AS
        10674: 4,  # AS
        13275: 4,  # UBER AS
        13276: 4,  # UBER AS
        13277: 4,  # UBER AS
        13278: 4,  # UBER AS

        2461: 5,  # CRIT
        12365: 5,  # CRIT
        13763: 5,  # CRIT
        13764: 5,  # CRIT
        13248: 5,  # UBER CRIT
        13249: 5,  # UBER CRIT
        13791: 5,  # UBER CRIT
        13792: 5,  # UBER CRIT

        13199: 6,  # CAST SPEED
        13200: 6,  # CAST SPEED
        13201: 6,  # CAST SPEED
        13202: 6,  # CAST SPEED
        13264: 6,  # UBER CAST SPEED
        13265: 6,  # UBER CAST SPEED
        13266: 6,  # UBER CAST SPEED
        13267: 6,  # UBER CAST SPEED

        13236: 7,  # MELEE PVP 1
        12426: 7,  # MELEE PVP 1
        13774: 7,  # MELEE PVP 1
        13775: 7,  # MELEE PVP 1
        13273: 7,  # UBER MELEE PVP 1
        13272: 7,  # UBER MELEE PVP 1
        13803: 7,  # UBER MELEE PVP 1
        13804: 7,  # UBER MELEE PVP 1

        12984: 8,  # REIATSU PVP 2
        12985: 8,  # REIATSU PVP 2
        13783: 8,  # REIATSU PVP 2
        13784: 8,  # REIATSU PVP 2
        13291: 8,  # UBER REIATSU PVP 2
        13292: 8,  # UBER REIATSU PVP 2
        13811: 8,  # UBER REIATSU PVP 2
        13812: 8,  # UBER REIATSU PVP 2

        13103: 9,  # STARRK
        12364: 9,  # STARRK
        12421: 9,  # STARRK
        13769: 9,  # STARRK
        13258: 9,  # UBER STARRK
        13259: 9,  # UBER STARRK
        13797: 9,  # UBER STARRK
        13798: 9,  # UBER STARRK

        13195: 10,  # NNOITRA
        12452: 10,  # NNOITRA
        12424: 10,  # NNOITRA
        13198: 10,  # NNOITRA
        13260: 10,  # UBER NNOITRA
        13261: 10,  # UBER NNOITRA
        13262: 10,  # UBER NNOITRA
        13263: 10,  # UBER NNOITRA

        12420: 11,  # BARRAGAN WAVE
        13111: 11,  # BARRAGAN WAVE
        13787: 11,  # BARRAGAN WAVE
        13785: 11,  # BARRAGAN WAVE
        13256: 11,  # UBER BARRAGAN WAVE
        13257: 11,  # UBER BARRAGAN WAVE
        13813: 11,  # UBER BARRAGAN WAVE
        13786: 11,  # UBER BARRAGAN WAVE

        13770: 12,  # FULLBRINGER PROT
        13771: 12,  # FULLBRINGER PROT
        13098: 12,  # FULLBRINGER PROT
        13099: 12,  # FULLBRINGER PROT
        13269: 12,  # UBER FULLBRINGER PROT
        13270: 12,  # UBER FULLBRINGER PROT
        13799: 12,  # UBER FULLBRINGER PROT
        13800: 12,  # UBER FULLBRINGER PROT

        12434: 13,  # BLIND
        12451: 13,  # BLIND
        13776: 13,  # BLIND
        13777: 13,  # BLIND
        13714: 13,  # UBER BLIND
        13281: 13,  # UBER BLIND
        13805: 13,  # UBER BLIND
        13806: 13,  # UBER BLIND

        13781: 14,  # YAMAMOTO
        2528: 14,  # YAMAMOTO
        10709: 14,  # YAMAMOTO
        13782: 14,  # YAMAMOTO
        13287: 14,  # UBER YAMAMOTO
        13288: 14,  # UBER YAMAMOTO
        13809: 14,  # UBER YAMAMOTO
        13810: 14,  # UBER YAMAMOTO

        13814: 15,  # MELEE PVP 2
        13815: 15,  # MELEE PVP 2
        10733: 15,  # MELEE PVP 2
        12454: 15,  # MELEE PVP 2
        13289: 15,  # UBER MELEE PVP 2
        13290: 15,  # UBER MELEE PVP 2
        13793: 15,  # UBER MELEE PVP 2
        13794: 15,  # UBER MELEE PVP 2

        12788: 16,  # REIATSU PVP 1
        13237: 16,  # REIATSU PVP 1
        13110: 16,  # REIATSU PVP 1
        12983: 16,  # REIATSU PVP 1
        13271: 16,  # UBER REIATSU PVP 1
        13274: 16,  # UBER REIATSU PVP 1
        13801: 16,  # UBER REIATSU PVP 1
        13802: 16,  # UBER REIATSU PVP 1

        13239: 17,  # AIZEN
        13778: 17,  # AIZEN
        13779: 17,  # AIZEN
        13780: 17,  # AIZEN
        13282: 17,  # UBER AIZEN
        13283: 17,  # UBER AIZEN
        13807: 17,  # UBER AIZEN
        13808: 17,  # UBER AIZEN

        13233: 18,  # GRAND FISHER MASK
        13234: 18,  # GRAND FISHER MASK (USED)
        13242: 18,  # UBER GRAND FISHER MASK
        13243: 18,  # UBER GRAND FISHER MASK (USED)

        13749: 19,  # YHWACH
        13750: 19,  # YHWACH
        13751: 19,  # YHWACH
        13752: 19,  # YHWACH
        13753: 19,  # UBER YHWACH
        13754: 19,  # UBER YHWACH
        13755: 19,  # UBER YHWACH
        13756: 19,  # UBER YHWACH

        14026: 20,  # HARRIBEL
        14027: 20,  # HARRIBEL
        14028: 20,  # HARRIBEL
        14029: 20,  # HARRIBEL
        14030: 20,  # UBER HARRIBEL
        14031: 20,  # UBER HARRIBEL
        14032: 20,  # UBER HARRIBEL
        14033: 20,  # UBER HARRIBEL
    }

    def __init__(self, equipment):
        self.equipment = equipment

    def getSetBonus(self, setId):
        setBonus = 0
        for item in self.equipment.values():
            if item:
                item_id = item.id
                print(f"item_id: {item_id}")
                if item_id in self.itemIdToSet and self.itemIdToSet[item_id] == setId:
                    setBonus += 1

        return setBonus