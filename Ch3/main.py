def countdown(num):
    print(num)
    if num == 1:
        return
    else:
        countdown(num - 1)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
fact=factorial(4)
print("factorial = ",end="")
print(fact)
countdown(4)
