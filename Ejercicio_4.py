#Ejercicio 4: Clasificacion de notas
num= float(input("Ingresar puntuacion (0-100): "))
if num >= 90 and num <= 100:
    print(" A (Sobresaliente)")
elif num >= 80 and num <= 89:
    print("B (Bueno)") 
elif num >=70 and num <= 79:
    print("C (Satisfactorio)")
elif num >= 60 and num <= 69:
    print("D (Necesita mejorar)")
else:
    print("F (Reprobado)")

