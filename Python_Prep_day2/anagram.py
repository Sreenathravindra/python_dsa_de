def anagram(s,t):
    s= s.replace(' ','').lower()
    t = t.replace(' ','').lower()

    if len(s) != len(t):
        return False
    fr = {}
    for i in s.lower():
        fr[i] = fr.get(i,0)+1
    for i in t.lower():
        fr[i] = fr.get(i,0)-1
    for i in fr:
        if fr[i] !=0:
            return False
        return True

if __name__ == "__main__":
    s = "I am Lord Voldemort"
    t = "Tom Marvolo Riddle"
    print(anagram(s,t))