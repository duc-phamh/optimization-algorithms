# Golden ratio method

Algorithm description: https://en.wikipedia.org/wiki/Golden-section_search


---


**Problem:** Minimize the function `f()` on the interval `[a,b]` with precision at least `tol` using the golden ratio (a special variant of ternary search) method. You should assume that variables `f,a,b` are already defined. You need to output the point of the minimum of the function using the standard `print` statement. **Make sure you perform only one function call at each iteration!**


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
