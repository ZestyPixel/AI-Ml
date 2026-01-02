try:
    x = int(input("Enter a number: "))
    ans = 10/x
except ZeroDivisionError:
    print("Divide by 0 error")
else:
    print(f"Ans: {ans}")
finally: #Runs irrespective of exception occurrence
    print("Program Done")