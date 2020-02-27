# https://www.isograd.com/FR/solutionconcours.php?contest_id=59
# Dev Champion 2019 - Pics de fréquentation

import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

num_p = int(lines[0])
list_p = []

for i in range(1, num_p+1):
    list_p.append(lines[i].split(" "))

for item in list_p:
    item[0] = int(item[0])
    item[1] = int(item[1])

list_p.sort(key=lambda x: x[0])

# at each arrival we count the current number of people present
# the final output will be the max of this list
num_current_p = 1
list_num_p = [1]
last_departure = [list_p[0][1]]
last_people = list_p[0]

for people in list_p[1:]:
    num_current_p += 1
    for departure in last_departure:
        if people[0] > departure:
            last_departure.remove(departure)
            num_current_p -= 1

    last_departure.append(people[1])
    list_num_p.append(num_current_p)

print(max(list_num_p))
