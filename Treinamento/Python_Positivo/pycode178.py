def count_paths(m, n, holes):
    """Return number of paths from (0, 0) to (m, n) in an m x n grid.
 
    holes is a list of tuples (x, y) where each tuple is a coordinate which is
    blocked for a path.
    """
    paths = [[-1]*(m + 1) for _ in range(n + 1)]
    return count_paths_helper(m, n, holes, paths, n, m)
 
 
def count_paths_helper(m, n, holes, paths, x, y):
    """Return number of paths from (0, 0) to (x, y) in an m x n grid.
 
    holes is a list of tuples (x, y) where each tuple is a coordinate which is
    blocked for a path.
 
    The function uses the table paths (implemented as a list of lists) where
    paths[a][b] will store the number of paths from (0, 0) to (a, b).
    """
    if paths[x][y] >= 0:
        return paths[x][y]
 
    if (x, y) in holes:
        q = 0
    elif x == 0 and y == 0:
        q = 1
    elif x == 0:
        q = count_paths_helper(m, n, holes, paths, x, y - 1)
    elif y == 0:
        q = count_paths_helper(m, n, holes, paths, x - 1, y)
    else:
        q = count_paths_helper(m, n, holes, paths, x - 1, y) \
            + count_paths_helper(m, n, holes, paths, x, y - 1)
 
    paths[x][y] = q
    return q
 
 
m, n = input('Enter m, n for the size of the m x n grid (m rows and n columns): ').split(',')
m = int(m)
n = int(n)
print('Enter the coordinates of holes on each line (empty line to stop): ')
holes = []
while True:
    hole = input('')
    if not hole.strip():
        break
    hole = hole.split(',')
    hole = (int(hole[0]), int(hole[1]))
    holes.append(hole)
 
count = count_paths(m, n, holes)
print('Number of paths from (0, 0) to ({}, {}): {}.'.format(n, m, count))