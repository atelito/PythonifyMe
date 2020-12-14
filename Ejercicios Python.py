#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""2. Ingresar un arreglo de 10 componentes.
a) Imprimir la cuarta componente.
b) Imprimir las componentes en orden invertida.
c) Imprimir el producto entre la primera y la última componente.
d) Imprimir las componentes de índice impar.
e) Imprimir la suma de las componentes de índice par.
f) Imprimir la multiplicación de las componentes de índice impar.
g) Imprimir el arreglo que resulta de intercambiar la primera con la última
componente.

from operator import attrgetter
arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a
print('#a', arreglo[3])
# b
print('#b')
for i in reversed(arreglo):
    print(i)
# c
print('#c', arreglo[0]*arreglo[-1])
# d
for i in arreglo:
    if i % 2 == 1:
        print(i)

# e
sum = 0
for i in arreglo:
    if i % 2 == 0:
        sum += i
print('#e', sum)

# f
prod = 1
for i in arreglo:
    if i % 2 == 1:
        prod *= i
print('#f', prod)

# g
print('#g')
var = 0
var = arreglo[0]
arreglo[0] = arreglo[-1]
arreglo[-1] = var
for i in arreglo:
    print(i)


4. Generar un arreglo P con los 15 primeros números primos. Mostrarlo

def factorial(n):
    res = 0
    if (n == 1):
        return 1
    else:
        res = n * factorial(n - 1)
    return res

P = []
for i in range(0, 15, 1):
    resultado = factorial((i+2)-1)
    if (((resultado+1) % (i+2)) == 0):
        P.append(i)
print(P)

5. Dado un arreglo, imprimir los valores máximo y mínimo.

arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max = 0
min = max
for i in range(0, len(arreglo)):
    if arreglo[i] > max:
        max = arreglo[i]
    elif arreglo[i] < min:
        min = arreglo[i]
print('El maximo es ', max, ' y el minimo es ', min)


6. Dado un arreglo imprimir el lugar que ocupa el mínimo. Tener en cuenta que este
valor puede estar repetido, en ese caso imprimir todos los lugares donde aparece este
valor.

arreglo = [10, 2, 30, 4, 50, 6, 70, 8, 90, 2, 10]
max = 0
min = 999
pos_max = 0
pos_min = 0
for i in range(0, len(arreglo)):
    if arreglo[i] > max:
        pos_max = i+1
        max = arreglo[i]
    elif arreglo[i] < min:
        pos_min = i+1
        min = arreglo[i]
for i in range(0, len(arreglo)):
    if min == arreglo[i]:
        print('el minimo es ', min, ' y esta en la posicion ', i)
#print('El maximo es ', max, ' y esta en la posicion ', pos_max, ' y el minimo es ', min, ' y esta en la posicion ', pos_min)

7. Revertir un arreglo de 16 componentes sobre él mismo, es decir, poner el primer
elemento en el último lugar y el último en el primer lugar, el segundo en el penúltimo y
este en el segundo, etc. Decir si el arreglo es capicúa

arreglo = [11, 2, 30, 4, 50, 6, 70, 8, 90, 2, 10]
arreglo_invertido = []
aux = 0
for i in range(len(arreglo)-1, -1, -1):
    aux = arreglo[i]
    arreglo_invertido.append(aux)
print(arreglo_invertido)

8. Se pide cargar en memoria un arreglo de N posiciones. Se pide generar un programa
que emita un ranking con los 10 números más grandes.

from random import randint

arreglo = []
arr_num_grandes = []
n = randint(11,20)

for i in range(0, n):
    aleatorio = randint(0,100)
    arreglo.append(aleatorio)

print(arreglo)
arreglo.sort(reverse=True)

for i in range(0, 10):
    arr_num_grandes.append(arreglo [i])

print(arr_num_grandes)

9. Cargar dos arreglos de enteros de N y M posiciones. Se pide generar un programa
que produzca la intersección entre los dos arreglo s.

from random import randint

arreglo_N = []
arreglo_M = []
interseccion = []
N = randint(5,20)
M = randint(5,20)
for i in range(0, N):
    arreglo_N.append(randint(0,20))
for i in range(0, M):
    arreglo_M.append(randint(0,20))

print(arreglo_N)
print(arreglo_M)

for numero_N in arreglo_N:
    for numero_M in arreglo_M:
        if numero_N == numero_M:
            interseccion.append(numero_M)

print(interseccion)

10. Dado un arreglo de n elementos, calcular e imprimir el menor de los múltiplos de 5
y el mayor de los múltiplos de 10. Determinar la posición de cada uno de ellos.

from random import randint

arreglo = []
for i in range(0, randint(20,100)):
    arreglo.append(randint(0,100))
print(arreglo)

max = 0
min = 101
pos_max = 0
pos_min = 0
for i in range(0, len(arreglo)):
    if arreglo[i] > max and arreglo[i] % 10 == 0:
        pos_max = i+1
        max = arreglo[i]
    elif arreglo[i] < min and arreglo[i] % 5 == 0:
        pos_min = i+1
        min = arreglo[i]
print('el minimo multiplo de 5 es', min, ' y esta en la posicion', arreglo.index(min))
print('el maximo multiplo de 10 es', max, ' y esta en la posicion', arreglo.index(max))

11. Se dan 20 valores correspondientes a las estaturas de los alumnos de un curso A y 20
de un curso B. Hallar:
    a) Estatura máxima del curso A y del curso B y el lugar que ocupa alumno en
    la lista.
    b) Comparar ambas estaturas e indicar cuál es la mayor imprimiendo un
    mensaje.

from random import random, randint

arreglo_A = []
arreglo_B = []
for i in range(0, 20):
    arreglo_A.append(round(random()*100, 2))
    arreglo_B.append(round(random()*100, 2))

print(arreglo_A)
print(arreglo_B)

print('La estatura maxima del curso A es', max(arreglo_A),
      'y esta en la posicion', arreglo_A.index(max(arreglo_A))+1)
print('La estatura maxima del curso A es', max(arreglo_B),
      'y esta en la posicion', arreglo_B.index(max(arreglo_B))+1)
if max(arreglo_A) > max(arreglo_B):
    print('El curso A tiene mayor estatura')
else:
    print('El curso B tiene mayor estatura')


14. Diseñar con funciones el siguiente programa:

a) Se carga A con 10 números pares y B con 10 números múltiplos de 5.
b) Cargar el arreglo C con la suma de cada elemento de A con cada elemento
de B.
c) Cargar el arreglo D con los todos los elementos de A y a continuación todos
los elementos de B.
d) Invertir el arreglo A sobre sí mismo.
e) Buscar la posición del máximo de B. Mostrar la posición del máximo y el
valor del máximo. Poner en cero los valores a la derecha del máximo.
f) Encontrar el promedio de C. Contar cuántos valores hay en C por encima
de ese promedio.

from random import random, randint

#a
def carga_arreglo(dimension, tipo):
    arreglo = []
    # print(len(arreglo))
    if tipo == '2':
        while len(arreglo) < dimension:
            numero = randint(20, 100)
            if numero % 2 == 0:
                arreglo.append(numero)
    elif tipo == '5':
        while len(arreglo) < dimension:
            numero = randint(20, 100)
            if numero % 5 == 0:
                arreglo.append(numero)
    else:
        while len(arreglo) < dimension:
            arreglo.append(randint(20, 100))
    return arreglo

A = carga_arreglo(10, '2')
B = carga_arreglo(10, '5')
print('A:', A)
print('B:', B)
#b
C = []
for i in range(0, len(A)):
    C.append(A[i]+B[i])
print('C:', C)
#c
D = A + B
print('D:', D) #A.extend(B)
#d
A.reverse()
print('A:', A)
#e
print('La posicion del maximo de B es:' , B.index(max(B))+1 , 'y es el numero' , max(B))
for i in range(B.index(max(B))+1, len(B)):
    B[i] = 0
print('B:', B)
#f
promedio = contador = 0
for i in range(0, len(C)):
    promedio = 0
    for num in C:
        promedio += (num/len(C))
    if promedio < C[i]:
        contador += 1
print('El promedio de C es:', round(promedio, 2), 'y hay ', contador, 'numeros por encima del promedio')

15. Leer 15 números y generar un arreglo con los primeros 8 números mayores que 20. Si
no hay 8 números que cumplan la condición, repetir el primero hasta completar el vector.
Si ningún número era mayor que 20, mostrar mensaje y salir.
a) Calcular el promedio de los números que no entraron en el vector.
b) Buscar el máximo elemento y mostrar el elemento que esté en la posición
anterior.
c) Mostrar el factorial de los elementos de posición par del vector.

from random import random, randint
from math import factorial

def promedio_arreglo(arreglo):
    promedio = 0
    for num in arreglo:
        promedio += num/len(arreglo)
    return promedio    

def carga_arreglo(cant_num_aleatorios, cant_num_vector, num_a_evaluar):
    arreglo = []
    arreglo_menores = []
    while len(arreglo) < cant_num_vector:
        contador = 0
        while contador < cant_num_aleatorios:     #len(arreglo) < cant_num_vector
            numero = randint(0, 40)
            if len(arreglo) < cant_num_vector and numero > num_a_evaluar:
                arreglo.append(numero)
            else:
                arreglo_menores.append(numero) 
            contador += 1
        if len(arreglo) == 0:
            print('No se generaron numeros mayores a', num_a_evaluar)
    contador = 0
    prom_num_menores = promedio_arreglo(arreglo_menores)
    #print(arreglo_menores)
    print('El promedio de los numeros que no entraron en el vector es:', round(prom_num_menores,2))
    print('El numero mas grande es:', max(arreglo), 'y el elemento que esta en la posicion anterior es:', arreglo[arreglo.index(max(arreglo))-1] )
    for i in range(0, len(arreglo)):
        if i % 2 == 1:
            print('El factorial de', arreglo[i], 'es: ', factorial(arreglo[i]))
    print(arreglo)
    return arreglo

A = carga_arreglo(15, 8, 20)

16. Ingresar números hasta cargar un arreglo de 10 elementos de la siguiente manera: 5
positivos y 5 negativos en ese orden.
    a) El promedio de los números negativos.
    b) Ordenar el arreglo de menor a mayor.
    c) Generar otro arreglo con los múltiplos de 4. Si no los hubiese mostrar
    cartel aclaratorio.
    d) Mostrar cuántos pares y cuántos múltiplos de 3 hay.

from random import random, randint


def promedio_arreglo_neg(arreglo):
    promedio = 0
    for num in arreglo:
        if num < 0:
            promedio += num/len(arreglo)
    return round(promedio, 2)


def carga_arreglo(cant_num_vector):
    arreglo = []
    contador_pos = 0
    contador_neg = 5
    while len(arreglo) < cant_num_vector:
        numero = randint(-100, 100)
        if numero > 0 and contador_pos < 5:
            arreglo.insert(contador_pos, numero)
            contador_pos += 1
        elif numero < 0 and contador_neg < cant_num_vector:
            arreglo.insert(contador_neg, numero)
            contador_neg += 1
    print(arreglo)
    return arreglo


A = carga_arreglo(10)
# a
print('Promedio de numeros negativos:', promedio_arreglo_neg(A))
# b
print('Arreglo ordenado: ', sorted(A))
# c


def arreglo_mult_4(arreglo):
    arreglo_mult_4 = []
    for num in arreglo:
        if num % 4 == 0:
            arreglo_mult_4.append(num)
    if len(arreglo_mult_4) == 0:
        print('No tiene multiplos de 4')
    return arreglo_mult_4


print('Arreglo con multiplos de 4:', arreglo_mult_4(A))
#d
def contador(arreglo):
    pares = mult3 = 0
    for num in arreglo:
        if num % 2 == 0:
            pares += 1
        elif num % 3 == 0:
            mult3 += 1
    print('Tiene', pares, 'numeros pares y', mult3, 'numeros multiplos de 3')

contador(A)

18. Cargar un arreglo A de números enteros con los números que sean pares entre los
primeros 15 ingresados. Mostrarlo.Generar un segundo arreglo B con los elementos de A que sean
menores que el promedio de A. Mostrarlo.Desplazar el arreglo A desde la posición donde se encuentre
el primer número mayor al promedio una posición hacia atrás. Mostrarlo.
Datos ingresados:16,64,2,1,11,1,5,6,6,10,4,14,7,8,33
Arreglo A = [16, 64, 2, 6, 6, 10, 4 14, 8]
Promedio=14,44
Arreglo B
2 6 6 10 4 14 8
Arreglo A

from random import random, randint

def numero_par(min, max):
    num_par = 0
    if max < min:
        aux = min
        min = max
        max = aux
    while num_par == 0:
        numero = randint(min, max)
        if numero % 2 == 0:
            num_par = numero
    return num_par

def numero_impar(min, max):
    num_par = 0
    if max < min:
        aux = min
        min = max
        max = aux
    while num_par == 0:
        numero = randint(min, max)
        if numero % 2 != 0:
            num_par = numero
    return num_par

def carga_arreglo_par(cant_num_vector, min, max):
    arreglo = []
    while len(arreglo) < cant_num_vector:
        arreglo.append(numero_par(min, max))
    return arreglo

def carga_arreglo_prom(arreglo):
    arreglo_min_prom = []
    for num in arreglo:
        if num < promedio_arreglo(arreglo):
            arreglo_min_prom.append(num)
    return arreglo_min_prom

def carga_arreglo(cant_num_vector):
    arreglo = []
    while len(arreglo) < cant_num_vector:
        numero = randint(0, 100)
        arreglo.append(numero)
    return arreglo

def promedio_arreglo(arreglo):
    promedio = 0
    for num in arreglo:
        promedio += num/len(arreglo)
    return round(promedio, 2)    

def desplazar_arreglo_prom(arreglo):
    for i in range(0, len(arreglo)):
        if arreglo[i] > promedio_arreglo(arreglo):
            arreglo.pop(i-1)
            break
    return arreglo

A = carga_arreglo_par(15, -100, 200)
print('Arreglo A:', A)
print('El promedio del arreglo es:', promedio_arreglo(A))
B = carga_arreglo_prom(A)
print('Arreglo numeros menores al promedio:',B)
C = desplazar_arreglo_prom(A)
print(C)

19. Ingresar 12 números, cargar un vector, calcular y mostrar:
    a) El máximo de los números múltiplos de 2 y su posición.
    b) El mínimo de los números impares y su posición.

    

from random import randint

def promedio_arreglo(arreglo):
    promedio = 0
    for num in arreglo:
        promedio += num/len(arreglo)
    return round(promedio, 2)    

def carga_arreglo(cant_num_vector):
    arreglo = []
    while len(arreglo) < cant_num_vector:
        numero = randint(0, 100)
        arreglo.append(numero)
    return arreglo

def es_par(num):
    if num % 2 == 0:
        return True
    return False

def es_impar(num):
    if num % 2 != 0:
        return True
    return False

def numero_impar(min, max):
    num_par = 0
    if max < min:
        aux = min
        min = max
        max = aux
    while num_par == 0:
        numero = randint(min, max)
        if numero % 2 != 0:
            num_par = numero
    return num_par

def pos_max_par(arreglo):
    num_par_max = 0
    for num in arreglo:
        if es_par(num):
            if num > num_par_max:
                num_par_max = num
    return arreglo.index(num_par_max)+1

def pos_min_impar(arreglo):
    num_impar_min = 101
    for num in arreglo:
        if es_impar(num):
            if num < num_impar_min:
                num_impar_min = num
    return arreglo.index(num_impar_min)+1

A = carga_arreglo(12)
print('Arreglo A:',A)
print('La posicion del maximo numero par en el arreglo es: ', pos_max_par(A))
print('La posicion del minimo numero impar en el arreglo es: ', pos_min_impar(A))

20. Ingresar 10 números, cargar un arreglo donde los números pares estén en las posiciones pares
y los números impares en las posiciones impares.Calcular y mostrar:
    a) El promedio de los números múltiplos de 5 que se encuentren las posiciones impares
    y la suma de las posiciones pares (en una función).
    b) Cuántas veces aparece un número múltiplo de 4 en las posiciones pares
    c) Contar en cuántas parejas de números el primero es menor que el segundo

Ejemplo:Ingresamos:8 3 5 9 15 10 12 14 1 2. Cargamos el vector:8 3 10 5 12 9 14 15 2 1
    a)Promedio: (5+15)/2 Suma=8+10+12+14+2
    b)Sólo 2 veces
    c)4 parejas de números cumplen la condición


from random import randint

def es_par(num):
    if num % 2 == 0:
        return True
    return False

def es_impar(num):
    if num % 2 != 0:
        return True
    return False

def promedio_mult_5_impar(arreglo):
    promedio = contador = 0
    for i in range(0, len(arreglo)):
        if es_impar(i+1) and arreglo[i] % 5 == 0:
            contador += 1
            promedio += arreglo[i]
    if contador != 0:
        return round(promedio/contador, 2)
    return '---'

def promedio_mult_4_cant(arreglo):
    contador = 0
    for i in range(0, len(arreglo)):
        if es_par(i+1) and arreglo[i] % 4 == 0:
            contador += 1
    return contador

def promedio_arreglo(arreglo):
    promedio = 0
    for num in arreglo:
        promedio += num/len(arreglo)
    return round(promedio, 2)    

def carga_arreglo(cant_num_vector):
    arreglo = []
    contador_pos = 0
    contador_neg = 5
    for i in range(0, cant_num_vector):
        while True:
            numero = randint(-100, 100)
            if es_par(numero) and es_par(i+1):
                arreglo.append(numero)
                break
            elif es_impar(numero) and es_impar(i+1):
                arreglo.append(numero)
                break
    print(arreglo)
    return arreglo

def contador(arreglo):
    mayor = 0
    for i in range(0, len(arreglo), 2):
        if arreglo[i] < arreglo[i+1]:
            mayor += 1
    print('Tiene', mayor, 'parejas de números donde el primero es menor que el segundo')

A = carga_arreglo(10)
# a
print('Promedio de numeros multiplos de 5 en posiciones impares:', promedio_mult_5_impar(A))
# b
print('Promedio de numeros multiplos de 4 en posiciones pares:', promedio_mult_4_cant(A))
# c
contador(A)

21. Implementar un algoritmo que, dado un número entero 𝑛, permita calcular su
factorial.

def factorial(n): return n * factorial(n-1) if n > 1 else 1

print(factorial(6))

22. Escribir un programa que le pida una palabra al usuario, para luego imprimirla
1000 veces, en una única línea, con espacios intermedios.
Ayuda: Investigar acerca del parámetro end de la función print.


def palabra_n_veces1(palabra, n):
    for i in range(0, n):
        print(palabra, end=" ")
        
def palabra_n_veces2(palabra, n):
    print((palabra+" ")*n)

palabra_n_veces2('Atel', 1000)


23. Escribir un programa que imprima por pantalla todas las fichas de dominó, de
una por línea y sin repetir.

def imprimir_fichas():
    # imprime fichas de domino
    contador = 0
    for izq in range(0, 7):
        for der in range (0, izq+1):
            print(f'[{izq}] | [{der}]')

imprimir_fichas()


24. Escribir dos funciones que permitan calcular:
    a) La duración en segundos de un intervalo dado en horas, minutos y segundos.
    b) La duración en horas, minutos y segundos de un intervalo dado en segundos.

def seg_a_h_m_s(segundos):
    s = segundos
    h = m = 0
    while s >= 60:
        if (s // 3600) > 0:
            h += 1
            s -= 3600
            if s // 60 > 0:
                m += 1
                s -= 60
        elif (s // 60) > 0:
                m += 1
                s -= 60
    return h, m, s

def h_m_s_a_seg(h, m, s):
    segundos = h *3600 + m * 60 + s
    return segundos

x, y, z = seg_a_h_m_s(4567)
print(f'Horas: {x}, Minutos: {y}, Segundos: {z}')
print('Segundos totales:', h_m_s_a_seg(x, y, z), 'seg.')

25. Usando las funciones del ejercicio anterior, escribir un programa que pida al
usuario dos intervalos expresados en horas, minutos y segundos,
sume sus duraciones, y muestre por pantalla la duración total en horas, minutos y segundos.

def seg_a_h_m_s(segundos):
    s = segundos
    h = m = 0
    while s >= 60:
        if (s // 3600) > 0:
            h += 1
            s -= 3600
            if s // 60 > 0:
                m += 1
                s -= 60
        elif (s // 60) > 0:
                m += 1
                s -= 60
    return h, m, s

def h_m_s_a_seg(h, m, s):
    segundos = h *3600 + m * 60 + s
    return segundos

class Intervalo():
    h = 0
    m = 0
    s = 0

    def pedir_intervalo(self):
        self.h = int(input('Ingrese cantidad de horas: '))
        self.m = int(input('Ingrese cantidad de minutos: '))
        self.s = int(input('Ingrese cantidad de segundos: '))

    def intervalo_seg(un_intervalo, otro_intervalo):
        suma_de_intervalo = (un_intervalo.h + otro_intervalo.h) *3600 + (un_intervalo.m + otro_intervalo.m) * 60 + (un_intervalo.s + otro_intervalo.s)
        return suma_de_intervalo

int_1 = Intervalo()
int_1.pedir_intervalo()
int_2 = Intervalo()
int_2.pedir_intervalo()
intervalo = Intervalo.intervalo_seg(int_1, int_2)
x, y, z = seg_a_h_m_s(intervalo)
print('Duracion total en segundos:', intervalo, 'son --', f'Horas: {x}, Minutos: {y}, Segundos: {z}')

26. Dado un año indicar si es bisiesto.
Nota: un año es bisiesto si es un número divisible por 4
pero no si es divisible por 100,excepto que también sea divisible por 400


def es_bisiesto(anio):
    if not anio % 4:
        if anio % 100 or not anio % 400:
            print('Es bisiesto')
    else:
        print('no es bisiesto')
es_bisiesto(2072)

27. MASTERMIND
Cada vez que se empieza un partido, el programa debe “eligir” un número de cuatro cifras
(sin cifras repetidas), que será el código que el jugador debe adivinar en la menor cantidad de
intentos posibles. Cada intento consiste en una propuesta de un código posible que tipea el jugador,
y una respuesta del programa. Las respuestas le darán pistas al jugador para que pueda deducir el código
Estas pistas indican cuán cerca estuvo el número propuesto de la solución a través dedos valores:
    la cantidad de aciertos es la cantidad de dígitos que propuso el jugador que también están en el código en la misma
    posición. La cantidad de coincidencia es la cantidad de digitos que propuso el jugador que también están en el
    código pero en una posición distinta

import random

def carga_string_no_vacio(num):
    cadena = ''
    while True:
        try:
            cadena = input('')
            if len(cadena) <= num and cadena.isdigit():
                return cadena
            else:
                print(f'ATENCIÓN: Debe ingresar un numero de {num} digitos')
        except ValueError:
            print(f'ATENCIÓN: Debe ingresar un numero de {num} digitos')


def generacion_codigo(num):
    print(f'Generando codigo de {num} digitos')
    digitos = ('0','1','2','3','4','5','6','7','8','9')
    codigo = ''
    for i in range(num):
        digito  = random.choice(digitos)
        while digito in codigo:
            digito  = random.choice(digitos)
        codigo += digito
    print(codigo)
    return codigo       

def comparacion(codigo, intento):
    aciertos = coincidencias = 0
    for c, p in zip(codigo, intento):
        if c == p:
            print(f'El numero {p} es un acierto')
            aciertos += 1
        elif p in codigo:
            print(f'El numero {p} esta en el codigo secreto')
            coincidencias += 1
    print(f'Tu propuesta ({intento}) tiene {aciertos} aciertos y {coincidencias} coincidencias') 
    if aciertos == len(codigo): return True

def master_mind():
    num = int(input('De cuantos numeros quiere adiviniar el codigo secreto?: '))
    codigo = generacion_codigo(num)
    intentos = 0
    while True:
        print(f'Ingrese intento (numero de {num} digitos) --escriba \'Fin\' para terminar')
        intento = carga_string_no_vacio(num)
        if intento.lower() == 'fin':
            print(f'Mala suerte! El código era:{codigo}')
            break
        if comparacion(codigo, intento):
            print(f'Felicitaciones, has adivinado en {intentos} intentos!!')
            break
        intentos += 1
        
master_mind()


28. Escribir funciones que dada una cadena y un caracter:
    a) Inserte el caracter entre cada letra de la cadena. Ej: 'separar' y ',' debería devolver
    's,e,p,a,r,a,r'
    b) Reemplace todos los espacios por el caracter. Ej: 'mi archivo de texto.txt' y '_'
    debería devolver 'mi_archivo_de_texto.txt'
    c) Reemplace todos los dígitos en la cadena por el caracter. Ej: 'su clave es: 1540' y
    'X' debería devolver 'su clave es: XXXX'
    d) Inserte el caracter cada 3 dígitos en la cadena. Ej. '2552552550' y '.' debería devolver
    '255.255.255.0'


29. Modificar las funciones anteriores, para que reciban un parámetro que indique
la cantidad máxima de reemplazos o inserciones a realizar.



30. Escribir una función que reciba una cadena que contiene un largo número entero
y devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe
'1234567890', debe devolver '1.234.567.890'.



31. Escribir una función que dada una cadena de caracteres, devuelva:
    a) La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe
    devolver 'USB'.
    b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
    'república argentina' debe devolver 'República Argentina'.
    a) Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, 'cadena'
    es una subcadena de 'subcadena'.
    b) Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe 'kde' y 'gnome'
    debe devolver 'gnome'.

"""