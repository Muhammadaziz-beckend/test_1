def spin_words(sentence:str):
    arr:list[str] = []
    arr.extend(sentence.split())
    
    for i in range(len(arr)):
        if len(arr[i]) >= 5:
            text = [*arr[i]]
            text.reverse()
            text1 = ''.join(text)
            arr[i] = text1

    return ' '.join(arr)



print(spin_words('Hey fellow warriors'))