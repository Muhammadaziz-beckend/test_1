x = -121

def s():
    num = str(x)
    num2 = [*str(x)]
    num2.reverse()
    num2 = ''.join(num2)

    return (num,num2,num == num2)


print(s())
# 1