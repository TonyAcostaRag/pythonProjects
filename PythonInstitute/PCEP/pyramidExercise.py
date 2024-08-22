blocks = int(input("Enter the number of blocks: "))

height = 0

if blocks > 0:

    pyramid = base = height = 1

    while blocks > pyramid:
        base += 1
        pyramid += 1

        if blocks > pyramid:
            for i in range(height):

                pyramid += 1
                if (i+1) == height:
                    height += 1

                if pyramid == blocks:
                    break

print("The height of the pyramid:", height)

