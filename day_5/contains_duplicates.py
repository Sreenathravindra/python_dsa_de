def contains_dup(arr):
    seen = set()
    for i in arr:

        if i in seen:
            return True
        seen.add(i)
    return False


if __name__ == '__main__':
    arr = [1,2,3,4,5,4,5]
    print(contains_dup(arr))