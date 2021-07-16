def derivative(x):
    fx_add = f(x+tol)
    fx_subtract = f(x-tol)
    fx = f(x)
    # First order derivative
    D1 = (fx_add - fx_subtract)/(2*tol)
    # Second order derivative
    D2 = (fx_add -2*fx + fx_subtract)/tol**2
    
    return D1, D2
    
       
def newton(a, b, f, tol):
    x = (a+b)/2
    while True:
        D1, D2 = derivative(x)
        xnew = x - (D1/D2)
        if abs(x - xnew) < tol:
            return xnew
            break
        x = xnew
    
x = newton(a, b, f, tol)
print(x)

