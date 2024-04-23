import numpy as np  # Import NumPy library

def funcionquetengo(x):
    return np.log(x**2)-0.7

def metodoFalsaPosicion(extremo_inferior, extremo_superior):
  valor= extremo_superior-(funcionquetengo(extremo_superior)*(extremo_superior-extremo_inferior))/(funcionquetengo(extremo_superior)-funcionquetengo(extremo_inferior))
  return valor

extremo_inferior = 0.5
extremo_superior = 2


resultado= metodoFalsaPosicion(extremo_superior,extremo_inferior)

print("Resultado",resultado)

