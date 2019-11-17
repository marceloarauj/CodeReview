def lcw(u, v):
    """Return length of an LCW of strings u and v and its starting indexes.
 
    (l, i, j) is returned where l is the length of an LCW of the strings u, v
    where the LCW starts at index i in u and index j in v.
    """
    c = [[-1]*(len(v) + 1) for _ in range(len(u) + 1)]
 
    lcw_i = lcw_j = -1
    length_lcw = 0
    for i in range(len(u)):
        for j in range(len(v)):
            temp = lcw_starting_at(u, v, c, i, j)
            if length_lcw < temp:
                length_lcw = temp
                lcw_i = i
                lcw_j = j
 
    return length_lcw, lcw_i, lcw_j
 
 
def lcw_starting_at(u, v, c, i, j):
    """Return length of the LCW starting at u[i:] and v[j:] and fill table c.
 
    c[i][j] contains the length of the LCW at the start of u[i:] and v[j:].
    This function fills in c as smaller subproblems for solving c[i][j] are
    solved."""
    if c[i][j] >= 0:
        return c[i][j]
 
    if i == len(u) or j == len(v):
        q = 0
    elif u[i] != v[j]:
        q = 0
    else:
        q = 1 + lcw_starting_at(u, v, c, i + 1, j + 1)
 
    c[i][j] = q
    return q
 
 
u = input('Enter first string: ')
v = input('Enter second string: ')
length_lcw, lcw_i, lcw_j = lcw(u, v)
print('Longest Common Subword: ', end='')
if length_lcw > 0:
    print(u[lcw_i:lcw_i + length_lcw])