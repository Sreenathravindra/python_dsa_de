def long_repeating(s,k):
    ch = {}
    j=list(s)
    l = 0
    c = 0
    max_s = 0
    for r in range(len(s)):


        ch[j[r]] = ch.get(j[r],0)+1


        if j[r] != j[l]:
            max_s = max(max_s, r - l + 1)
            l = r
            while c <=k:

                j[r] = j[0]
                c+=1

    print(c)
    print(max_s)
    s = ''.join(j)
    return s


if __name__ == "__main__":
    s = 'ABAB'
    k = 2
    print(long_repeating(s,k))