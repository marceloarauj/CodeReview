def powerset(list):
  return reduce(lambda x, y: x+(map(lambda z:z+[y],x)),list,[[]])