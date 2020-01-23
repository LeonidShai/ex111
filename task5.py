"""
ATTA
ACTA
AGCA
ACAA

"""
cons_str = str()
spis = ["ATTA", 'ACTA', 'AGCA', 'ACAA']  # исходный список

k = 0
while k < 4:
    sp_str = str()
    for i in spis:
        sp_str = sp_str + i[k]

    prom = {}
    for i in sp_str:
        if i not in prom:
            prom[i] = sp_str.count(i)

    buk = max(prom.values())
    for i in prom:
        if prom[i] == buk:
            cons_str = cons_str + i
    k += 1
print(cons_str)


