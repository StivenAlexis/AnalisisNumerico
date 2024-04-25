import sympy as sp

x= sp.symbols('x')

def metodoNewtonRaphson(f,errorlim,x0):
    print ("**********Metodo De Newton-Raphson**********")
    fDerivada = sp.diff(f, x)
    fDerivadaSegunda = sp.diff(fDerivada, x)

    f = sp.lambdify(x, f) 
    df = sp.lambdify(x, fDerivada)
   

    if f(x0)>0 and fDerivadaSegunda>0 or f(x0)<0 and fDerivadaSegunda<0:
        iter=1
        x1= x0 -( f(x0)/df(x0))
        errorAbsoluto= x0-x1
        errorRelativo= errorAbsoluto/x0
        errorPorcentual= errorRelativo*100
        print("iteracion: ", iter)
        print("x0= ", x0)
        print("x1", x1)
        print("f(x0)= ", f(x0))
        print("f'(x0)= ", df(x0))
        print("El error absoluto es",errorAbsoluto)
        print("El error relativo es", errorRelativo)
        print("El error porcentual es", errorPorcentual)
        print()

        while errorAbsoluto > errorlim:
            iter+=1
            x0=x1
            x1= x0 -( f(x0)/df(x0))
            errorAbsoluto= abs(x0-x1)
            errorRelativo= errorAbsoluto/x0;
            errorPorcentual= errorRelativo*100
            print("iteracion: ", iter)
            print("x0= ", x0)
            print("f(x0)= ", f(x0))
            print("f'(x0)= ", df(x0))
            print("El error absoluto es",errorAbsoluto)
            print("El error relativo es", errorRelativo)
            print("El error porcentual es", errorPorcentual)
            print("x1", x1)
            print()
    else:
        print("No se puede resolver por que el signo de sus derivada segunda es diststinta a la funcion en ", x0)

def secante(f,xi_1,xi,tol,n=10):
    print ("**********Metodo De La Secante**********")
    for k in range(1,n):
          xr= xi-(f(xi)*(xi_1-xi))/(f(xi_1)-f(xi))
          e_abs= abs(xr-xi)
          e_rel= (e_abs/xr)
          e_aprox= e_rel*100
          
          print ("Iteracion número" ,k)
          print ("Error aproximado " ,e_aprox)
          print ("El error absoluto es",e_abs) 
          print ("El error relativo es",e_rel)
          print ("El valor de la raiz es",xr)
          print ("------------------------------------------------")

          if e_aprox <=tol:
               break
          xi_1=xi
          xi=xr



def f(x):
    return -x**2+1.8*x+2.5

def g(x):
    return -x**2 + 1.8*x + 2.5

metodoNewtonRaphson(f(x),0.05,5)

#Teniendo en cuenta el método de Newton-Raphson las dos primeras iteraciones nos dan el valor de xi-1(5) y de xi(3.353658537) para poder resolver el método de iteración de la secante")
secante(g,5,3.353658537,0.05)    


