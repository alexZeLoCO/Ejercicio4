a = 10      #Valor entero cualsea en variable a
b = 3       #Valor entero cualsea en variable b

c = (5<=a<=30 and b%2!=0)       #Valor booleano en c. Condición: Si a es mayor o igual a 5, menor o igual a 30 e impar.
d = (not (5<=a<=30) and not (b%2!=0))       #Valor booleano en d. Condición: Si a NO es mayor o igual a 5, menor o igual a 30 y NO es impar.

print (c)       #Imprimir c. Con los valores propuestos (10 y 3) sería true.
print (d)       #Imprimir d. Con los valores propuestos (10 y 3) sería false.

#SUGERENCIA: MODIFICAR DATOS Y EXPERIMENTAR CON VARIACIÓN DE c Y d.