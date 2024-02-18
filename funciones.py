from clase import *
from tkinter import *
import os.path
import pickle

def es_letra(palabra):
    switch = False
    letras = "abcdefghojklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ"

    for i in palabra:
        if i in letras:
            switch = True

    return switch


def es_minuscula(palabra):
    minusculas = "abcdefghojklmnñopqrstuvwxyzáéíóú"
    switch = False

    for i in palabra:
        if i in minusculas:
            switch = True

    return switch


def shell_sort(vec):
    n = len(vec)
    h = 1
    while h <= n // 9:
        h = 3 * h + 1
    while h > 0:
        for j in range(h, n):
            y = vec[j]
            k = j - h
            while k >= 0 and y.km < vec[k].km:
                vec[k + h] = vec[k]
                k -= h
            vec[k + h] = y
        h //= 3


def obtener_ticket(line):
    codigo = line[0]
    patente = line[1]
    tipo_vehiculo = line[2]
    forma_pago = line[3]
    pais_cabina = line[4]
    distancia = line[5]
    ticket = Ticket(codigo, patente, tipo_vehiculo, forma_pago, pais_cabina, distancia)
    return ticket


def obtener_texto(ruta):
    archivo = open(ruta, "rt")
    texto = archivo.readlines()
    archivo.close()
    return texto


def aniadir_binario(obj, archivo):
    archivo = open(archivo, "ab")
    pickle.dump(obj, archivo)
    archivo.close()


def crear_archivo(archivo):
    i = 0

    texto = obtener_texto(archivo)

    archivob = open("archivo_binario.dat", "wb")
    for line in texto:
        i += 1
        if line[-1] == "\n":
            line = line[:-1]
        line = line.split(",")
        if i > 2:
            ticket = obtener_ticket(line)
            pickle.dump(ticket, archivob)
    archivob.close()


def cargar_datos(archivo, id_cargado, patente_cargada, tipo_cargado, pago_cargado, pais_cargado, km_cargado):
    ticket = Ticket(id_cargado, patente_cargada, tipo_cargado, pago_cargado, pais_cargado, km_cargado)
    aniadir_binario(ticket, archivo)


def mostrar_datos(archivo, main_txt):
    binario = open(archivo, 'rb')
    tamanio = os.path.getsize(archivo)
    i = 1

    while binario.tell() < tamanio:
        ticket = pickle.load(binario)
        main_txt.insert(f"{i}.0",f"{ticket}\n")
        i+=1

    binario.close()


def buscar_patente(archivo, patente, main_text):
    binario = open(archivo, "rb")
    tamanio = os.path.getsize(archivo)
    main_text["state"] = "normal"
    main_text.delete("1.0","end")
    cant_patentes = 0

    main_text.insert("1.0",f"Las pantentes iguales a {patente} son:\n")

    while binario.tell() < tamanio:
        ticket = pickle.load(binario)
        if ticket.patente == patente:
            cant_patentes += 1
            main_text.insert(f"{cant_patentes+1}.0",f"{ticket}\n")

    binario.close()

    main_text.insert(f"{cant_patentes+1}.0",f"Cantidad de patentes: {cant_patentes}\n")
    main_text["state"] = "disabled"


def buscar_codigo(archivo, codigo, main_text):
    binario = open(archivo, "rb")
    tamanio = os.path.getsize(archivo)
    main_text["state"] = "normal"
    main_text.delete("1.0","end")

    while binario.tell() < tamanio:
        ticket = pickle.load(binario)
        if ticket.codigo == codigo:
            main_text.insert("1.0",f"El registro con el código {codigo} es:\n{ticket}")
            main_text["state"] = "disabled"
            binario.close()
            return

    binario.close()
    main_text.insert("1.0","No se ha encontrado el registro deseado")
    main_text["state"] = "disabled"


def generar_vehiculo_cabina(archivo):
    binario = open(archivo, "rb")
    tamanio = os.path.getsize(archivo)
    mat = [[0] * 3 for i in range(5)]

    while binario.tell() < tamanio:
        ticket = pickle.load(binario)
        mat[int(ticket.pais)][int(ticket.tipo)] += 1

    binario.close()
    return mat


def mostrar_vehiculo_cabina(archivo, main_text):
    paises = ("Argentina", "Chile", "Brasil", "Bolivia", "Paraguay", "Uruguay", "Otro")
    vehiculos = ("motocicleta", "automóvil", "camión")
    mat = generar_vehiculo_cabina(archivo)
    t = 1
    
    for i in range(5):
        main_text.insert(f"{t}.0",f"Tipos de vehículos de {paises[i]}:\n")
        t += 1
        for j in range(3):
            t += 1
            if mat[i][j] != 0:
                main_text.insert(f"{t}.0",f"Cantidad de vehículos tipo {vehiculos[j]}: {mat[i][j]}\n")


def mostrar_filas_columnas_matriz(archivo, main_text):
    p = ("Argentina", "Chile", "Brasil", "Bolivia", "Paraguay", "Uruguay", "Otro")
    v = ("motocicleta", "automóvil", "camión")
    mat = generar_vehiculo_cabina(archivo)
    vehiculos = 3 * [0]
    paises = 5 * [0]

    for i in range(5):
        for j in range(3):
            paises[i] += mat[i][j]
            vehiculos[j] += mat[i][j]

    for auto in range(len(vehiculos)):
       main_text.insert(f"{auto}.0",f"Cantidad de vehículos tipo {v[auto]}: {vehiculos[auto]}\n")

    for pais in range(len(paises)):
       main_text.insert(f"{pais + auto}.0",f"Cantidad de vehículos de {p[pais]}: {paises[pais]}\n")


def promedio_distancia(archivo, main_text):
    binario = open(archivo, "rb")
    tamanio = os.path.getsize(archivo)
    distancia_total = acu_tick = promedio = 0
    vec_acu = []

    while binario.tell() < tamanio:
        ticket = pickle.load(binario)
        distancia_total += int(ticket.km)
        acu_tick += 1

    binario.close()

    if acu_tick > 0:
        promedio = round(distancia_total / acu_tick, 2)

    binario = open(archivo, "rb")

    while binario.tell() < tamanio:
        ticket = pickle.load(binario)
        if int(ticket.km) > promedio:
            vec_acu.append(ticket)

    binario.close()

    shell_sort(vec_acu)

    for i in range(len(vec_acu)):
        main_text.insert(f"{i}.0",f"{vec_acu[i]}\n")

    main_text.insert(f"{len(vec_acu)+1}.0",f"La distancia promedio desde la última cabina recorrida es: {promedio}")

#Notas
#Verificar el tema de que se puede añadir una patente con la misma id
