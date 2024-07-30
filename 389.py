s = "abcd"
t = "abcde"

def a():
    text = ''
    for i in range(len(s)):
        if s[i] == t[i]:
            s.replace(s[i],'')
            t.replace(s[i],'')
            print(s,t)
        else:
            text += s[i]
    return text

print(a())