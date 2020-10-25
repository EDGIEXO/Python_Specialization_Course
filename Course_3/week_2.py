name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_756539.txt"
handle = open(name)
import re
bi = list()

for hs in handle:
    st = hs.rstrip()
    nstr = re.findall('[0-9]+',st)
    if not len(nstr) >= 1 : continue
    for we in nstr:
        x = int(we)
        bi.append(x)
print(sum(bi)) 