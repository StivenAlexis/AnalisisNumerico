import numpy as np 
import matplotlib.pyplot as plt

def funcionquetengo(x):
    return (np.log(x**2)-0.7)

def metodoFalsaPosicion(extremo_inferior, extremo_superior,cantidad_iteraciones):
  valores_xr=[]
  for i in range(cantidad_iteraciones):
    print("\n")
    print("Iteracion numero",i+1)
    print("Extremo Inferior",extremo_inferior,"f(xl) evaluada en el punto inferior",funcionquetengo(extremo_inferior))
    print("Extremo Superior",extremo_superior,"f(xu) evaluada en el punto superior",funcionquetengo(extremo_superior))
    valor_f_xr=extremo_superior-((funcionquetengo(extremo_superior)*(extremo_inferior-extremo_superior))/funcionquetengo(extremo_inferior)-funcionquetengo(extremo_superior))
    valores_xr.append(valor_f_xr)
    print("valor de xr",valor_f_xr,"Valor de la funcion en xr",funcionquetengo(valor_f_xr))
    if i>0:
      print("Se puede calcular el Error Absoluto y Error Relativo")
      print("Error Absoluto",abs(extremo_superior-valor_f_xr))
      print("Error Relativo",(abs(extremo_superior-valor_f_xr)/valor_f_xr)*100)
      
    if funcionquetengo(valor_f_xr)*funcionquetengo(extremo_inferior)<0:
      print("Se cumple la condicion de que xr evaluada en la funcion * extremo inferior evaluado en la funcion <0")
      extremo_superior=valor_f_xr
    if funcionquetengo(valor_f_xr)*funcionquetengo(extremo_inferior)>0:
      print("Se cumple la condicion de que xr evaluada en la funcion * extremo inferior evaluado en la funcion >0")
      extremo_inferior=valor_f_xr
    if funcionquetengo(valor_f_xr)*funcionquetengo(extremo_inferior)==0:
      print("Se encontro la raiz")
    if i+1==cantidad_iteraciones:
# Graficar la función
      x = np.linspace(-5, 20, 100)
      y = funcionquetengo(x)
      plt.plot(x, y, label='funcionquetengo(x)')
    
      # Resaltar el último xr encontrado
      plt.scatter(valores_xr[-1], funcionquetengo(valores_xr[-1]), color='red', label='Último xr encontrado')
    
      plt.xlabel('x')
      plt.ylabel('funcionquetengo(x)')
      plt.title('Gráfico de la función funcionquetengo(x)')
      plt.legend()
      plt.grid(True)
      plt.show() 

extremo_inferior = 0.5
extremo_superior = 2
cantidad_iteraciones=3

metodoFalsaPosicion(extremo_inferior,extremo_superior,cantidad_iteraciones)



