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

