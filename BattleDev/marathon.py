# https://www.isograd.com/FR/solutionconcours.php?contest_id=46
# Marathon

import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))


pos = int(lines[0])

sys.stderr.write("Stderr : \n")

for depacement in lines[1:]:
    depacement_split = depacement.split(" ")
    pos += int(depacement_split[0])
    pos -= int(depacement_split[1])

sys.stderr.write(str(pos))

if (pos <= 100):
    print(1000)
elif pos <= 10000:
    print(100)
else:
    print("KO")
