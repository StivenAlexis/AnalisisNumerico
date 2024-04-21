

def metodoBiseccion(f,raizInf, raizSup, error):
    resultadoList=[]
    raizInfList=[]
    raizSupList=[]
    errorGradualList=[]
    error=(error/100)

    errorGradual=(raizSup-raizInf)/2
    resultado=(raizInf+raizSup)/2
    resultadoList.append(resultado)
    raizInfList.append(raizInf)
    raizSupList.append(raizSup)
    errorGradualList.append(errorGradual)
    
    
    while abs(errorGradual) > error:
        resultado=(raizInf+raizSup)/2
        fr=f(resultado)
        fri=f(raizInf)
        frs=f(raizSup)
        
    
        if fr> 0 and fri> 0 or fr < 0 and fri < 0:
            raizInf = resultado
        else:
            raizSup = resultado

        errorGradual=abs((raizInf-raizSup)/2)

        resultadoList.append(resultado)
        raizInfList.append(raizInf)
        raizSupList.append(raizSup)
        errorGradualList.append(errorGradual)
        

    for i in range(len(resultadoList)):
        print("Iteración", i+1)
        print("Resultado: ", resultadoList[i])
        print("Raiz inferior: ", raizInfList[i])
        print("Raiz superior: ", raizSupList[i])
        print("Error gradual: ", errorGradualList[i])
        print()

def f(x):

    return 5 * x**3 - 5 * x**2 + 6 * x - 2

raizInf = 0
raizSup = 1
error = 10

metodoBiseccion(f, raizInf, raizSup, error)




    

