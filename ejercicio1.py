def metodoBiseccion(funcion,raizInf, raizSup, error):
    funcion= x
    x = (raizInf + raizSup)/2
    while (raizInf - raizSup) > error:
        if f(x) == 0:
            break
        elif f(raizInf)*f(x) < 0:
            raizSup = x
        else:
            raizInf = x
        x = (raizInf + raizSup)/2
    return x


def metodoNewtonRaphson(){
    x = float(input("Ingrese el valor de x: "))
    error = float(input("Ingrese el valor de error: "))
    while abs(f(x)) > error:
        x = x - f(x)/df(x)
    
}





