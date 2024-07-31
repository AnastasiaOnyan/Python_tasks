num = int(input("Enter a positive number: ")) #starts from 1: 1 1 2 3 5 8 13 ....

def fibonacci_summ(n):
    if n == 1 or n <= 0:
        return 1
    return fibonacci_summ(n - 2) + fibonacci_summ(n - 1)


print(fibonacci_summ(num))
