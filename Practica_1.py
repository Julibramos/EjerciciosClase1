#Leer 3 notas de un alumno, calcular definitiva en rango de 0-5 y enviar mensaje que diga si aprobó o no
num = float(input("Ingresar nota 1: "))
num2= float(input("Ingresar nota 2: "))
num3= float(input("Ingresar nota 3: "))
pro= (num+num2+num3)
definitiva= (pro/3)
if definitiva < 3: 
    print("No aprobo la materia")
elif definitiva >= 3:
    print("Aprobo la materia")
    print(definitiva)