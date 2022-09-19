print("Ingrese 3 Números distintos para notificar cual es el mayor:")

a=int(input("\n Ingrese el primer número: "))

b=int(input("\n Ingrese el segundo número: "))

c=int(input("\n Ingrese el tercer número: "))

while(a==b or a==c or b==c):
    if (a==b):
        b=int(input("\n El primer y el segundo número son iguales.\n Ingrese el segundo número nuevamente:"))
    if (a==c):
        c=int(input("\n El primer y el tercer nñumero son iguales.\n Ingrese el tercer número nuevamente: "))
    if(b==c):
        c=int(input("\n El segundo y el tercer número son iguales.\n Ingrese el tercer número nuevamente: "))

if (a>=b and a>=c):
    mayor=a

elif (b>=a and b>=c):
    mayor=b
else:
    mayor=c

print("\n El número mayor es:" + str(mayor))

print("Los números ingresados fueron: " + str(a) + ", " + str(b) + " y " + str(c) + ", en dicho orden")