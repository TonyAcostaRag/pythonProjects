
def reverse_array(arr):

    print('\nReceived array:', arr)
    first_index = 0
    last_index = len(arr) - 1

    while first_index < last_index:
        temp = arr[first_index]
        arr[first_index] = arr[last_index]
        arr[last_index] = temp

        first_index += 1
        last_index -= 1  # ---> Be aware with variables which need to be in decreasing order.

    print('Delivered array:', arr)
    return arr


print(reverse_array([1, 2, 3, 4, 5]))
print(reverse_array([i for i in range(1, 101)]))
