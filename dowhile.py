
# Para el bucle Do While, deberás crear la misma estructura que en el While, pero solo se debe ejecutar una vez.


# Por último, para el Switch, deberás crear la variable estacion, y distintos case para las cuatro estaciones del año. Dependiendo del valor de la variable 
# estacion se deberá mandar un mensaje por consola informando de la estación en la que está. También habrá que poner un default para cuando el valor de la variable no sea una estación.



doWhile = int(input('Introduzca un numero : ') ) 
while True : 
    doWhile += 1 
    if doWhile > 0 : 
        print('Bucle Do While Positivo : ' + str(doWhile))
        break
    elif doWhile == 0 :
        print('Bucle do while neutro : ' + str(doWhile))
        break
    else: 
        print('Bucle do while negativo :' + str(doWhile))
        break
    
    

