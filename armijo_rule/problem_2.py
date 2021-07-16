def f(x1, x2): 
    p = 4
    q = 5
    return (p-x1)**2+q*(x2-x1**2)**2
tol = 0.00001
initial = (10., 0.)

def gradient(x1, x2, tol):
    fx1x2 = f(x1, x2)
    return ((f(x1 + tol, x2) - fx1x2)/tol, (f(x1, x2 + tol) - fx1x2)/tol)

def sqrnorm(x):
    return sum(t**2 for t in x)

def armijo(f, grad_approx, x1, x2, c, alpha):
    return (
        f(x1 - alpha*grad_approx[0], x2 - alpha*grad_approx[1]) 
        <= 
        f(x1, x2) - c * alpha * sqrnorm(grad_approx)
    )

def optimizer(f, initial, tol, max_iter, c):
  max_iter = 0
  c = 0.0001
  x1, x2 = initial
  for i in range(50000):
      
      ###
      # Possible improvement for gradient: use tol = min(tol**3, avg_alpha)
      # This is because when alpha gets too small and tol is still high,
      # the gradient will not be applicable.
      ### 
      grad_approx = gradient(x1, x2, tol**2)

      # Find the optimal alpha by Armijo rule
      alpha = 1
      while armijo(f, grad_approx, x1, x2, c, alpha*1.5):
          alpha *= 1.5

      max_iter_armijo = 100
      cur_iter_armijo = 0
      while not armijo(f, grad_approx, x1, x2, c, alpha):
          alpha *= 0.5
          cur_iter_armijo += 1
          if cur_iter_armijo > max_iter_armijo:
            return (x1, x2)

      # Update the variables by the alpha obtained above
      x1 = x1 - alpha * grad_approx[0]
      x2 = x2 - alpha * grad_approx[1]
  return (x1, x2)

result = optimizer(f, initial, tol, max_iter=10, c=0.7)
print(" ".join([str(x) for x in result]))
