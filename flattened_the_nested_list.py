def flatteninng_the_list(arr):
    flat_l = []
    for items in arr:
        if isinstance(items,list):
            flat_l.extend(flatteninng_the_list(items))
        else:
            flat_l.append(items)
    return flat_l

if __name__ == '__main__':
    arr = [1,[2,3,4],5,[6],7,[8,[9,10,[11,[12,[13,[14,[15]]]]]]]]
    print(flatteninng_the_list(arr))