"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

# Lectura del archivo
with open("data.csv", "r") as file:
    data = file.readlines()

data = [line.replace("\n", "") for line in data]
data = [line.split("\t") for line in data]


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma_col_2 = 0

    for i in range(len(data)):
        suma_col_2 += int(data[i][1])
    respuesta_1 = suma_col_2

    return respuesta_1


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    col_0 = [data[i][0] for i in range(len(data))]
    letras_unique = sorted(list(set(col_0)))
    respuesta_2 = []
    
    for x in letras_unique:
        respuesta_2.append((x,col_0.count(x)))

    return respuesta_2


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    col_0 = [data[i][0] for i in range(len(data))]
    col_1 = [int(data[i][1]) for i in range(len(data))]
    letras_unique = sorted(list(set(col_0)))

    respuesta_3 = []

    for letter in letras_unique:
        valor = 0
        for i in range(len(data)):
            if col_0[i] == letter:
                valor = valor + col_1[i]
        respuesta_3.append((letter, valor))

    return respuesta_3


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    meses = [data[i][2][5:7] for i in range(len(data))]
    respuesta_4 = []

    for mes in meses:
        respuesta_4.append((mes,meses.count(mes)))

    respuesta_4 = sorted(list(set(respuesta_4)))
    
    return respuesta_4


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    col_0 = [data[i][0] for i in range(len(data))]
    col_1 = [int(data[i][1]) for i in range(len(data))]
    letras_unique = sorted(list(set(col_0)))
    respuesta_5 = []

    for letter in letras_unique:
        maximo = min(col_1)
        minimo = max(col_1)
        for i in range(len(data)):
            if col_0[i] == letter:
                if col_1[i] > maximo:
                    maximo = col_1[i]    
                if col_1[i] < minimo:
                    minimo = col_1[i]
        respuesta_5.append((letter,maximo,minimo))

    return respuesta_5


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    col_4 = []
    col_4 = [data[i][4] for i in range(len(data))]
    col_4 = [line.split(",") for line in col_4]

    lista_col_4 = []
    lista_col_4_keys = []
    lista_col_4_values = []
    respuesta_6 = []

    for i in range(len(col_4)):
        for sublista in range(len(col_4[i])):
            lista_col_4.append(col_4[i][sublista])

    for e in range(len(lista_col_4)):
        lista_col_4_keys.append(lista_col_4[e][0:3])
        lista_col_4_values.append(int(lista_col_4[e][4:]))

    lista_col_4_keys = [line.replace(":", "") for line in lista_col_4_keys]

    col_4_unique_keys = sorted(list(set(lista_col_4_keys)))

    for key in col_4_unique_keys:
        maximo = min(lista_col_4_values)
        minimo = max(lista_col_4_values)
        for i in range(len(lista_col_4)):
            if lista_col_4_keys[i] == key:
                if lista_col_4_values[i] > maximo:
                    maximo = lista_col_4_values[i]
                if lista_col_4_values[i] < minimo:
                    minimo = lista_col_4_values[i]
        respuesta_6.append((key, minimo, maximo))

    return respuesta_6


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    col_0 = [data[i][0] for i in range(len(data))]
    col_1 = [int(data[i][1]) for i in range(len(data))]
    num_unique = list(set(col_1))
    respuesta_7 = []

    for numero in num_unique:
        letras_numero = []
        for i in range(len(col_0)):
            if col_1[i] == numero:
                letras_numero.append(col_0[i])
        respuesta_7.append((numero, letras_numero))

    return respuesta_7


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    col_0 = [data[i][0] for i in range(len(data))]
    col_1 = [int(data[i][1]) for i in range(len(data))]

    num_unique = list(set(col_1))
    respuesta_8 = []

    for numero in num_unique:
        letras_numero = []
        for i in range(len(col_0)):
            if col_1[i] == numero:
                letras_numero.append(col_0[i])
        letras_numero = sorted(list(set(letras_numero)))
        respuesta_8.append((numero, letras_numero))

    return respuesta_8


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    col_4 = [data[i][4] for i in range(len(data))]
    col_4 = [line.split(",") for line in col_4]

    lista_col_4 = []
    lista_col_4_keys = []
    lista_col_4_values = []
    respuesta_9 = []

    for i in range(len(col_4)):
        for sublista in range(len(col_4[i])):
            lista_col_4.append(col_4[i][sublista])

    for e in range(len(lista_col_4)):
        lista_col_4_keys.append(lista_col_4[e][0:3])
        lista_col_4_values.append(int(lista_col_4[e][4:]))

    lista_col_4_keys = [line.replace(":", "") for line in lista_col_4_keys]
    col_4_unique_keys = sorted(list(set(lista_col_4_keys)))

    for clave in col_4_unique_keys:
        contador = 0
        for i in range(len(lista_col_4_keys)):
            if lista_col_4_keys[i] == clave:
                contador = contador + 1
        respuesta_9.append((clave, contador))

    respuesta_9 = dict(respuesta_9)

    return respuesta_9

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    col_0 = [data[i][0] for i in range(len(data))]
    col_3 = [data[i][3] for i in range(len(data))]
    col_4 = [data[i][4] for i in range(len(data))]

    respuesta_10 = []

    for i in range(len(col_0)):
        respuesta_10.append((col_0[i],col_3[i].count(',')+1,col_4[i].count(',')+1))

    return respuesta_10


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    col_1 = [data[i][1] for i in range(len(data))]
    col_3 = [data[i][3] for i in range(len(data))]

    col_3 = [line.split(",") for line in col_3]

    letras = []
    respuesta_11 = []

    for i in range(len(col_3)):
        for letra in col_3[i]:
            letras.append(letra)

    letras_unique = sorted(list(set(letras)))

    for letra in letras_unique:
        contador = 0
        for i in range(len(col_1)):
            if col_3[i].count(letra)>0:
                contador = contador + int(col_1[i])
        respuesta_11.append((letra, contador))

    respuesta_11 = dict(respuesta_11)

    return respuesta_11


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    col_0 = [data[i][0] for i in range(len(data))]
    col_4 = [data[i][4] for i in range(len(data))]

    col_4 = [line.split(",") for line in col_4]

    letras_unique = sorted(list(set(col_0)))
    respuesta_12 = []

    for letra in letras_unique:
        contador = 0
        for i in range(len(col_0)):
            for e in range(len(col_4[i])):
                if col_0[i] == letra:
                    contador = contador + int(col_4[i][e][4:])
        respuesta_12.append((letra,contador))

    respuesta_12 = dict(respuesta_12)

    return respuesta_12
