#Ecrire un programme qui demande à l'utilisateur de saisir un nombre N.

nombre = input("Veuillez saisir un nombre: ")

#Convertir nombre en integer
nombre = int(nombre) + 1

#Le programme devra ensuite calculer puis afficher la somme des nombres compris entre 1 et N.
SumNombre = 0

for i in range(nombre):
    SumNombre = SumNombre + i
    
print(SumNombre)
