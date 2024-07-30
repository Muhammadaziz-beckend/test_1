def high_and_low(numbers):
    arr = []
    arr.extend(numbers.split())
    
    arr2 = list(map(int,arr))
    max_num = max(arr2)
    min_num = min(arr2)
    return (f'{max_num} {min_num}')