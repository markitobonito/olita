#operaciones de entrada y salida -> punto de vista del software
from typing import Union
from random import randint
palabras=["arquitectura","computadoras", "universidad","Telecomunicaciones","alumnos","clases"]

palabra= palabras[randint(0,len(palabras)-1)]
intentos = 5
palabra_lista=["_"]*len(palabra)

def busca_letra(p: str, l: str, p_lista: list[str]) -> Union[list[str], bool]:
    palabra_encontrada=False
    for idx in range(len(palabra)):
        if l == p[idx]:
            p_lista[idx]=l
            palabra_encontrada= True
    return p_lista, palabra_encontrada


if __name__ == '__main__':
    while True:
        print(f"{''.join(palabra_lista)}\n\nCantidad de intentos:{intentos}\n")
        var = input("Por favor ingrese una letra:")
        while len(var) != 1:
            var =input("Por favor ingrese una letra:")
        palabra_lista,encontrada= busca_letra(palabra,var,palabra_lista)
        if not var in palabra:
            intentos -=1
            print("Letra ingresada no pertenece a la palabra:")
        if intentos ==0:
            print("PERDISTE PI¹⁰")    
            exit(0)
        if not "_" in palabra_lista:
            print(f"Felicitaciones, ha encontrado la palabra: , {palabra}")
            exit(0)
















