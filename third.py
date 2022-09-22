## Definición de funciones

def number_month(month):
   months=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
   month=month.lower()
   while(True):
    for i in range(len(months)):
        if month==months[i]:
            return i+1
    month=input("\n\n El mes ingresado no es válido.\n\n Ingrese el mes nuevamente: ")

def precio_final(price,month):
    if month==10:
        return print("\n\n el precio del producto es $"+ str(price)+" y con el descuento, el precio final sería $" + str(price*0.85))
    else:
        return print("\n\n el precio del producto es $"+ str(price) + " y no corresponde descuento")

##ejecución

print("Tienda \n \n")

price=int(input("Ingrese el precio del producto: $"))

month=number_month(input("\n\n Ingrese el mes de la compra:"))


precio_final(price,month)