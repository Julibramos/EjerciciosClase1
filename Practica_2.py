#Ingresar estatura e indicar si es bajo (igual o menor a 150cm), mediano ( entre 151 y 170 ), alto (171 en adelante)
num= float(input("Ingresar estatura: "))
if num <= 150:
    print("Persona baja")
elif num >= 151 and num <= 170:
    print("Persona mediana")
elif num > 171:
    print("Persona alta")