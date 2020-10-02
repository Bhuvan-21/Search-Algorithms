import sys
def extend(explored, maze, path, m, n):
    paths = []
    a, b = path[-1]
    ext = [(a+1, b), (a, b+1), (a-1, b), (a, b-1)]
    for ex in ext:
        np = path[:]
        if ex[0] < m and ex[1] < n and ex[0] >= 0 and ex[1] >= 0:
            if maze[ex[0]][ex[1]] == 0 and not explored.get(ex, False):
                np.append(ex)
                explored[ex] = True
                paths.append(np)
    return paths, explored


def h(path):
    pt = path[-1]
    return abs(pt[0]-gp[0]) + abs(pt[1] - gp[1]) + len(path)


if len(sys.argv) != 2:
    print("Using default file")
    p = "maze2.txt"
else:
    p = sys.argv[1]

m = 0
n = 0
maze = []
a = []
sp = (-1, -1)
gp = (-1, -1)
f = open(p, 'r')
for line in f:
    a.append(line[:-1])
    for i in range(len(line)-1):
        if line[i] == 'A':
            sp = (m, i)
        if line[i] == 'B':
            gp = (m, i)
    m += 1
    n = max(n, len(line)-1)
print("Maze")
for i in range(m):
    s = a[i]
    ar = []
    for j in range(n):
        if s[j] == 'S':
            sp = (i, j)
        if s[j] == 'G':
            gp = (i, j)
        if s[j] == '#':
            ar.append(1)
        else:
            ar.append(0)
    print(a[i])
    maze.append(ar)
paths = [[sp]]
final = None
explored = {sp: True}

while len(paths) != 0:
    paths.sort(key = h)
    n_path = paths[0]

    if n_path[-1] == gp:
        final = n_path
        break
    nps, explored = extend(explored, maze, n_path, m, n)
    paths.pop(0)
    for p in nps:
        paths.append(p)
if final:
    print("------")
    print("ANSWER")
    print("------")
    maze2 = ["" for w in range(m)]
    for i in range(m):
        for j in range(n):
            if (i, j) == sp:
                maze2[i] += "A"
            elif (i, j) == gp:
                maze2[i] += "B"
            elif (i, j) in final:
                maze2[i] += ":"
            else:
                maze2[i] += a[i][j]
        print(maze2[i])
else:
    print("No path")
