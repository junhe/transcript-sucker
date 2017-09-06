import re
import codecs

prthd = open('./0to1words.txt')
# prthd = open('./Economist/over-200-times.txt')
gre = open('redbook.txt')
wdlst = list()
grewdslst = list()

for line in prthd:
    words = re.findall('[a-z]+',line)
    for word in words:
        wdlst.append(word)


for ln in gre:
    grewds = ln.split()[0]
    grewdslst.append(grewds)


matches = list(set(wdlst).intersection(grewdslst))

with open("overlap.txt", "w") as f:
    for x in matches:
        f.write(x + "\n")

print(len(wdlst),len(grewdslst),len(matches))
