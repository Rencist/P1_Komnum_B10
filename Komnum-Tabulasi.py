import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

def bolzano_method(func, a, b, iteration):
    i = 1
    ite = int(iteration)
    def f(x):
        f = eval(func)
        return f 
    
    data = [['iterasi', 'x1', 'x2', 'x3', 'f(x1)', 'f(x2)', 'f(x3)']]
    while iteration > 0:
        c = (b+a)/2
        data.append([i,a,b,c,f(a),f(b),f(c)])
        i = i + 1
        if f(a) * f(b) >= 0:
            print("No root or multiple roots present")
            quit()

        elif f(c) * f(a) < 0:
            b = c

        elif f(c) * f(b) < 0:
            a = c
        else:
            print("Error happens")
            quit()
        ans = (b+a)/2
        iteration -= 1
    
    print(tabulate(data, headers="firstrow", tablefmt="github"))

    print(f"The lower boundary is {a} and upper boundary is {b}")
    print(f"The root after {ite} iteration is {ans}")

function = input("function : ")
a = input("lower root boundary: ")
b = input("upper root boundary: ")
iteration = input("how many iteration: ")

bolzano_method(function, float(a), float(b), float(iteration))

x = np.linspace(-10,10,num = 1000)
y = eval(function)
plt.grid(visible=True)
plt.plot(x, y)
plt.show()
plt.xlabel('X Axis')
plt.ylabel('Y Axis')