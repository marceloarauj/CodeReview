def cut_rod(p, n):
    """Take a list p of prices and the rod length n and return lists r and s.
    r[i] is the maximum revenue that you can get and s[i] is the length of the
    first piece to cut from a rod of length i."""
    # r[i] is the maximum revenue for rod length i
    # r[i] = -1 means that r[i] has not been calculated yet
    r = [-1]*(n + 1)
 
    # s[i] is the length of the initial cut needed for rod length i
    # s[0] is not needed
    s = [-1]*(n + 1)
 
    cut_rod_helper(p, n, r, s)
 
    return r, s
 
 
def cut_rod_helper(p, n, r, s):
    """Take a list p of prices, the rod length n, a list r of maximum revenues
    and a list s of initial cuts and return the maximum revenue that you can get
    from a rod of length n.
 
    Also, populate r and s based on which subproblems need to be solved.
    """
    if r[n] >= 0:
        return r[n]
 
    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(1, n + 1):
            temp = p[i] + cut_rod_helper(p, n - i, r, s)
            if q < temp:
                q = temp
                s[n] = i
    r[n] = q
 
    return q
 
 
n = int(input('Enter the length of the rod in inches: '))
 
# p[i] is the price of a rod of length i
# p[0] is not needed, so it is set to None
p = [None]
for i in range(1, n + 1):
    price = input('Enter the price of a rod of length {} in: '.format(i))
    p.append(int(price))
 
r, s = cut_rod(p, n)
print('The maximum revenue that can be obtained:', r[n])
print('The rod needs to be cut into length(s) of ', end='')
while n > 0:
    print(s[n], end=' ')
    n -= s[n]