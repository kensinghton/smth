file_selected_1 = './wsp-1a.stat'
file_selected_2 = './com-2d.stat'
print(file_selected_1)
print(file_selected_2)


class Attacker(object):
    chassis = None
    mass = None
    move = None
    isjump = None
    heat = None
    armourhead = None
    armourtorso = None
    armourarms = None
    armourlegs = None
    punchkick = None
    weapons = None
    weapon1 = weapons
    weapon1.range = weapons
    weapon1.range.pointblank = None
    weapon1.range.short = None
    weapon1.range.medium = None
    weapon1.range.long = None
    weapon1.damage = None
    weapon2 = None
    weapon3 = None
    weapon4 = None
    weapon5 = None
    weapon6 = None
    def __init__(self, chassis, mass, move, isjump, heat, armorhead, armortorso, armorarms, armorlegs, punchkick,
                 weapons, weapon1, weapon2, weapon3, weapon4, weapon5, weapon6):
        self.chassis = None
        self.mass = None
        self.move = None
        self.isjump = None
        self.heat = None
        self.armourhead = None
        self.armourtorso = None
        self.armourarms = None
        self.armourlegs = None
        self.punchkick = None
        self.weapons = None
        self.weapon1 = weapon1
        self.weapon1.range = None
        self.weapon1.range.pointblank = None
        self.weapon1.range.short = None
        self.weapon1.range.medium = None
        self.weapon1.range.long = None
        self.weapon1.damage = None
        self.weapon1.heat = None
        self.weapon2 = weapon2
        self.weapon2.range = None
        self.weapon2.range.pointblank = None
        self.weapon2.range.short = None
        self.weapon2.range.medium = None
        self.weapon2.range.long = None
        self.weapon2.damage = None
        self.weapon2.heat = None
        self.weapon3 = weapon3
        self.weapon3.range = None
        self.weapon3.range.pointblank = None
        self.weapon3.range.short = None
        self.weapon3.range.medium = None
        self.weapon3.range.long = None
        self.weapon3.damage = None
        self.weapon3.heat = None
        self.weapon4 = weapon4
        self.weapon4.range = None
        self.weapon4.range.pointblank = None
        self.weapon4.range.short = None
        self.weapon4.range.medium = None
        self.weapon4.range.long = None
        self.weapon4.damage = None
        self.weapon4.heat = None
        self.weapon5 = weapon5
        self.weapon5.range = None
        self.weapon5.range.pointblank = None
        self.weapon5.range.short = None
        self.weapon5.range.medium = None
        self.weapon5.range.long = None
        self.weapon5.damage = None
        self.weapon5.heat = None
        self.weapon6 = weapon6
        self.weapon6.range = None
        self.weapon6.range.pointblank = None
        self.weapon6.range.short = None
        self.weapon6.range.medium = None
        self.weapon6.range.long = None
        self.weapon6.damage = None
        self.weapon6.heat = None


class Defender(object):
    def __init__(self, chassis, mass, move, isjump, heat, armorhead, armortorso, armorarms, armorlegs, punchkick,
                 weapons, weapon1, weapon2, weapon3, weapon4, weapon5, weapon6):
        self.chassis = None
        self.mass = None
        self.move = None
        self.isjump = None
        self.heat = None
        self.armourhead = None
        self.armourtorso = None
        self.armourarms = None
        self.armourlegs = None
        self.punchkick = None
        self.weapons = None
        self.weapon1 = weapon1
        self.weapon1.range = None
        self.weapon1.range.pointblank = None
        self.weapon1.range.short = None
        self.weapon1.range.medium = None
        self.weapon1.range.long = None
        self.weapon1.damage = None
        self.weapon1.heat = None
        self.weapon2 = weapon2
        self.weapon2.range = None
        self.weapon2.range.pointblank = None
        self.weapon2.range.short = None
        self.weapon2.range.medium = None
        self.weapon2.range.long = None
        self.weapon2.damage = None
        self.weapon2.heat = None
        self.weapon3 = weapon3
        self.weapon3.range = None
        self.weapon3.range.pointblank = None
        self.weapon3.range.short = None
        self.weapon3.range.medium = None
        self.weapon3.range.long = None
        self.weapon3.damage = None
        self.weapon3.heat = None
        self.weapon4 = weapon4
        self.weapon4.range = None
        self.weapon4.range.pointblank = None
        self.weapon4.range.short = None
        self.weapon4.range.medium = None
        self.weapon4.range.long = None
        self.weapon4.damage = None
        self.weapon4.heat = None
        self.weapon5 = weapon5
        self.weapon5.range = None
        self.weapon5.range.pointblank = None
        self.weapon5.range.short = None
        self.weapon5.range.medium = None
        self.weapon5.range.long = None
        self.weapon5.damage = None
        self.weapon5.heat = None
        self.weapon6 = weapon6
        self.weapon6.range = None
        self.weapon6.range.pointblank = None
        self.weapon6.range.short = None
        self.weapon6.range.medium = None
        self.weapon6.range.long = None
        self.weapon6.damage = None
        self.weapon6.heat = None


def load_sections(filename, side):
    with open(filename, 'r') as infile:
        for line in infile:
            if line.__contains__('='):
                line = line.strip()
                value = line.split('=', 1)[1]
                key = line.split('=', 1)[0]
                # print('line =', line)
                # print('value =', value)
                # print('key =', key)
                setattr(side, key, value)
                continue


file = open(file_selected_1, "r")
load_sections(file_selected_1, Attacker)
file.close()

file = open(file_selected_2, "r")
load_sections(file_selected_2, Defender)
file.close()

print(Attacker.weapon6)

# 6-25, 52, 60, (84-138), 154, (175-194), 195-234, 244
#
# base 1-244
# max 244-20-2-55-1-20-40-1 = 105
# accurate 244-20-2-1-40-1 = 180
