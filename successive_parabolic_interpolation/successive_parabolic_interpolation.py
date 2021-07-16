import numpy as np
x1 = a
f1 = f(a)
x2 = b
f2 = f(b)
x3 = (a+b)/2
f3 = f(x3)
while True:
    if abs(x1-x3) < tol:
        print(x3)
        break
    
    A = np.array([[x1**2, x1, 1], [x2**2, x2, 1], [x3**2, x3, 1]])
    B = np.array([f1, f2, f3])
    X = np.linalg.inv(A).dot(B)

    x_new = -X[1]/(2*X[0])
    
    if x_new > x2:
        x1 = x2
        f1 = f2
        x2 = x_new
        f2 = f(x_new)
    else:
        x3 = x2
        f3 = f2
        x2 = x_new
        f2 = f(x_new)

