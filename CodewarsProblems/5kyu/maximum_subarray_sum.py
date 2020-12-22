# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python


def max_sequence(arr):
    max_sub, tmp = 0, 0

    for x in arr:
        tmp += x
        tmp = max(0, tmp)
        max_sub = max(max_sub, tmp)

        print("tmp : ", tmp)
        print("max_sub : ", max_sub)

    return max_sub

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # --> should return 6
