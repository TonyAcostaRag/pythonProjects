
def three_dimentional_array():
    rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

    print(rooms)

    rooms = [[[True for r in range(20)] for f in range(14,-1)] for t in range(2,-1)]


    print (rooms)

    for build in rooms:
        for floor in build:
            for room in floor:
                print(room)
                print()

def iterate_list_backwards(list_to_iterate):

    for i in range(len(list_to_iterate)-1, -1, -1):

        print(i)


def is_prime(num):

    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def is_prime_recursive(num, n=2):

    if num <= 1:
        return None
    
    if n == num:
        return True
    elif num % n == 0:
        return False
    else:
        return is_prime_recursive(num, n+1)

def is_prime_roque(num):
    for i in range(2,num-1):
        if num%(i) == 0: 
            return False 
        return True

def isPrime_romero(n, x = 1):

    x += 1
    #print(n, x)
    if (x == n):
        return True
    elif (n%x == 0):
        return False
    else:
        return isPrime_romero(n, x)


if __name__ == '__main__':

    #three_dimentional_array()
    #iterate_list_backwards([1, 2, 3, 4, 5])
    
    for i in range(20):
        #if is_prime(i + 1):
        if is_prime_recursive(i + 1):
        #if is_prime_roque(i + 1):
        #if isPrime_romero(i + 1):
            print(i + 1, end=" ")
    print()
    