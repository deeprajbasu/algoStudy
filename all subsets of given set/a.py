def subsets(l):
    
    if l == []:
        return [[]]

    x = subsets(l[1:])
    return x + [[l[0]] + y for y in x]
