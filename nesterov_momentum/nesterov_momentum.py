# Implementation using Nesterov momentum
import numpy as np
import random

def f(x):
    return sum((np.sum(np.multiply(A, x), axis=1) - b)**2)

def gradient(x):
    grad = [0 for i in range(len(x))]
    for i in range(len(A)):
        for k in range(len(x)):
            grad[k] += 2*A[i][k]*(sum(np.multiply(A[i], x)) - b[i])
    return grad

def sqrnorm(x):
    return sum(xi**2 for xi in x)

def optimize(A, b, alpha=0.1, zeta=0.5, eta=0.5, max_iter=50000):
    eps = [0 for i in range(len(b))]
    x = [random.uniform(-5,5) for i in range(len(b))]
    iteration = 0

    while iteration < max_iter:
        iteration += 1
        grad = gradient(x)

        grad_lookahead = gradient([x[i] - alpha*eps[i] for i in range(len(x))])  
        eps = [zeta*eps[i] + eta*grad_lookahead[i] for i in range(len(eps))]

        x = [x[i] - alpha*eps[i] for i in range(len(x))]
        # x = [x[i] - alpha*grad[i] for i in range(len(x))]
    print(" ".join([str(xi) for xi in x]))
    
optimize(A,b)
