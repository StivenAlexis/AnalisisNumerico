import numpy as np  # Import NumPy library

def funcionquetengo(x):
    return (np.log(x**2)-0.7)

def metodoFalsaPosicion(extremo_inferior, extremo_superior,cantidad_iteraciones):
  for i in range(cantidad_iteraciones):
    print("Iteracion numero",i+1)
    valor_f_xr=extremo_superior-((funcionquetengo(extremo_superior)*(extremo_inferior-extremo_superior))/funcionquetengo(extremo_inferior)-funcionquetengo(extremo_superior))
    print("valor de xr",valor_f_xr,"Valor de la funcion en xr",funcionquetengo(valor_f_xr))
    if funcionquetengo(valor_f_xr)*funcionquetengo(extremo_inferior)<0:
      print("Se cumple la condicion de que xr evaluada en la funcion * extremo inferior evaluado en la funcion <0")
    if i>0:
      print("Se puede calcular el Error Absoluto y Error Relativo")
      print("Error Absoluto",abs(extremo_superior-valor_f_xr))
      print("Error Relativo",(abs(extremo_superior-valor_f_xr)/valor_f_xr)*100)
      print("\n")
  #Siguiente Iteracion se actualiza
    extremo_superior=valor_f_xr

extremo_inferior = 0.5
extremo_superior = 2
cantidad_iteraciones=50

metodoFalsaPosicion(extremo_inferior,extremo_superior,cantidad_iteraciones)



