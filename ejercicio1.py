import numpy as np
import matplotlib.pyplot as plt

def metodoBiseccion(f,raizInf, raizSup, error):
    resultadoList=[]
    raizInfList=[]
    raizSupList=[]
    errorAbsList=[]
    errorPorcentualList=[]
    fxrList=[]
    fxiList=[]
    fxlList=[]

    
    
    
    errorPorcentual=(abs((raizInf-raizSup)/(raizInf+raizSup)*100))
    errorAbs=(raizSup-raizInf)/2
    resultado=(raizInf+raizSup)/2
    
    
    while abs(errorPorcentual) > error:
        resultado=(raizInf+raizSup)/2
        errorPorcentual=(((raizInf-raizSup)/(raizInf+raizSup)*100))
        
        fxr=f(resultado)
        fxl=f(raizInf)
        fxi=f(raizSup)
        
    
    
        if fxr> 0 and fxl> 0 or fxr < 0 and fxl < 0:
            raizInf = resultado
        else:
            raizSup = resultado

        errorAbs=abs((raizInf-raizSup)/2)

        resultadoList.append(resultado)
        raizInfList.append(raizInf)
        raizSupList.append(raizSup)
        errorAbsList.append(errorAbs)
        errorPorcentualList.append(errorPorcentual)
        fxrList.append(fxr)
        fxiList.append(fxi)
        fxlList.append(fxl)

    
    x_vals = np.linspace(-1, 2, 400)  
    plt.plot(x_vals, f(x_vals), label='f(x)')
    
    plt.plot(resultadoList[-1], 0, 'bo', label=f'Raíz encontrada: x={resultadoList[-1]:.4f}')
    plt.axhline(0, color='black', linewidth=0.5)  
    plt.title('Método de Bisección')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)  

    for i in range(len(resultadoList)):
        print("Iteración", i+1)
        print("Resultado: ", resultadoList[i])
        print("Raiz inferior: ", raizInfList[i])
        print("Raiz superior: ", raizSupList[i])
        print("Error Absoluto: ", errorAbsList[i])
        print("Error Porcentual: ", errorPorcentualList[i])
        print("f(xr): ", fxrList[i])
        print("f(xl): ", fxlList[i])
        print("f(xi): ", fxiList[i])
        print()


def f(x):

    return 5 * x**3 - 5 * x**2 + 6 * x - 2

raizInf = 0
raizSup = 1
error = 10

metodoBiseccion(f, raizInf, raizSup, error)

plt.show()





    

