#python 3 program 2 find
#factorial of given number
#Function to find factorial of given number
def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n - 1)


#Driver Code
num = 4
print("Factorial of", num, "is", factorial(num))
