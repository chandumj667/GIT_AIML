
# sum function it takes two paramenters 
# and return the summation of those two
def sum(a, b):
    return a+b

# sub function it takes two paramenters 
# and return the subtraction of those two
def sub(a, b):
    return (a-b)

# mul function it takes two paramenters 
# and return the multiplication of those two
def mul(a, b):
    return a*b

# div function it takes two paramenters 
# and return the division of those two

def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Divison can not be done with '0' as denominator")
        print("Enter some other number")

# fact function it takes one paramenter
# and return the factorial of the the parameter
def fact(a):
    if a == 0:
        return 1
    else:
        return a * fact(a - 1)


# fib function it takes two paramenters 
# and return the fibonacci series till the number
def fib(a):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    fib = [0, 1]
    for i in range(2, n + 1):
        next_fib = fib[i - 1] + fib[i - 2]
        fib.append(next_fib)
    
    return fib[n]
if __name__ == "__main__":
    print("From calculator file it is using as a module")

