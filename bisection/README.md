# Bisection method

Algorithm description: https://en.wikipedia.org/wiki/Bisection_method

---

**Problem:** Find the root of the function `f()` on the interval `[a,b]` with precision at least `tol` using the bisection method. You should assume that variables `f,a,b` are already defined. You need to output the root of the function using the standard print statement.


---

Sample Input 1:
```
from math import sin
a = 3.
b = 4.
tol = 0.00001
f = sin
```

Sample Output 1:
```
3.141590118408203
```


---


Sample Input 2:
```
from math import tan
a = -1.
b = 1.
tol = 0.00001
f = tan
```
Sample Output 2:
```
-3.814697265625e-06
```


---


Sample Input 3:
```
from math import sqrt, sin
a = .01
b = 1.
tol = 0.00001
f = lambda x: sqrt(x)-2*sin(x)
```
Sample Output 3:
```
0.2555097579956055
```
