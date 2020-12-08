
##########################################################################################
################################### EJERCICIO 1 ##########################################
##########################################################################################
"""
Una barrio privado posee una lista de los inmuebles que tiene en alquiler con los siguientes datos:  
    ●Nro. Lote de la casa
    ●Nombre del titular
    ●Cantidad de AMBIENTES (1 –2 –3 –4)
    ●Precio del alquiler anual
1)Diseñar un programa que permita cargar toda la lista en cuatro arreglos:
LOTES, TITULARES, AMBIENTES y ALQUILER. La carga finaliza con lote = 0.
2)Listar los datos en cuatro columnas LOTE -TITULAR -AMBIENTES -ALQUILER
3)Calcular el precio promedio de las casas del barrio privado.
4)Determinar de cuántos AMBIENTES tiene el alquiler más caro

from random import randint

def promedio_arreglo(arreglo):
    promedio = 0
    for num in arreglo:
        promedio += num/len(arreglo)
    return round(promedio, 2)    

def carga_num():
    num = 0
    while True: 
        try:
            num = int(input(''))
            return num
        except ValueError:
            print('ATENCIÓN: Debe ingresar un número entero.')

def indice_max(arreglo):
    i = arreglo.index(max(arreglo))
    return i

def ambientes_mas_caro(arreglo, indice):
    cant_amb = arreglo[indice]
    print('La cantidad de ambientes del alquiler mas caro es:', cant_amb)
                
def carga_string_no_vacio():
    cadena = ''
    while True:
        try:
            cadena = input('')
            if cadena != '':
                return cadena
            else:
                print('ATENCIÓN: Debe ingresar un dato no vacio')
        except ValueError:
            print('ATENCIÓN: Debe ingresar un dato no vacio')

def carga_lote():
    arreglo = []
    numero = randint(1, 100)
    arreglo.append(numero)
    return arreglo

def completarConEspacios(cadena):
        cantidadEspacios = 20 - len(cadena)
        for i in range(0, cantidadEspacios):
            cadena += " "
        return cadena

LOTES = []
TITULARES = []
AMBIENTES = []
ALQUILERES = []
contador = 0
while True:
    nro_lote = ambiente = 0
    print('Ingrese numero de lote. "0" para finalizar')
    nro_lote = carga_num()
    if nro_lote == 0 and contador != 0: break
    LOTES.append(nro_lote)
    print('Ingrese Titular')
    TITULARES.append(carga_string_no_vacio())
    print('Ingrese Cantidad de AMBIENTES')
    while True:
        ambiente = carga_num()
        if ambiente == 1 or ambiente == 2 or ambiente == 3 or ambiente == 4:
            AMBIENTES.append(ambiente)
            break
        else:
            print('ATENCION: Debe ingresar 1, 2, 3, o 4 AMBIENTES')
    print('Ingrese $$$ Alquiler')
    ALQUILERES.append(carga_num())
    contador += 1

print(completarConEspacios('LOTES'), completarConEspacios('TITULARES'), completarConEspacios('AMBIENTES'),completarConEspacios('ALQUILER'))
for i in range(0, contador):
    print(completarConEspacios(str(LOTES[i])), completarConEspacios(TITULARES[i]), completarConEspacios(str(AMBIENTES[i])), completarConEspacios(str(ALQUILERES[i])), )
print('El promedio de ALQUILERES en el barrio es:', promedio_arreglo(ALQUILERES))
ambientes_mas_caro(AMBIENTES, indice_max(ALQUILERES))
"""
##########################################################################################
################################### EJERCICIO 2 ##########################################
##########################################################################################
"""
Una empresa de Viajes de Egresados guarda la información de los alumnos que quieren viajar:
- nombre y apellido - sexo - Destino: Bariloche - Porto Seguro.
Ingresar los datos de todos los viajeros, hasta que no se quiera cargar más viajeros (ingresan “fin” en el nombre). Se pide:
a) Separar mujeres y varones: se pide guardar en un arreglo el nombre de las mujeres y en otro el de los hombres.
b) Listar ambos grupos de datos ordenados alfabéticamente para pasárselo a la empresa de micros. Agregar el nùmero de viajero (empezando en 1 en adelante). Si alguno de los vectores quedará vacío, Indicarlo con un mensaje por pantalla.
c) Mostrar el Porcentaje de Hombres y Mujeres: 
d) Calcular e imprimir los porcentajes de alumnos que eligieron cada destino.
e) Decir cual es el destino con mayor cantidad de viajeros


class Viajero():
    nombre = ''
    apellido = ''
    sexo = ''
    destino = ''

    def __init__(self, nombre, apellido, sexo, destino):
        self.nombre = nombre.capitalize()
        self.apellido = apellido.capitalize()
        self.sexo = sexo.upper()
        self.destino = destino.capitalize()
        
    def __gt__(self, viajero):
        return ((self.apellido > viajero.apellido) and (self.nombre > viajero.nombre))
    
    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

def porcentage_h_m(viajeros):
    cant_h = cant_m = 0
    for viajero in viajeros:
        if viajero.sexo.upper() == 'H':
            cant_h += 1
        elif viajero.sexo.upper() == 'M':
            cant_m += 1
    print(f'Porcentaje de viajeros \nHombres: {round(cant_h/len(viajeros)*100, 2)}%,\nMujeres: {round(cant_m/len(viajeros)*100, 2)}%')

def porcentage_destino(viajeros):
    cant_B = cant_P = 0
    for viajero in viajeros:
        if viajero.destino.upper() == 'B':
            cant_B += 1
        elif viajero.destino.upper() == 'P':
            cant_P += 1
    print(f'Porcentaje de viajeros \nBariloche: {round(cant_B/len(viajeros)*100, 2)}%,\nPorto Seguro: {round(cant_P/len(viajeros)*100, 2)}%')
    if cant_B > cant_P:
        print('El destino con mayor cantidad de viajeros es: "Bariloche"')
    else:
        print('El destino con mayor cantidad de viajeros es: "Porto Seguro"')
def carga_string_no_vacio():
    cadena = ''
    while True:
        try:
            cadena = input('')
            if cadena != '':
                return cadena
            else:
                print('ATENCIÓN: Debe ingresar un dato no vacio')
        except ValueError:
            print('ATENCIÓN: Debe ingresar un dato no vacio')

def carga_num():
    num = 0
    while True: 
        try:
            num = int(input(''))
            return num
        except ValueError:
            print('ATENCIÓN: Debe ingresar un número entero.')

def carga_viajeros():
    PASAJEROS = []
    while True:
        sexo = destino = ''
        print('Ingrese Nombre. Para salir ingrese "Fin"')
        nombre = carga_string_no_vacio()
        if nombre.lower() == 'fin':
            break
        print('Ingrese Apellido')
        apellido = carga_string_no_vacio()
        print('Ingrese Sexo [H/M]')
        while True:
            sexo = carga_string_no_vacio()
            if sexo.upper() == 'M' or sexo.upper() == 'H':
                break
            else:
                print('ATENCIÓN: Debe ingresar "H" o "M"')
        print('Ingrese Destino [Bariloche - "B" / Porto Seguro - "P"]')
        while True:
            destino = carga_string_no_vacio()
            if destino.upper() == 'B' or destino.upper() == 'P':
                break
            else:
                print('ATENCIÓN: Debe ingresar "B" o "P"')
        viajero = Viajero(nombre, apellido, sexo, destino)
        PASAJEROS.append(viajero)
    return PASAJEROS
def imprimir_viajeros(viajeros):
    ordenada = sorted(pasajeros)
    for viajero in ordenada:
        print(viajero)


pasajeros = carga_viajeros()
porcentage_h_m(pasajeros)
imprimir_viajeros(pasajeros)
porcentage_destino(pasajeros)
"""
##########################################################################################
################################### EJERCICIO 3 ##########################################
##########################################################################################
"""
class Paciente():
    obra_social = 0
    nombre = ''
    edad = 0


    def __init__(self, obra_social, nombre, edad):
        obras_sociales = ['Osde', 'Swiss', 'Italiano', 'Otros']
        self.obra_social = obras_sociales[obra_social-1].lower()
        self.nombre = nombre.upper()
        self.edad = edad
        
    def __str__(self):
        cadena = f'Paciente {self.nombre} de {self.edad} años con {self.obra_social}'
        return cadena

def carga_num():
    num = 0
    while True: 
        try:
            num = int(input(''))
            return num
        except ValueError:
            print('ATENCIÓN: Debe ingresar un número entero.')

def carga_num_mayor_que(min):
    num = 0
    while True:
        try:
            num = int(input(''))
            if num > min:
                return num
            else:
                print('ATENCIÓN: Debe ingresar un número entero mayor que', min)
        except ValueError:
            print('ATENCIÓN: Debe ingresar un número entero mayor que', min)

def carga_string_no_vacio():
    cadena = ''
    while True:
        try:
            cadena = input('')
            if cadena != '':
                return cadena
            else:
                print('ATENCIÓN: Debe ingresar un dato no vacio')
        except ValueError:
            print('ATENCIÓN: Debe ingresar un dato no vacio')

def carga_paciente():
    arreglo = []
    #n = int(input('Ingrese cantidad de pacientes a atender'))
    for i in range(0, 10):  # n
        #paciente = 'paciente_'
        #paciente = paciente + str(i)
        print('Paciente numero', i+1)
        print('Ingrese Nombre del paciente: ')
        nombre = carga_string_no_vacio()
        print(f'Ingrese Obra social de {nombre}: (1 - Osde, 2 - Swiss, 3 - Italiano, 4 - Otros): ')
        while True:
            obra_social = carga_num()
            if obra_social == 1 or obra_social == 2 or obra_social == 3 or obra_social == 4:
                break
            else:
                print('ATENCION: Debe ingresar 1, 2, 3, o 4')
        print(f'Ingrese Edad de {nombre}: ')
        edad = carga_num_mayor_que(0)
        paciente = Paciente(obra_social, nombre, edad)
        arreglo.append(paciente)
    return arreglo

def cantidad_pacientes_e(edad, pacientes):
    contador = 0
    for paciente in pacientes:
        if paciente.edad > edad:
            contador += 1
    print('La cantidad de pacientes mayores a ', edad, 'es de', contador, ', representa un', round(contador/len(pacientes)*100, 2), '% del total')

def porcentage_pacientes_obra(pacientes):
    contador_osde = contador_swiss = contador_italiano = contador_otros = 0
    for paciente in pacientes:
        if paciente.obra_social == 'osde':
            contador_osde += 1
        elif paciente.obra_social == 'swiss':
            contador_swiss += 1
        elif paciente.obra_social == 'italiano':
            contador_italiano += 1
        elif paciente.obra_social == 'otros':
            contador_otros += 1
    print(f'Porcentaje de pacientes con \nOSDE: {round(contador_osde/len(pacientes)*100, 2)}%, \nSWISS: {round(contador_swiss/len(pacientes)*100, 2)}%, \nITALIANO: {round(contador_italiano/len(pacientes)*100, 2)}%, \nOTROS: {round(contador_otros/len(pacientes)*100, 2)}%')

def cantidad_pacientes_obra(pacientes):
    contador_osde = contador_swiss = contador_italiano = contador_otros = 0
    for paciente in pacientes:
        if paciente.obra_social == 'osde':
            contador_osde += 1
        elif paciente.obra_social == 'swiss':
            contador_swiss += 1
        elif paciente.obra_social == 'italiano':
            contador_italiano += 1
        elif paciente.obra_social == 'otros':
            contador_otros += 1
    obras_sociales = {'osde':contador_osde, 'swiss':contador_swiss, 'italiano':contador_italiano, 'otros':contador_otros}
    clave_mayor = max(obras_sociales.keys())

    print(f'Obra social con mayor cantidad de pacientes: {clave_mayor} y su valor es {obras_sociales.get(clave_mayor)}')

def imprimir_pacientes(arreglo):
    for paciente in arreglo:
        print(paciente)

pacientes = carga_paciente()

imprimir_pacientes(pacientes)
cantidad_pacientes_e(21, pacientes)
porcentage_pacientes_obra(pacientes)
cantidad_pacientes_obra(pacientes)
"""

##########################################################################################
################################### EJERCICIO 4 ##########################################
##########################################################################################
"""
Una concesionaria, necesita registrar “cada” venta realizada, para lo que se ingresa:
● Marca: 1- AA, 2-BB, 3-CC, 4-DD
● Tipo: 1- Auto, 2- Pïck Up, 3 – SUV, 4- Motocicleta, 5-Deportivo
● Precio (En pesos)
El ingreso termina con marca = 0
A. Guardar en un nuevo arreglo los vehículos con valor superior a $300.000 (inclusive) y guardar en otro los menores a $200.000.
B. Decir de qué marca fue el vehículo más costoso y de qué marca fue la motocicleta mas economica.
C. Calcular cuántos vehículos se vendieron por tipo y determinar cuál es el más vendido.
D. Listar los los vehículos con valor superior a $500.000.
"""


##########################################################################################
################################### EJERCICIO 5 ##########################################
##########################################################################################
"""
Se ingresan la cantidad de kilos vendidos de chocolate amargo y semiamargo (dos vectores) a lo largo de el mes de junio (30 días). El valor del kilo de chocolate amargo es $3500 y el valor del kilo del chocolate semiamargo es de $2400. Calcular y mostrar:
a) El día del mes donde se vendieron más kilos de chocolate amargo y el día del mes donde se vendieron la menor cantidad de chocolate semiamargo.
b) Insertar la recaudación del mes al comienzo del arreglo en cada tipo de chocolate
c) Eliminar las ventas menores a 3 kilos de cada tipo de chocolate.

"""
