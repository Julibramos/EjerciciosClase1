#Determinar el mayor de 3 numeros 
num1= float(input("Ingresar valor 1: "))
num2= float(input("Ingresar valor 2: "))
num3= float(input("Ingresar valor 3: "))
if num1 > num2 > num3:
    print(num1)
elif num2 > num1 > num3:
    print(num2)
elif num3 > num2 > num1:
    print(num3)
elif num1 > num3 > num2:
    print(num1)
elif num2 > num3 > num1:
    print(num2)
elif num3 > num1 > num2:
    print(num3)