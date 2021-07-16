from math import sqrt

alpha = (3-sqrt(5))/2

c = (1-alpha)*a + alpha*b
d = alpha*a + (1-alpha)*b

fa = f(a)
fb = f(b)
fc = f(c)
fd = f(d)

while True:
    if abs(a - b) < tol:
        print(d)
        break
        
    if (fc < fd) and (fd < fb):
        fb = fd
        b = d 
        
        fd = fc
        d = c
        
        c = (1-alpha)*a + alpha*b
        fc = f(c)
        
    elif (fa > fc) and (fc > fd):
        fa = fc
        a = c
        
        fc = fd
        c = d
        
        d = alpha*a + (1-alpha)*b
        fd = f(d)
