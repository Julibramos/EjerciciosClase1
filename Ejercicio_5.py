#Ejercicio 5: Calculo de impuesto sobre la renta
num= float(input("Ingresar salario anual: "))
if num <= 10000:
    print("No se aplica impuesto")
elif num > 10000 and num <=50000:
    descuento= (num*0.10)
    print(descuento)
elif num > 50000 and num <= 100000:
    descuento= (num*0.20)
    print(descuento)
else: 
    descuento= (num*0.30)
    print(descuento)
