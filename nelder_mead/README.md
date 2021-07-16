# Nelder-Mead algorithm

Algorithm description: https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method

---

**Problem:** You are to use Nelder—Mead algorithm to find an optimal vector of weights for the SVM linear classifier that perfectly classifies the given set of objects. The object descriptions (vectors of numbers) are provided in an array `x`, in which every row corresponds to an object, and columns correspond to vector components. The classes (-1 and +1) for each of the objects are provided in a separate array `y`. You are to output space-separated sequence of the weights $a_1\quad\ldots\quad a_m\quad b$ such that function $f(x_1,\ldots,x_m)=\mathrm{sign}(a_1x_1+\ldots+a_mx_m+b)$ perfectly classifies the provided objects.


---



Sample Input:
```
x = [
    [0.1, 0.5, 3.0],
    [1.0, -1.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.1, 0.5, 1.0]
]
y = [1, 1, -1, 1]
```
Sample Output:
```
3.0 -1.0 1.0 0.0
````
