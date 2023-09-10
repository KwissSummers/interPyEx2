import random
import time


def fibonacci(nthTerm):
    if nthTerm <= 0:
        return "invalid input, please enter a positive integer"
    elif nthTerm <= 2:
        return 1
    else:
        x, y = 1, 1
        for _ in range(3, nthTerm + 1):
            x, y = y, x + y
        return y
    
nthTerm = random.randint(15, 35)
startTime = time.time()
fibNum = fibonacci(nthTerm)
endTime = time.time()
totalTime = endTime - startTime

print(f"The {nthTerm}th Fibonacci term calculated is {fibNum}")
print(f"The amount of time the implementation took was {totalTime} seconds")

