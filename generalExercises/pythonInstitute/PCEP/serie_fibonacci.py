def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    
    num1 = num2 = 1
    serie = 0
    
    for i in range(3, n + 1):
        
        serie = num1 + num2
        num1, num2 = num2, serie
    return serie  

for i in range(10):
    print("Iteracion: ", i, "->", fibonacci(i))
