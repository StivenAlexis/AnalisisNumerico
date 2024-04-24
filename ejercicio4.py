import sympy as sp

x= sp.symbols('x')

def metodoNewtonRaphson(f,errorlim,x0):
    
    fDerivada = sp.diff(f,x)
    fDerivadaSegunda= sp.diff(fDerivada, x)
    
   
   
    if f>0 and fDerivadaSegunda>0 or f<0 and fDerivadaSegunda<0:
        x1= x0 -( f(x0)/fDerivada)
        errorAbsoluto= x0-x1
        errorRelativo= errorAbsoluto/x0
        errorPorcentual= errorRelativo*100
        print
        print("El error absoluto es",errorAbsoluto)
        print("El error relativo es", errorRelativo)
        print("El error porcentual es", errorPorcentual)
        print("El valor de la raiz es", x1)
        print()
        
        while (abs(errorAbsoluto) > errorlim):
            x0=x1
            x1= x0 -( f(x0)/fDerivada)
            errorAbsoluto= x0-x1



    else:
        print("No se puede resolver por que el signo de sus derivada segunda es diststinta a la funcion en ", x0)
    

def f(x):
    return -x**2+1.8*x+2.5

metodoNewtonRaphson(f(x),0.05,5)

