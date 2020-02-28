from pprint import pprint

lines = ['5 50', 
         '7 24', 
         '12 10 10 9 10', '5 21 31 29 28 36 13 48 27 45 19 3', '35 4 42 16 47 20 8 10 33 44',
         '6 14 23 12 26 2 38 39 40 15', '49 18 25 46 24 34 37 7 32', '30 1 11 9 43 17 41 42 22 50']

out_res = -1

num_line = lines[0].split(" ")[0]
num_station = lines[0].split(" ")[1]

dep_station = lines[1].split(" ")[0]
arr_station = lines[1].split(" ")[1]

line_dict = {}

for (i, line) in enumerate(lines[3:], start=1):
    line_dict[i] = line.split(" ")
    if dep_station in line_dict[i]:
        dep_line = i

pprint(line_dict)


# if dep and arr in the same line 
if arr_station in line_dict[dep_line]:
    out_res = 1
    print(out_res)

# find common station between lines
cur_station = dep_station
cur_line = dep_line
possible_num_line = []


