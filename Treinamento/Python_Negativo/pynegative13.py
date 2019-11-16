d = {}
datas = [1, 2, 3, 4, 2, 3, 4, 1, 5]
for k in datas:
    if k not in d:
        d[k] = 0 
    d[k] += 1