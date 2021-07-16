# Newton's method in optimization

Algorithm description:
* Formal explanation: https://en.wikipedia.org/wiki/Newton%27s_method_in_optimization
* How I learned it: https://www.youtube.com/watch?v=-5e2cULI3H8



---


**Problem:** Minimize the function `f()` on the interval `[a,b]` with precision at least `tol` using Newton’s method. You should assume that variables `f,a,b` are already defined. You need to output the point of the minimum of the function using the standard `print` statement.

---

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


---


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
