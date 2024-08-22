def is_prime(num):
    
    for i in range(1, num):
            
        if num%(i+1) == 0:
            return (i+1) == num

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
