def reverse_words(text):
    arr = []
    arr.extend(text.split())
    
    for i in range(len(arr)):
        text = [*arr[i]]
        text.reverse()
        text2 = ''.join(text)
        
        arr[i] = text2
        
    return ' '.join(arr)

print(reverse_words('Hello Woreld'))