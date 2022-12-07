n = int(input("Enter number"))

def factorial(n):
    if n == 1:
        return 1
    else:
     return n * factorial(n-1)

print("Factorial of",n,"is:",factorial(n))
