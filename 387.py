s = "leetcode"

def a():
    if not 1 <= len(s) <= (10 * 10 * 10 * 10 * 10):
        return -1
    for i in s:
        if s.count(i) == 1:
            return s.index(i)
    
    return -1


print(a())