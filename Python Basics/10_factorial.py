def factorial(a):
    sum = 1
    for i in range(a, 0, -1):
        sum *= i
    return sum

num = int(input("Enter a number: "))
print(factorial(num))