class Tamagotchi:
    nombre=""
    hambre=0
    animo=0
    energia=0

    def __init__(self,nombre,hambre,animo,energia):
        self.nombre=nombre
        self.hambre=hambre
        self.animo=animo
        self.energia=energia
                
    def jugar(self):
        self.animo+=1
        self.energia-=1

    def alimentar(self):
        self.animo+=1
        self.hambre-=1

    def dormir(self):
        self.hambre+=1
        self.energia+=1

    def pasar(self):
        self.animo-=1
        self.hambre+=1
        self.energia-=1
      
    def __str__(self):
       return ("Nombre:%s\tNiveles: Hambre:%d\tAnimo:%d\tEnergia:%d ") %(self.nombre,self.hambre,self.animo, self.energia)

# Programa Principal

t=Tamagotchi("Tamagotchito",10,10,10)
t.dormir()
t.jugar()
t.alimentar()
t.pasar()
print(t)

"""
# menu
opcion=999    
while opcion != 0:
    print("\t\t\tMenu de opciones")
    print("\t\t\t0 Salir")
    print("\t\t\t1 Crear tamagotchi")
    print("\t\t\t2 Jugar")
    print("\t\t\t3 Alimentar")
    print("\t\t\t4 Pasar tiempo")
    print("\t\t\t5 Dormir")
    
    if t.energia<=0:
        print("*********************Game over**************************")
        opcion=0
    else:
        opcion=int(input("\t\t\tIngrese una opcion:"))
    
    if opcion==0:
        print("*********************Chau********************************")
    elif opcion==1:
        nom=input("Ingrese nombre:")
        t=Tamagotchi(nom,10,10,10)
        print(t)    
    elif opcion==2:  #jugar
        t.jugar()
        print(t)
    elif opcion==3:  #Alimentar
        t.alimentar()
        print(t)
    elif opcion==4:  # Pasar tiempo
        t.pasar()
        print(t)
    elif opcion==5:  # Dormir
        t.dormir()
        print(t)
    else:  #error
        print("opcion erronea")
    
"""