#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            is_elem1_number = isinstance(my_list_1[i], (int, float))
            is_elem2_number = isinstance(my_list_2[i], (int, float))
            if not is_elem1_number or not is_elem2_number:
                print("wrong type")
                result.append(0)
            else:
                result.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
    return result
