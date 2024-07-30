def sum_two_smallest_numbers(numbers):
    main_num = numbers[0]
    
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if (numbers[i] + numbers[j]) < main_num:
                main_num = numbers[i] + numbers[j]

    print(main_num)


print(sum_two_smallest_numbers([19, 5, 42, 2, 77])) # ===> 7