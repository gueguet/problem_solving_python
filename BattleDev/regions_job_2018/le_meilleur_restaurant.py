import math
import statistics

lines = ['18', '14 7 5', '0 2 11', '0 5 11', '15 0 2', '15 4 15', '2 0 15', 
         '10 15 10', '9 1 1', '3 2 1', '4 6 5', '11 0 8', '1 0 8', '12 6 11', 
         '0 14 1', '14 11 7', '14 14 14', '5 15 2', '13 8 15']

nb_restau = int(lines[0])
score_resto = []


for notes in lines[1:]:
    avg = 0
    for values in list(map(int, notes.split(" "))):
        avg += values
    score_resto.append(int(round(avg/3)))

print(max(score_resto))
