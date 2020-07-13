# https://www.codewars.com/kata/55983863da40caa2c900004e/train/python



import unittest

# go through the list from tight part
def next_bigger(n):
    n_lst = list(str(n))
    i, j = len(n_lst) - 1, len(n_lst) - 1

    while i > 0 and n_lst[i - 1] >= n_lst[i]:
        i -= 1

    if i <= 0:
        return -1

    while n_lst[j] <= n_lst[i - 1]:
        j -= 1

    swap(n_lst, i - 1, j)
    j = len(n_lst) - 1
    while i < j:
        swap(n_lst, i, j)
        i += 1
        j -= 1
    return int("".join(c for c in n_lst))


def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp



"""
First try --> problem was that I only take care about the previous digit and not all..

def next_bigger(n):

    if len(str(n)) == 1:
        return -1

    # if all same digit inside the number
    if (len(set(str(n)))) == 1:
        return -1


    n = str(n)
    m = []
    count = 0

    for i in range(len(n)-1, -1, -1):

        count += 1

        if (n[i] > n[i-1]):
            m.insert(0, n[i-1])
            m.insert(0, n[i])
            break

        else:
            m.insert(0, n[i])

    list_to_add = []

    for k in range(0, len(n)-count-1):
        list_to_add.append(n[k])

    m = list_to_add + m

    res = ""

    for i in m:
        res += (i)


    return (int(res))
"""








# test 


class Test(unittest.TestCase):

    def test_next_bigger(self):


        self.assertEqual(next_bigger(12), 21)
        self.assertEqual(next_bigger(513), 531)
        self.assertEqual(next_bigger(2017), 2071)
        self.assertEqual(next_bigger(414), 441)
        self.assertEqual(next_bigger(144), 414)


if __name__ == "__main__":
    unittest.main()


