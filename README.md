# Curso-Python-Utch
 Code and Notes for the "Programacion Python" course at UTCH-Educación Continua
 Código fuente de ejemplo y notas para el curso de "Programación Python" ofertado por Educación Continua de la Universidad Tecnológica de Chihuahua (UTCH) [www.utch.edu.mx]

 ## Día 1 - Introducción a Python

### Ints y Floats

### Operadores aritméticos

### Operadores de comparación

### Operadores lógicos

### Strings (parte 1), Input y Print

### Funciones lambda

## Día 2 - Estructuras de datos en Python

### Tuplas

### Listas

### Diccionarios

### Conjuntos

### map() , filter() y reduce()

### Strings (parte 2) y format 

### Manejo de Archivos de texto en Python (parte 1): Open, Write

Los archivos de texto con extensión **txt** son archivos sin una estructura interna específica.
Archivos de texto con extensión como **.csv .doc .json .xml** son archivos de texto que tienen una estrucutra interna especifica que hay que conocer para poder trabajar con ellos.

El manejo de los archivos de texto con extensión **txt** usualmente es más sencillo debido a que contienen lo que se denomina texto plano.

Python permite el manejo de diferentes archivos de texto sin realmente tener que conocer la estructura interna específica del formato del archivo.

Python utiliza lo que se denomina un *file handle* el cual es un objeto que utiliza Python para referirse internamente al archivo de texto que se desea manipular.

La función ***open()*** realiza las siguientes tareas o acciones:

1. Se asegura que el archivo de texto especificado exista y si no tira *throw* un error .Puede especificarsele a la función **open()** que si el archivo no existe cree uno nuevo con el nombre y la extensión dados.
2. Una vez localizado el archivo (o creado) se genera el *file handle* de este.
3. Posiciona el cursor de lectura/escritura de texto en la posición ***pos*** de inicio del archivo, **pos=0**

Una llamada a la función ***open()*** no lee ni carga en la memoria alguna parte del texto contenido en el archivo, tampoco escribe o vacia de la memoria algun texto hacia el archivo, o cierra el archivo. Todas las acciones anteriores se deben de realizar de manera **explicita por medio de los metodos del _file handle_*

```
file_handle = open('elarchivodetexto.txt')
```

| Metodo | Descripción |
| ------ | ----------- |
| file_handle.read(n=-1) | Lee, a partir de la posición actual del cursor, *n* bytes del archivo, si no se especifica un valor para *n* o si *n=-1* se leera todo los bytes restantes del archivo. |
| str = file_handle.readlines() | Lee , a partir de la posición actual del cursor, la siguiente linea de texto y regresa una cadena de caracteres *str* que contiene el caracter de nueva linea al final |
| file_handle.readlines() | Lee, a partir de la posición actual del cursor, las lineas de texto restantes dentro del archivo de texto y regresa una lista que las contiene. Las lineas de texto terminan con el caracter de nueva linea |
| file_handle.seek(pos)| Mueve el cursor dentro del archivo a la posición indicada por *pos* |
| file_handle.tell() | Regresa la posición actual del cursor dentro del archivo | 
| file_handle.write(str) | Inserta la cadena de caracteres *str* en la posición actual del cursor dentro del archivo |
| file_handle.flush() | Realiza todas las operaciones de escritura pendientes y se asegura que se actualicen en el disco o medio de almacenamiento |
| file_handle.close() | Cierra el archivo y libera los recursos de memoria asociados con el mismo |


La función ***open()***por defecto abre los archivos en modo *solo lectura*. Las siguientes son las banderas que se pueden especificar para abrir un archivo en distintos modos:

| Bandera | Modo |
| ------- | ---- |
| 'r' | Solo lectura. Posicioón inicial *pos=0*
| 'w' | Solo escritura. Si el archivo no existe, lo crea; si el archivo existe, el contenido actual se borra para escribir nuevo contenido. Posición inicial *pos=0*
| 'a' | Agregar (Append). Si el archivo existe lo abre para escritura pero no borra el contenido actual del mismo; si el archivo no existe lo crea y lo abre para escritura. Posición inicial al final del archivo.
| '+' | Actualizar (Update). Abre el archivo para realizar escritura y lectura, puede ser combinada con otras banderas; no borra el contenido actual del archivo. Posición inicial *pos=0*

# Día 3 - Programación Orientada a Objetos  (OOP) en Python

### Manejo de Archivos de texto en Python (part 2): Read

#### Ejemplo de escritura a un archivo de texto

```
file_handle = open('datos.txt','r+')
datos_originales = file_handle.read()
file_handle.seek(0)
file_handle.write('1,2,3,4\n')
file_handle.write(datos_originales)
file_handle.write('\n9,9,9,9')
file.handle.close()

```

```
str_con_texto_a_agregar = 'Texto agregado al archivo de texto'
file_handle = open('datos.txt','a')
file_handle.write(str_con_texto_a_agregar)
file_handle.close()
```

#### Ejemplo de lectura de un archivo de texto


```
datos_leidos = []
with open('datos.txt') as file_handle:
    for linea_de_texto in file_handle.readlines():
        datos_numericos = [int(x) for x in linea_de_texto.split(',')]
        datos_leidos.append(datos_numericos)
```

```
file_handle = open('datos.txt'.'r')
lista_con_lineas_de_texto = file_handle.readlines()
file_handle.close()
lista_con_lineas_de_texto
```

```
file_handle = open('datos.txt','r')
string_con_todas_lineas_de_texto = file_handle.read()
file_handle.close()
string_con_todas_lineas_de_texto
```

```
file_handle = open('datos.txt','r')
string_con_bytes_texto = file_handle.read(10)
file_handle.close()
string_con_bytes_texto
```
#### Archivos de Valores Separados por Coma (.csv)

Los archivos de Valores Separados por Coma (CSV) son en realidad archivos de texto.

```
file_handle = open(''radiation_dose.csv','r')
lineas_de_texto = file_handle.readlines()
file_handle.close()
encabezado = lineas_de_texto[0].strip().split(',')
encabezado
for linea_texto in lineas_de_texto[1:]:
    datos = linea_texto.strip().split(',')
    print(datos[0],float(datos[1]),float(datos[2]))
```

```
import csv

file_handle = open('radiation_dose.csv','r')
lector_csv = csv.reader(file_handle)
for renglon_datos in lector_csv:
    print(renglon_datos)
file_handle.close()
```

```
import csv

file_handle = open('radiation_dose.csv','r')
lector_dict_csv = csv.DictReader(file_handle)
for renglon_datos in lector_dict_csv:
    print(renglon_datos)
file_handle.close()
```

#### Archivos binarios

Aspectos a tener en cuenta cuando se utilizan archivos binarios:
-

### Introducción a la OOP

### Clases y el "SELF" en Python

### Metodos y funciones en Python


### Subclases


### Modulos y Paquetes

## Día 4 - Interfaces de usuario (GUI) con TKinter en Python

### Introducción a TKinter

### Ejemplos de GUI sencillas en Python usando TKinter



