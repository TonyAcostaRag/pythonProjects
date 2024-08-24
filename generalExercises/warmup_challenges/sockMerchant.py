def sockMerchant(n, ar):

    # 1. Put each sock into a dictionary to have color : count
    sock_dictionary = {}

    for sock in ar:
        if sock not in sock_dictionary:
            sock_dictionary[sock] = 1
        else:
            sock_dictionary[sock] += 1

    # 2. Sum and return the total number of pairs in the dictionary
    pair_sum = 0
    for num in sock_dictionary.values():
        pair_sum += (num // 2)

    return pair_sum


print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
print(sockMerchant(10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]))
