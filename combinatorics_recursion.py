#1) calculate unique combinations (1, 2 == 2, 1) where n is an amount of all elements which are given and k - the amount of elements in each combination

first = int(input("Enter a number: "))
second = int(input("Enter a number: "))

def factorial(n):
    if n == 0: #also we may use the following expression: n == 1
        answer = 1 
    else:
        answer = n * factorial(n - 1)
    return answer


def partly_factorial(n, k): #factorial from k to n
    if n == k:
        return k
    return n * partly_factorial(n - 1, k)


unique_combs = partly_factorial(first, second + 1)/factorial(first - second)
print(unique_combs)





#2)A recursive function in Python. Consider the following function power(), which takes in two integers x and n and returns the value x^n (x in power n)


def power(x, n):
    if n == 0:
        return 1
    else:
        return power(x, n - 1) * x
