numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

even_numbers = tuple(num for num in numbers if num % 2 == 0)

odd_numbers = tuple(num for num in numbers if num % 2 != 0)

print("Original tuple:", numbers)
print("Even numbers tuple:", even_numbers)
print("Odd numbers tuple:", odd_numbers)
