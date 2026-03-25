def second_largerst(arr):
    seen = set()
    max_ele = float('-inf')
    for i in arr:
        if i not in seen:
            max_ele = max(max_ele, i)
        seen.add(i)
    if len(seen) == 1:
        return -1
    seen.remove(max_ele)
    return  max(seen)

if __name__ == '__main__':
    arr = [10, -4, -2]
    print(second_largerst(arr))