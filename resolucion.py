'''
======================================================================================================
SECCIÓN DECLARATIVA

Descripción: Experimento en el cual se mediran los tiempos de ejecución de búsqueda lineal, 
búsqeuda binaria y búsqueda por interpolación para distintos tamaños de entrada.

Casos de Prueba: 
Listas de tamaño n = [5000, 10000, 50000, 100000]
Busqueda de 1000 claves (500 presentes y 500 ausentes) para medir el promedio real

Recursos: 
Modulo time para perf.counter()
modulo random para sample y seed
n (int) 
datos (list) = lista de números enteros
claves (list) = lista de números a buscar en datos


======================================================================================================
'''
import random
import time
from rich.table import Table
from rich.console import Console

#=========================
# DEFINIMOS LAS FUNCIONES
#=========================

def generar_datos(n, semilla): #Funcion para obtener los datos para el experimento - Lista Ordenada + Casos de Prueba
    ''' SECCIÓN DECLARATIVA
    Descripción: Generamos los datos para el experimento.
    
    Precondición: Utilizamos Semilla para tener los datos iguales
    
    Postcondición: Retornamos los valores de los datos
'''
    #Sección algoritmica
    
    # Prólogo: Con random creamos los datos a utilizar y con semilla determinamos como serán.
    random.seed(semilla) 
    
    # Resolución: Creamos la lista ordenada y con distribución uniforme
    datos = sorted(random.sample(range(1, 10 * n), n)) 
    return datos

def claves_a_buscar (datos, n):
    ''' SECCIÓN DECLARATIVA
    Descripción: Generamos las claves para el experimento.
    
    Precondición: Utilizamos Semilla para tener los datos iguales
    
    Postcondición: Retornamos los valores de las claves 
    '''
    #Creamos las claves a utilizar, 500 presentes y 500 ausentes
    claves_presentes = random.sample(datos, 500)
    claves_ausentes = random.sample(list(set(range(1, 10 * n)) - set(datos)), 500)
    
    # Juntamos las claves en una misma lista
    claves = claves_presentes + claves_ausentes
    return claves

  
def busqueda_lineal(datos, clave):
    '''  Sección Declarativa
    Descripción: Buscamos la posicion "clave" en la secuencia "datos". 
        Recorremos la secuencia elemento a elemento hasta encontrar clave o agotoar todos los elementos
    
    Precondición: datos es una secuencia indexeable; clave es comparable con los elementos de datos mediante ==.
    
    Postcondición: Retorna el índice i tal que datos[i] == clave o -1 si no se encuentra.
    '''

    #Sección Algoritmica
     
    #Prólogo: Obtener el tamaño de la secuencia 
    n = len(datos)
     
    #Resolución: Recorremos hasta encontrar o agotar
    i = 0
    while i < n and datos[i] != clave:
        i += 1
    
    #Epílogo: Inspeccion post-bucle
    if i < n:
        return i
    else:
        return -1
    
def busqueda_binaria(datos, clave):
    '''
    SECCIÓN DECLARATIVA
    
    Descripción: Buscamos la posicion "clave" en la secuencia "datos". 
    Precondición: datos está ordenada de menor a mayor.
    Postcondición: Retorn el índice i tal que datos[i] == clave, o -1 si no se encuentra en datos.
    '''
    #Sección Algoritmica

    # Prólogo: Definir la región de búsqueda
    izquierda = 0
    derecha = len(datos) - 1
    
    # Resolución: Dividimos la región por la mitad en cada paso
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if datos[medio] == clave:
            return medio # Clave encontrada
        elif clave < datos[medio]:
            derecha = medio - 1 # Descartamos la mitad derecha
        else:
            izquierda = medio + 1 # Descartamos la mitad izquierda
    
    # Epílogo: La región quedó vacia (izquierda > derecha)
    return -1 # No encontrado
       
def busqueda_interpolacion(datos, clave):
    '''
    Sección Declarativa
    Descripción: Buscamos la posicion "clave" en la secuencia ordenada "datos" usando interpolación
    Precondición: Datos está ordenada de menor a mayor.
    Postcondición: Retorna el índice i tal que datos[i] == clave, o -1 si no se encuentra en datos.
    '''
    
    #Seccion Algoritmica
    
    #Prólogo: Definir la región de búsqueda
    izquierda = 0
    derecha = len(datos) - 1
    
    #Resolucion:
    while izquierda <= derecha and datos[izquierda] <= clave <= datos[derecha]:
        # Evitamos division por cero cuando todos los valores son iguales
        if datos[izquierda] == datos[derecha]:
            if datos[izquierda] == clave:
                return izquierda
            else:
                return -1   
            
        # Estimamos la posición por interpolación
        posicion = izquierda + (clave - datos[izquierda]) * (derecha - izquierda) // (datos[derecha] - datos[izquierda])
        
        if datos[posicion] == clave:
            return posicion
        elif datos[posicion] < clave:
            izquierda = posicion + 1
        else:
            derecha = posicion - 1
    return -1



def medir_busquedas(funcion, datos, claves, repeticiones=3):
    '''
    Sección Declarativa
    Descripción: Mide el tiempo promedio de ejecución de una función de búsqueda dada una lista de datos y claves.      
    Precondición: funcion es una función de búsqueda que toma (datos, clave) como argumentos; datos es una lista de números ordenada; claves es una lista de números a buscar en datos; repeticiones es un entero positivo.
    Postcondición: Retorna el tiempo promedio de ejecución en milisegundos.
    '''
    #Empezamos el cronometro 
    inicio = time.perf_counter()
    
    # lo repetimos 3 veces
    for _ in range(repeticiones):
        for clave in claves:
            #Ejecutamos la funcion dada al incio
            funcion(datos, clave)
    #frenamos el tiempo
    fin = time.perf_counter()
    
    #calculamo el promedio en milisegundos
    # fin - incio nos daria en segundos
    # despues devidimos por repeticiones para el promedio y x1000 para milisegundos
    
    #Tiempo total / repeticiones / 1000 para pasar a ms
    tiempo_promedio = ((fin - inicio) / repeticiones) * 1000
    
    return tiempo_promedio          
            


from rich.table import Table
from rich.console import Console

def mostrar_tabla(resultados):  # En formato alineado
    '''Seccion declarativa
    Descripción: Mostrar los resultados en una tabla formateada usando rich.   
    Precondición: resultados es una lista de tuplas (n, t_lin, t_bin, t_int) donde n es el tamaño de la entrada y t_* son los tiempos promedio en ms.
    Postcondición: Imprime una tabla formateada con los resultados.
    '''
# Sección algorítmica
    tabla = Table(title="Resultados de Búsqueda")
    tabla.add_column("Tamaño (n)", justify="right", style="cyan", no_wrap=True)
    tabla.add_column("Búsqueda Lineal (ms)", justify="right", style="red")
    tabla.add_column("Búsqueda Binaria (ms)", justify="right", style="yellow")
    tabla.add_column("Búsqueda por Interpolación (ms)", justify="right", style="green")


# nueva columna para el punto e) 
    tabla.add_column("Ratio Lin/Bin", justify="right", style="bold white")

    for n, t_lin, t_bin, t_int in resultados:
        # Calculamos el ratio: ¿Cuántas veces es más lenta la lineal?
        ratio = t_lin / t_bin if t_bin > 0 else float('inf')  # Evitamos división por cero
        tabla.add_row(str(n), f"{t_lin:.4f}", f"{t_bin:.4f}", f"{t_int:.4f}", f"{ratio:.4f}x")

    console = Console()
    console.print(tabla)

def main():
    # Programa Principal
    resultados_finales = []  # Lista para almacenar los resultados de cada tamaño de entrada
    for n in [5000, 10000, 50000, 100000]: 
        
        datos = generar_datos(n, semilla=42)

        claves = claves_a_buscar(datos, n)
        
        t_lin = medir_busquedas(busqueda_lineal, datos, claves)
        
        t_bin = medir_busquedas(busqueda_binaria, datos, claves)
        
        t_int = medir_busquedas(busqueda_interpolacion, datos, claves)

        resultados_finales.append((n, t_lin, t_bin, t_int))

    mostrar_tabla(resultados_finales)   
        
    #Print final para el análisis del Punto (e)
    print("\nANÁLISIS TEÓRICO:")
    print("Tal como pide el Problema 5, observamos que el ratio crece significativamente.")
    print(f"Esto se debe a que la Búsqueda Lineal es O(n) y la Binaria es O(log n).")

if __name__ == "__main__":
    main()
