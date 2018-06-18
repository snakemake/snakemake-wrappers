# for debugging metazoa dataset
# compares EOGs present in the ancestral and orthoinfo file

import os
import sys

ancestral = sys.argv[1]
ortho = sys.argv[2]

f = open(ancestral)
f2 = open(ortho)

in_set = []
for line in f:
    if line.startswith('>'):
        name = line.strip()[1:]
        if name not in in_set:
            in_set.append(name)

print(len(in_set))

info = []
for line in f2:
    if line.startswith('Ortho'):
        pass
    else:
        name = line.split()[0]
        if name not in info:
            info.append(name)

print(len(info))

out = open('mia_ogs.dbg', 'w')

for entry in in_set:
    if entry not in info:
        out.write('%s\n' % (entry))

