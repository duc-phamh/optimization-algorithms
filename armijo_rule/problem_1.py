c = 0.01
alpha = 1
x = (a+b)/2

def df(x):
    return (f(x + tol) - f(x - tol))/2/tol

def armijo(f, grad_approx, x, c, alpha):
    return (f(x - alpha* grad_approx)
    <=
    f(x) - c*alpha*grad_approx**2)

while True:
    grad_approx = df(x)
    
    if abs(grad_approx) < tol:
        print(x)
        break
    
    # Find the optimal alpha by Armijo rule
    while armijo(f, grad_approx, x, c, alpha*1.2):
        alpha *= 1.2

    max_iter_armijo = 30
    cur_iter_armijo = 0
    while not armijo(f, grad_approx, x, c, alpha):
        alpha /= 1.2
        cur_iter_armijo += 1
        if cur_iter_armijo > max_iter_armijo:
            print(x)

    # Update the variables by the alpha obtained above
    x = x - alpha*grad_approx

