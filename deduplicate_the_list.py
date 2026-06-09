def deduplication_list(ls):
    ls1 = set()
    for i in ls:
        ls1.add(i)
    return list(ls1)

if __name__ == '__main__':
    ls = [1,2,2,3,3,4,4,5,6,6,6,7,7,7,7,100,100,101,102]
    print(deduplication_list(ls))