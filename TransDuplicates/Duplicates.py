import csv

x = []
# reader = csv.reader(open('duplicates.csv', 'r'))
with open('duplicates.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        x.append(row)

trans_list = []
header = x[0]
print header
x = x[1:]
for i in x:
    trans_list.append(dict(zip(header, i)))

print len(trans_list)

el = []
for i in trans_list:
    if i['DESCRIPTION'] == 'E&L INSURANCE':
        el.append(i)
print el[0], el[1]

print set(el[0]) ^ set(el[1])


def dict_compare(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    intersect_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o: (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
    same = set(o for o in intersect_keys if d1[o] == d2[o])
    return added, removed, modified, same


x = dict(a=1, b=2)
y = dict(a=2, b=2)
added, removed, modified, same = dict_compare(x, y)
