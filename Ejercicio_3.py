#Ejercicio 3:Calculadora de descuento 
#Ingrese precio de producto y edad- menos de 18(aplica el 10%)- tiene 65 o mas(aplica el 15%)-en otros casos no aplica
num = float(input("Ingresar edad: "))
producto = float(input("Ingresar precio producto: "))
if num < 18:
    descuento = producto * 0.10
    print(descuento)    
elif num == 65 or num > 65: 
    descuento = producto*0.15
    print(descuento)
else: 
    print("ningun descuento")
