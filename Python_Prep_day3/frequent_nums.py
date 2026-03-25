def top_k(nums, k):
    fr = {}

    # count
    for i in nums:
        fr[i] = fr.get(i, 0) + 1

    items = list(fr.items())

    # swap (freq, num)
    new_items = []
    for i in items:
        new_items.append((i[1], i[0]))
    print(new_items)
    # sort by freq
    new_items.sort(reverse=True)
    print(new_items)

    # pick top k
    result = []
    for i in new_items[:k]:
        result.append(i[1])

    return result



if __name__ == '__main__':
    nums = nums = [1,1,1,2,2,3,3,3,3]
    k = 2
    print(top_k(nums,k))