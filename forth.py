print("Categorizador de notas")

def val_nota(nota):
    while (True):
        if nota>=1 and nota <=10:
            return nota
        else:
            nota=int(input("La nota ingresada es " + str(nota) + "\n\n Solo son válidas la notas entre 1 y 10 :"))

def res_nota(nota):
    if nota>=9 and nota <=10:
        return "Ha obtenido una calificación sobresaliente"
    elif nota>=7 and nota <=8:
        return "Ha obtenido una calificación notable"
    elif nota>=4 and nota<=6:
        return "Ha obtenido un aprobado"
    elif nota>=1 and nota <=3:
        return "ha desaprobado"

def imprimir_curso(curso):
    for alumno in curso:
        print("\n"+alumno["nombre"] + " " + alumno["calificacion"])
        

def lista_alumnos():
    curso=[]
    while(True):
        alumno={"nombre": input("Ingrese el nombre del alumno: ")}
        alumno["nota"]= val_nota(int(input("Ingrese la calificación de " + alumno["nombre"] +": ")))
        alumno["calificacion"]= res_nota(alumno["nota"])
        curso.append(alumno)

        print(alumno)

        salida=input("Si desea imprimir la Lista de resultados de cada alumno ingrese 'IMPRIMIR'")
        
        if salida =="IMPRIMIR":
            return imprimir_curso(curso)

lista_alumnos()

        
