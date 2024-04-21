import numpy as np  # Import NumPy library

def g(x):
  return np.log(x**2) - 0.7  # Difference between f(x) and 0.7

def falsa_posicion(a, b, tol=1e-6, max_iter=100):
  for i in range(max_iter):
    if abs(g(b)) < tol:
      return b
    x_r = b - ((g(b) * (b - a)) / (g(b) - g(a)))
    if g(a) * g(x_r) < 0:
      b = x_r
    else:
      a = x_r
  raise Exception("No se pudo encontrar la raíz en el número máximo de iteraciones")

# Define f(x) using NumPy for clarity (not strictly necessary)
def f(x):
  return np.log(x**2)

# Values for initial guess
a = 1.5
b = 2

# Find the root
raiz = falsa_posicion(a, b)

# Print the result
print("Raíz:", raiz)

print("LOL")

prtin("lucas feo")

