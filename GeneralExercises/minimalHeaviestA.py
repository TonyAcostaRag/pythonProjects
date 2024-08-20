# 1. null = A inter B
# 2. set = A union B
# 3. A 2 num limited
# 4. sum A > sum B

def minimalHeaviestSetA(arr):

    def extract_as(arr_sorted, x_arr):

        print('sorted arr:', arr_sorted)
        print('Received list:', x_arr)
        while True:

            for i in range(1, len(arr_sorted)):
                temp_arr = [arr_sorted[0], arr_sorted[i]]

                sum_a = 0
                for j in range(1, len(arr_sorted)):
                    sum_a += arr_sorted[j]

                if (temp_arr[0] + temp_arr[1]) > sum_a - arr_sorted[i]:
                    print(temp_arr[0] + temp_arr[1])
                    print(sum_a - arr_sorted[i])
                    print('Appending arr a:', temp_arr)

                    x_arr.append(temp_arr)
                    print('Appended value:', x_arr)

                #print('Print received list at i:', x_arr)

            break
        print('print before out func:', x_arr)
        return x_arr

    arr.sort(reverse=True)
    as_arr = []
    as_arr = extract_as(arr, as_arr)

    # Method to check the biggest A

    # Method to get A and B sets.
    print(as_arr)

minimalHeaviestSetA([5, 3, 2, 4, 1, 2])
