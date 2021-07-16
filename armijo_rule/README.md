# Armijo's rule (First Wolfe's condition)

Algorithm description: https://en.wikipedia.org/wiki/Wolfe_conditions

Youtube video: https://www.youtube.com/watch?v=X4Pjd-1R-jI

---


**Problem 1:**

Minimize the function `f()` on the interval `[a,b]` with precision at least `tol` using inexact method with Armijo’s rules (no curvature constraint). You can take $c_{1}$ = 0.8, $c_2$ = 3. Assume that variables `f,a,b` are already defined. You need to output the point of the minimum of the function using the standard `print` statement. You can start building the sequence of points with either `a` or `b`. To compute the derivative of a function at a given point use the approximation $\approx \frac{f(x+\epsilon)-f(x-\epsilon)}{2\epsilon}$ for $ϵ=tol$. Make sure you never drop out of optimization bracket.

Sample Input 1:
```
from math import sin
a = 2.
b = 7.
tol = 0.000001
f = sin
```
Sample Output 1:
```
4.712388985743289
```


Sample Input 2:
```
f = lambda x: x**1.8 - 15*x + 4
a = 2.
b = 30.
tol = 0.000001
```
Sample Output 2:
```
14.158702029267767
```

---

**Problem 2:** 

The goal of this problem is to give a first try to multivariate function optimization applied to “Rosenbrock’s banana” function.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Rosenbrock_function.svg/720px-Rosenbrock_function.svg.png" width="400">

Sample Input 1:
```
def f(x1, x2): 
    p = 1
    q = 10
    return (p-x1)**2+q*(x2-x1**2)**2
tol = 0.00001
initial = (0., 0.)
```
Sample Output 1:
```
0.9999995431600506 0.9999990675164568
```

Sample Input 2:
```
def f(x1, x2): 
    p = 4
    q = 5
    return (p-x1)**2+q*(x2-x1**2)**2
tol = 0.00001
initial = (10., 0.)
```
Sample Output 2:
```
3.999997310301427 15.99997847418483
```

---

**Problem 3:** 

Optimize functions of significant (dozens, hundreds) number of variables.

Sample Input 1:
```
def f(x): 
    n = len(x)
    p = 4
    return sum((x[i] - p)**2 for i in range(n))
tol = 0.00001
initial = (0.,) * 20 + (5.,) * 20
```
Sample Output 1:
```
3.9999950231281116 3.9999950231281116 3.9999950231281125 3.999995023128113 3.999995023128113 3.9999950231281116 3.999995023128115 3.9999950231281147 4.000002178629641 4.000002178629641 4.000002178629641 4.000002178629641 4.000002178629642 4.000002178629642 4.000002178629643 3.999995023128114 4.000002178629642 4.000002178629642 4.000002178629641 4.000002162174651 3.9999958611368296 3.9999958611368296 3.9999958611368296 3.9999958611368296 3.9999958611368296 3.9999958446818398 3.9999958446818398 3.9999958446818398 3.9999958446818398 3.9999958446818398 3.9999958446818398 3.9999958446818398 3.9999958446818398 3.9999958446818398 3.9999958446818398 3.9999958446818398 3.9999958446818398 3.9999958446818398 3.9999958446818398 3.9999958446818398
```

Sample Input 2:
```
def f(x): 
    n = len(x)
    p = 1
    q = 10
    t = sum((p-x[2*i])**2+q*(x[2*i+1]-x[2*i]**2)**2 for i in range(n//2))
    return t if n % 2 == 0 else (t + x[n-1]**2)
tol = 0.00001
initial = (0.,) * 40
```
Sample Output 2:
```
0.9999998393899576 0.9999997350036939 0.9999998393713422 0.9999997350132265 0.9999998771797968 0.999999714687888 0.9999998771237618 0.9999997147234567 0.9999998622140015 0.9999997229255297 0.9999998182454602 0.9999997460636384 0.9999998378558655 0.999999735806783 0.9999995198800534 0.9999990628587145 0.9999995375050681 0.9999990531378934 0.9999995379314592 0.9999990529016716 0.9999995571056811 0.9999990457043434 0.9999995296499421 0.9999990272278173 0.9999998680013452 0.9999997178388732 0.9999995349520188 0.9999990248662819 0.9999995654389255 0.9999990308741271 0.9999992715671752 0.9999984019972741 0.9999991866507559 0.9999984524848595 0.999999271845083 0.9999982780253368 0.999999183044506 0.9999983210294597 0.9999992166722037 0.9999983042208087
```

