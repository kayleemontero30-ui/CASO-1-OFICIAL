# !pip install ....
#como import
import math as m
import pandas as pd 

def evaluar_funcion(a, b, c, x):
    y = a*x**2+b*x+c
    return y

def evaluar_funcionF2(a, b, c, N):
    y = a*N**2+b*N+c
    return y

def evaluar_F6(A, B, C, x):
     y = A*x**2+B*x+C 
     return y

def evaluar_discriminante(a, b ,c):
    D = (b**2-4*a*c)
    return D
    
def evaluar_D6(A, B, C):
    D = (B**2-4*A*C)
    return D
    
def evaluar_quadratica(a, b, c):
    if a == 0:
        print("Ecuacion invalida. Introduzca un valor distinto de 0 para a.")
        return None
    D = evaluar_discriminante(a, b, c)
    if D >= 0:
        x1 = ((-b)/(2*a)) + (m.sqrt(D)/(2*a))
        x2 = ((-b)/(2*a)) - ((m.sqrt(D))/(2*a))
    else:
        real = (-b)/(2*a)
        im = m.sqrt(abs(D)) / (2*a)
        x1 = complex(round(real,2), round(im,2))
        x2 = complex(round(real,2), round(-im,2))
    return x1, x2
def evaluar_lineal(b, c):
    if b==0:
        print("No hay solucion(a y b son 0.)")
        return None
    x= -(c)/(b)
    y = 0
    return x, y

def evaluar_L6(B, C):
    if B==0:
        print("No hay interseccion")
        return None
    x= -(C)/(B)
    return x

def evaluar_QR6(A, B, C):
    if A==0:
        print("Ecuacion invalida. Introduzca un valor no 0 de a")
        return None
    D = evaluar_D6(A, B, C)
    x1=((-B)/(2*A)) + ((m.sqrt(D))/(2*A))
    x2=((-B)/(2*A)) - ((m.sqrt(D))/(2*A))
    return x1, x2
        
def evaluar_simetria_real(a, b):
    if a==0:
        print("Ecuacion invalida. Introduzca un valor no 0 de a")
        return None
    x=(-b)/(2*a)
    return x
        
def evaluar_SR6(A, B):
    if A==0:
        print("Ecuacion invalida. Introduzca un valor no 0 de a")
    x=(-B)/(2*A)
    return x

def evaluar_restas(a, a1, b, b1, c, c1):
    A = a - a1
    B = b - b1
    C = c - c1
    return A, B, C

def evaluar_pendiente(a, b, M):
    y=2*a*M+b
    return y

import random 

def evaluar_numeros_aleatorios(a, b, c, A, B, N=7):
    valores = []
    for _ in range(N):
        x = random.uniform(A, B)  # Example range
        y = evaluar_funcion(a, b, c, x)
        valores.append((x, y))
    return valores
    
#    list= [random.sample(range(1, 100),6)]
   # i=0
    #for i<7 in range(i):
   # x= random.sample((range(100), 6)
   # y= evaluar_funcion(a, b, c, x)
  #  return list #valores??
    #print(Numero{i}: x= {x}, y= {y})

print("~Programa para Ecuaciones de Segundo Grado~")

while True:
    try:
        a =float(input("Ingrese el valor de a:__"))
        b =float(input("Ingrese el valor de b:__"))
        c =float(input("Ingrese el valor de c:__"))
    except ValueError:
        print("Indrosuzca valores numericos validos")
        continue
    

    print("""
  ~  MENU PRINCIPAL ~
  1. Resolver la ecuacion para toda solucion.
  2. Evaluar funcion en un numero N.
  3. Evaluar en 7 valores aleatorios en un intervalo [a , b].
  4. Linea de simetria, vertices y concavidad.
  5. Pendiente de la tangente en un punto M.
  6. Interseccion entre dos curvas.
  7. Salir.
 """)
    opcion = input("Elija una opcion:")

    if opcion=='1':
        if a==0:
            x= evaluar_lineal(b, c)
            print("Ecuacion lineal")
            print(f"Solucion: x = {x}")
        else:
            D= evaluar_discriminante(a, b, c)
            x1, x2= evaluar_quadratica(a, b, c)
            
            if D==0:
                print(f"Una solucion real: x= {round(x1, 2)}")
            elif D >=0:
                print(f"Dos soluciones reales: x1= {round(x1, 2)} y x2= {round(x2, 2)}")
            else:

                print(f"Dos soluciones imaginarias: x1= {x1}  y x2= {x2}")
#PREGUNTARRRRRRR: que hace cuando se pone f alante de lo que quieres print.
                
    elif opcion=='2':
        N = float(input("Ingrese el valor de N:"))
        y = evaluar_funcionF2(a, b, c, N)
        print(f"Solucion y = {round(y, 2)}")
#evaluar_N(a,b,c):"evalua la funcion en un numero N" N=leer_entero(N(entero)) yN=f(N, a, b, c) 

                           
    elif opcion=='3':
        A=float(input("Ingrese el limite inferior del intervalo:"))
        B=float(input("Ingrese el limite superior del interalo:"))
        list = evaluar_numeros_aleatorios(a, b, c, A, B)
        print("Valores aleatorios con solucion:")
        for x, y in list:
            print(f"Para x= {round(x, 2)}, y= {round(y, 2)} ")
            ########revisaaaaaaa
            
    elif opcion=='4':
        x= evaluar_simetria_real(a, b)
        y= evaluar_funcion(a, b, c, x)
        print(f"Simetria: x= {round(x, 2)}")
        print(f"Vertice: ({round(x, 2)} , {round(y, 2)})")
        if a>0:
            print("Convexa hacia arriba")  
        else:
            print("Concava hacia abajo") 

    elif opcion=='5':
        M = float(input("Ingrese el valor de M:"))
        y = evaluar_pendiente(a, b, M)
        print(f"Pendiente de la tangente en M= {round(y, 2)}")  

    elif opcion=='6':
        a1 = float(input("Ingrese el valor de a1:__"))
        b1 = float(input("Ingrese el valor de b1:__"))
        c1 = float(input("Ingrese el valor de c1:__"))
        A, B, C= evaluar_restas(a, a1, b, b1, c , c1)
        if A==0:  
            if B==0:
                print("Las funciones no tienen interseccion.")
            else:
                x= evaluar_L6(B, C)
                y= evaluar_funcion(a, b, c, x)
                print(f"Punto de Interseccion: ({round(x, 2)},{round(y, 2)})")

        else:
            D= evaluar_D6(A, B, C) 
            if D <=0:
                print("Las parabolas no se curzan, no hay interseccion.")

            elif D==0:
                x = evaluar_SR6(A, B)
                y= evaluar_funcion(a, b, c, x)
                print("Las parabolas tienen un punto de interseccion (tangente).")
                print(f"Puntos de Interseccion: P= ({round(x, 2)},{round(y, 2)})")

            else:
                x1, x2= evaluar_QR6(A, B, C)
                y1= evaluar_funcion(a, b, c, x1)
                y2= evaluar_funcion(a, b, c, x2)
                print("Las parabolas tienen dos puntos de interseccion.")
                print(f"Punto de Interseccion 1:({round(x1, 2)},{round(y1, 2)}) ")
                print(f"Punto de Interseccion 2:({round(x2, 2)},{round(y2, 2)}) ")

    elif opcion=='7': 
        print("Saliendo del programa...")
        break
    
    else:
        print("Opcion no valida")