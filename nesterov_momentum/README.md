# Nesterov momentum (NAG)

Algorithm description: https://dominikschmidt.xyz/nesterov-momentum/

---

You are to solve a system of linear equations $Ax=b$ by solving a corresponding optimization problem $(A\mathbf{x}-\mathbf{b})^\mathsf{T}(A\mathbf{x}-\mathbf{b})\to\min(Ax−b)$ That is, you are given the matrix _A_ and vector _b_

<p align="center">
$A=\begin{pmatrix}a_{1,1}\dots a_{1,n}\\\vdots\\a_{n,1}\dots a_{n,n} \end{pmatrix}$
</p>
<p align="center">
$b=\begin{pmatrix}b_1,\dots,b_n\end{pmatrix}$ 
</p>

and you are to minimize the function 


<p align="center"> $f(x_1,\dots,x_n)=\sum_{i=1}^n{(a_{i,1}x_1+a_{i,2}x_2+\dots+a_{i,n}x_n-b_i)^2}$ </p>

 
Note that partial derivatives of the function are computed with

<p align="center"> $\frac{\partial f}{\partial x_k}(t_1,\dots,t_n)=2\sum_{i=1}^{n}{a_{i,k}(a_{i,1}t_1+a_{i,2}t_2+\dots+a_{i,n}t_n-b_i)}$ </p>

The tolerance parameter in this problem is the maximal value of the function you should achieve, i.e. if `tol=0.001`, you should output such values of $(x_1,\dots,x_n)$ for which $f(x_1,\dots,x_n) < 0.001$



---



Sample Input:
```
A = [[0.99, 0.87, 0.51, 0.27], [0.34, 0.22, 0.28, 0.34], [0.86, 0.16, 0.14, 0.76], [0.74, 0.36, 0.34, 0.67]]
b = [0.22, 0.56, 0.12, 0.32]
tol = 0.001
```
Sample Output:
```
1.9250001434580333 -4.800059678539262 6.003006880246984 -2.115673076371321
```
