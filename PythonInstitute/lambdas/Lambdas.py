

def the_print_function(args, function):
    for i in args:
        print("f(", i, ") = ", function(i), sep="")


# Printing the first map results
print("Printing the first set of results of map():")
the_print_function([x for x in range(-3, 4)], lambda x: 2 * x ** 2 - 4 * x + 2)


mapped_values = list(map(lambda x: 2 * x ** 2 - 4 * x + 2, [i for i in range(-3, 4)]))

# Printing the second map results
print("Printing the second set of results of map():")
for i in mapped_values:
    print(i)



filtered_values = list(filter(lambda x: x >= 70, [x for x in range(0, 101)]))

# Printing the first filter results
print("Printing the first set of results of filter():")
for i in filtered_values:
    print(i)
