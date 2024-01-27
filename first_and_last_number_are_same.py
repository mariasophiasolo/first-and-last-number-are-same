# checking if the first and last number are the same

def is_first_and_last_same(list):
    # check if the list is not empty
    if list:
        # then compare the first and last number
        return list[0] == list[-1]
    else:
        # if the list is empty then consider it as false
        return False

# first given 
numbers_x = [10, 20, 30, 40, 10]
result = is_first_and_last_same(numbers_x)
print("result is:",  is_first_and_last_same(numbers_x))

# second given [75, 65, 35, 75, 30]



