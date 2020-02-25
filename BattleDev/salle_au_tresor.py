# https: // www.isograd.com/FR/solutionconcours.php?contest_id = 46
# salle au tresor
# not finished... error with TOSA tool...


array = [['*', '*', 'o', 'o', '.'], ['.', 'o', '.', '.', '.'], ['*', '*',
                                                                '.', '.', '.'], ['.', '.', '*', '.', '*'], ['.', '*', '*', '.', 'o']]


def putin(piece):

    list_o = []
    list_star = []

    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j] == 'o':
                list_o.append((i, j))
            if piece[i][j] == '*':
                list_star.append((i, j))


    pos = [0, 0]
    butin = 0
    path = ""

    # collect pieces
    while len(list_o) != 0:
        o_x = list_o[0][0]
        o_y = list_o[0][1]

        dep_x = o_x - pos[0]
        dep_y = o_y - pos[1]

        if (dep_y > 0):
            path += (">" * dep_y)

        if (dep_y < 0):
            for i in range(abs(dep_y)):
                path += ("<")

        if (dep_x > 0):
            for i in range(dep_x):
                path += "v"

        if(dep_x < 0):
            path += ("^" * (dep_x))

        path += "x"

        del list_o[0]

        pos[0] = o_x
        pos[1] = o_y

        print(path)

putin(array)


# error dans l'outil en ligne... probleme de print...
