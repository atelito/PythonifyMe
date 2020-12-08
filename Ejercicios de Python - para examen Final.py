
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
"""
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

##########################################################################################
################################### EJERCICIO 2 ##########################################
##########################################################################################


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
    print(f'Porcentaje de pacientes con OSDE: {round(contador_osde/len(pacientes)*100, 2)}%, SWISS: {round(contador_swiss/len(pacientes)*100, 2)}%, ITALIANO: {round(contador_italiano/len(pacientes)*100, 2)}%, OTROS: {round(contador_otros/len(pacientes)*100, 2)}%')

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

##########################################################################################
################################### EJERCICIO 5 ##########################################
##########################################################################################

##########################################################################################
################################### EJERCICIO 6 ##########################################
##########################################################################################