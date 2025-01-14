def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
if __name__ == "__main__":
    
    n = int(input("Enter a number: "))
    if(n < 0):
        print("Factorial does not exist for negative numbers")
    else:
        print("Factorial of", n, "is:", factorial(n))