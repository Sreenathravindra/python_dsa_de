def anagram(s,t):
    ch = {}
    s=s.strip().lower()
    t =t.strip().lower()
    su=0
    if len(s) != len(t):
        return False
    for i in s:
        ch[i] = ch.get(i,0)+1
    for i in t:
        ch[i] = ch.get(i,0)-1
    print(ch)
    for i, k in enumerate(ch):
        if ch[k] !=0:
            return False




    return True

if __name__ == "__main__":
    s = "anagram "
    t = "nagaram"
    print(anagram(s,t))