def frequency_map(s):

    fr ={}
    for seen in s:

        fr[seen] = fr.get(seen,0)+1

    for i in range(len(s)):
        if fr[s[i]] == 1:
            return i

    return -1

if __name__ == '__main__':
    s = 'loveleetcode'
    a = frequency_map(s)
    print(a)