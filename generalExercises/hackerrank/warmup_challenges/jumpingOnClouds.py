def jumpingOnClouds(c):
    # 1. Within a loop, which is known the total number of clouds,
    # If the i+2 is a cumulus,
    # true: adds +1 to total_jumps and adds +2 to i
    # false: +1 to the total_jumps and adds +1 to i
    # return the total jumps
    total_jumps = 0
    i = 0
    while i < len(c):

        if i < (len(c) - 2):

            if c[i + 2] == 0:
                i += 2
            else:
                i += 1
            total_jumps += 1

        elif i == len(c) - 1:
            i += 1
        else:
            total_jumps += 1
            i += 1

    return total_jumps


print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))
print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))
