
def find_sf(x):
    r = []
    for items in x:
        if type(items) is list :
            r.extend(find_sf(items))
        else:
            r.append(items)
    return r

print(find_sf([[1, 2, [3, 4]], [5, [6, 7]], 8, [9]]))

