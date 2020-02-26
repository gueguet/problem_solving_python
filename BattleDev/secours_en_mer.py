import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

num_bateau = int(lines[0])
per_bateau = lines[1:]
nb_aller_retour = 0

for per in per_bateau:
    q = (int(per) // 10)
    r = (int(per) % 10)

    nb_aller_retour += q

    if (r != 0):
        nb_aller_retour += 1

print(nb_aller_retour)
