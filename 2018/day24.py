import re


class Group:
    def __init__(self, army, group_id, units, hp, specials, attack, attack_type, initiative):
        self.id = group_id
        self.units = units
        self.hp = hp
        self.specials = specials
        self.attack = attack
        self.attack_type = attack_type
        self.initiative = initiative
        self.army = army
        
        self.picked = False
        self.target = None
        self.damage = 0
        self.killed = 0
        self.mult = 0


def calc(values, boost):
    groups = []
    army = ""
    armies = {}
    
    r = re.compile("([0-9]+) units each with ([0-9]+) hit points (\\((.*)\\) |)with an attack that does ([0-9]+) (.*) "
                   "damage at initiative ([0-9]+)")
    
    for cur in values:
        if cur == "Immune System:":
            army = "immune"
            armies[army] = 1
        elif cur == "Infection:":
            army = "infection"
            armies[army] = 1
        elif len(cur) > 0:
            m = r.search(cur)
            if army == "immune":
                boost_army = boost
            else:
                boost_army = 0
            group = Group(army, armies[army], int(m.group(1)), int(m.group(2)), m.group(4),
                          int(m.group(5)) + boost_army, m.group(6), int(m.group(7)))
            armies[army] += 1
            groups.append(group)
    
    for cur in groups:
        if cur.specials is None:
            cur.specials = set()
        else:
            temp = cur.specials.split("; ")
            cur.specials = set()
            for temp_cur in temp:
                flavor = None
                for sub in temp_cur.split(", "):
                    if sub.startswith("weak to "):
                        flavor = "weak to "
                        cur.specials.add(sub)
                    elif sub.startswith("immune to "):
                        flavor = "immune to "
                        cur.specials.add(sub)
                    else:
                        cur.specials.add(flavor + sub)
    
    while True:
        for cur in groups:
            cur.picked = False
            cur.target = None
            cur.damage = 0
            cur.killed = 0
        
        groups.sort(key=lambda x: (x.units * x.attack, x.initiative), reverse=True)
        
        for cur in groups:
            best_option = None
            for sub in groups:
                if (not sub.picked) and (sub.units > 0):
                    if sub.army != cur.army:
                        mult = 1
                        if ("immune to " + cur.attack_type) in sub.specials:
                            mult = 0
                        if ("weak to " + cur.attack_type) in sub.specials:
                            mult = 2
                        
                        if mult > 0:
                            sub.damage = cur.attack * cur.units * mult
                            sub.mult = mult
                            if best_option is None:
                                best_option = sub
                            else:
                                if sub.damage > best_option.damage:
                                    best_option = sub
                                elif sub.damage == best_option.damage:
                                    if sub.units * sub.attack > best_option.units * best_option.attack:
                                        best_option = sub
                                    elif sub.units * sub.attack == best_option.units * best_option.attack:
                                        if sub.initiative > best_option.initiative:
                                            best_option = sub
            
            if best_option is not None:
                cur.target = best_option
                best_option.picked = True
        
        groups.sort(key=lambda x: (x.initiative,), reverse=True)
        
        did_damage = 0
        
        for cur in groups:
            if cur.units > 0:
                if cur.target is not None:
                    cur.target.damage = cur.attack * cur.units * cur.target.mult
                    cur.target.killed = cur.target.damage // cur.target.hp
                    if cur.target.killed > 0:
                        did_damage += 1
                    cur.target.units -= cur.target.damage // cur.target.hp
                    if cur.target.units <= 0:
                        armies[cur.army] -= 1
        
        if min(armies.values()) == 1:
            break
        
        if did_damage == 0:
            return 0, 'nobody'
    
    ret = 0
    for cur in groups:
        if cur.units > 0:
            ret += cur.units
            winning = cur.army
    
    return ret, winning


def part_one(inp):
    ret = calc(inp, 0)
    return ret[0]


def part_two(inp):
    boost = 1
    span = 64
    found = {}
    while True:
        if boost not in found:
            found[boost] = calc(inp, boost)
        if boost - 1 not in found:
            found[boost - 1] = calc(inp, boost - 1)
        
        if found[boost][1] == "immune":
            if found[boost - 1][1] != "immune":
                break
            span = span // 2
            boost = max(1, boost - span)
        else:
            boost += span
    
    return found[boost][0]


def main():
    with open(r'input\day24.txt') as fin:
        inp = fin.read().splitlines()
    
    print(part_one(inp))
    print(part_two(inp))
    
    
if __name__ == '__main__':
    main()
