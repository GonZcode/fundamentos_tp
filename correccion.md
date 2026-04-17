
# Este documento contiene la corrección del archivo perteneciente a Abalo - Gimenez Lescano - Pate


## Punto 1

### Si el programa principal o función main() y las funciones tienen los docstrings (secciones declarativas) iniciales describiendo el análisis y el diseño correspondiente: objetivo del programa o contrato de la función (análisis) y reporte de variables (nombre, tipo y para qué se usa -diseño).

Aunque todas las funciones cuentan con una buena estructura inicial indicando "Sección Declarativa", "Descripción", "Precondición" y "Postcondición", falta el reporte detallado de variables exigido por la consigna. No se incluye una sección que indique explícitamente el nombre, tipo y propósito de las variables locales utilizadas dentro de cada función o del programa principal como tampoco hay un docstring a nivel de módulo (al inicio del archivo) que explique el objetivo general del programa completo.


## Punto 2

### Si las secciones de código del programa y de las funciones están documentadas con comentarios de encabezamiento de subsecciones que anuncian su objetivo o con comentarios de fin de línea explicando lo que resuelven instrucciones significativas o secuencias de instrucciones de estructuras de control. Se debe poder hacer un seguimiento o traza de ejecución de programas y funciones mediante la documentación interna (programación literaria).


El programa cumple con la consigna, pero sin embargo, hay un comentario con información erronea en la función busqueda_binaria. 
En la línea der = len(datos) - 1, el comentario dice ''# Devuelve la cantidad de elementos'', lo cual es incorrecto; en realidad, devuelve el índice del último elemento de la lista.


## Punto 3

### Si las funciones están al comienzo de la sección de código, antes del programa principal o función main(), y antes de cualquier otra función que las invoque.

Todas las funciones cumplen con la consigna, es decir repetan el orden lógico, aunque en la función que cumple el papel de main(), en nuetra opinion no se optimiza el codigo.

## Punto 4

### Si los nombres de variables son mnemónicos, es decir, claramente indicativos de los valores que representan.

La elección de nombres para las variables es la adecuada para el contexto del problema.

## Punto 5
### Si el programa es correcto y completo, es decir, si cumple todas las especificaciones del enunciado con eficacia.

El programa genera bien los datos, las claves y ejecuta el banco de pruebas midiendo los tiempos correctamente. Las lógicas de las tres búsquedas cumplen su función (incluyendo la prevención de división por cero en la búsqueda por interpolación) y el programa satisface las especificaciones del enunciado. Aunque faltarian las especificaciones que corregimos en el punto 1


## Punto 6
### Si la interfaz del programa es amigable: los resultados deben estar bien presentados y descriptos.

No cumple totalmente. Aunque la impresión de la tabla utiliza f-strings con un formato muy prolijo y alineado que facilita la lectura de los datos crudos, la consola simplemente arroja una tabla sin explicarle al usuario qué experimento se está corriendo, qué significan los datos o qué representan las columnas. Podria incluirse un mensaje para explicar el contexto. 


## Punto 7
### Si hay una evaluación de resultados, sea mediante documentación interna o impresión en pantalla.

El código imprime los datos crudos (tiempos y ratio) en pantalla mediante la tabla, pero no ofrece ninguna evaluación, conclusión o análisis de esos resultados. Faltan sentencias al final del experimento que interpreten los datos empíricos.


## Punto 8
### Si recomiendan una o más cambios para mejorar la legibilidad o la eficiencia del programa o funciones.
   
Recomendamos aplicar los siguientes cambios para elevar la calidad y eficiencia del código:

    - Corregir comentarios imprecisos: Modificar el comentario en la búsqueda binaria asociado a la variable der para reflejar que representa el "último índice" y no la "cantidad de elementos".

    - Mejorar la Interfaz de Usuario (UI): Agregar un print() al inicio de ejecutar_experimento() que dé contexto, por ejemplo: "Iniciando experimento de rendimiento de algoritmos de búsqueda...".

    - Agregar Conclusión: Añadir unas líneas de código al final del script que impriman una breve conclusión teórica contrastada con la empírica basándose en los datos obtenidos del ratio.

    - También se recomienda que la función donde se ejecuta el programa principal, optimize lo más posible el código, lo ideal seria que en esta función solo se llame a las demás funciones. 


## Corregido por Argañin y Vasquez Gonzalez