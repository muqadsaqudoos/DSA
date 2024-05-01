def no_of_occurences(list):
    count_dict = {}
    for element in list:
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1
    print(count_dict)

    for element, count in count_dict.items():
        print(f"{element} occur {count} times")

a = [1,2,3,2,3,4,2,5,3,6,4,3,6,54]
no_of_occurences(a)