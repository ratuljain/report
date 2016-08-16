d = {}


def addStuff(d, k, v):
    if k in d:
        d[k].append(v)
    else:
        d[k] = []
        d[k].append(v)


addStuff(d, "ravi travels", "arv-10:30,dep-10:40")
addStuff(d, "ravi travels", "arv-09:30,dep-09:40")
addStuff(d, "ravi travels", "arv-11:30,dep-12:40")
addStuff(d, "kishore travels", "arv-09:30,dep-09:40")
addStuff(d, "kishore travels", "arv-09:30,dep-09:40")
# addStuff(d, 1, "a")
# addStuff(d, 1, "a")
# addStuff(d, 1, "a")
# addStuff(d, 1, "a")
# addStuff(d, 1, "a")

print d
# ravi travels: arv-10:00,dep-10:30
# ravi travels: arv-09:30,dep-09:40
# kishore travels: arv-09:30,dep-09:40
# kishore travels: arv-10:00,dep-10:30
