initial = list(initial)

def approximate_gradient(f, x, n, gamma, valf=None):
    if valf is None:
        valf = f(x)
    grad_approx = [-valf for j in range(n)]
    for j in range(n):
        grad_approx[j] += f(x[:j] + [x[j]+gamma] + x[j+1:])
        grad_approx[j] /= gamma
    return (grad_approx, valf)

def sqrnorm(x):
    return sum(t**2 for t in x)

def armijo(f, grad_approx, x, c, alpha):
    return (
        f([x[j] - alpha * grad_approx[j] for j in range(len(x))]) 
        < 
        f(x) - c * alpha * sqrnorm(grad_approx)
    )

def optimizer(f, initial, tolerance, max_iter, c):
    x_current = initial
    n = len(initial)
    for i in range(max_iter):
        grad_approx, valf = approximate_gradient(
            f, 
            x_current, 
            n,
            tolerance**2
        )
        alpha = 1.
        while armijo(f, grad_approx, x_current, c, alpha * 1.5):
            alpha *= 1.5
        max_iter_armijo = 100
        cur_iter_armijo = 0
        while not armijo(f, grad_approx, x_current, c, alpha):
            alpha *= 0.5        
            cur_iter_armijo += 1
            if cur_iter_armijo > max_iter_armijo:
                return x_current
        
        x_next = [x_current[j] - alpha * grad_approx[j] for j in range(n)]
        x_current = x_next
    return x_current

result = optimizer(f, initial, tol, max_iter=5000, c=0.9)
print(" ".join([str(x) for x in result]))
