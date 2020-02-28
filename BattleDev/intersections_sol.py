

from collections import defaultdict, deque


def bfs(start, start_line, end, rev_lines, lines):
    queue = deque([(start, 0, start_line)])
    visited = defaultdict(lambda: False)

    while queue:
        cur, changes, cur_line = queue.pop()

        if cur == end:
            return changes

        for line in rev_lines[cur]:
            if cur_line != line and not visited[(cur, line)]:
                queue.appendleft((cur, changes + 1, line))
                visited[(cur, line)] = True
            elif cur_line == line:
                for sta in (lines[cur_line] - {cur}):
                    if not visited[(sta, cur_line)]:
                        queue.appendleft((sta, changes, cur_line))
                        visited[(sta, cur_line)] = True

    return -1


def solve(start, end, lines):
    rev_lines = defaultdict(set)

    for u, stations in enumerate(lines):
        for sta in stations:
            rev_lines[sta].add(u)

    m = float('+inf')
    for start_line in rev_lines[start]:
        r = bfs(start, start_line, end, rev_lines, lines)
        if r != -1:
            m = min(r, m)

    return -1 if m == float('+inf') else m + 1


def main():
    N, M = list(map(int, input().split(' ')))
    start, end = list(map(int, input().split(' ')))
    nbStations = list(map(int, input().split(' ')))
    lines = [set(map(int, input().split(' '))) for _ in range(N)]

    print(solve(start, end, lines))


if __name__ == '__main__':
    main()
