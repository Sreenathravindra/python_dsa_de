def long_substring(s):
    se = set()
    l = 0
    max_l = 0
    for r in range(len(s)):

        while s[r] in se:
            print('in while loop',se)
            print(s[l])
            se.remove(s[l])
            l+=1

        else:
            se.add(s[r])
            max_l = max(max_l, r-l+1)
    print(se)
    return max_l


if __name__ == "__main__":
    s = 'pwwkew'
    print(long_substring(s))