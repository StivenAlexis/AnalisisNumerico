#Metodo de iteracion de punto fijo 
import math

def g(x):
    return math.atan(x)+math.pi

def metodoDePuntoFijo(x0,errorLim):
    xr=x0
    iter=0
    while True:
        xi=xr
        xr=g(xi)
        iter += 1
        if xr!=0:
            errorAproximado=abs(((xr-xi)/xr)*100)
            errorAbsoluto=abs(xr-xi)
            errorRelativo=(errorAbsoluto/xr)
        else:
            errorRelativo=0
        #print ("Iteracion:", iter)
        print ("El error aproximado es",errorAproximado) 
        print ("El error absoluto es",errorAbsoluto) 
        print ("El error relativo es",errorRelativo)
        print ("El valor de la raiz es",xr)
        print ("------------------------------------------------")
        if errorAproximado < errorLim :
            break

    return xr

metodoDePuntoFijo(4.5,0.001)