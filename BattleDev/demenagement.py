# https://www.isograd.com/FR/solutionconcours.php?contest_id=46
# Demenagement

import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

num_carton = int(lines[0])

poids_tot = 0
nb_aller_retour = 0

for carton in lines[1:]:

    if (poids_tot + int(carton)) > 100:
        nb_aller_retour += 1
        poids_tot = int(carton)

    else:
        poids_tot += int(carton)

nb_aller_retour += 1

sys.stderr.write("Res err : \n")
sys.stderr.write(str(nb_aller_retour))

print(nb_aller_retour)
