# battle dev 2019 - tobogan

import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

num_enfant = lines[0]
list_enfant = lines[1].split(" ")
out_res = 0

for enfant in list_enfant:
    if (5 <= int(enfant) <= 9):
        out_res += 1

print(out_res)
