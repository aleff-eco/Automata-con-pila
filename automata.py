import re

var = {
    "Tipo": r"int|string|boolean|float",
    "Nombre": r"[a-zA-Z][a-zA-Z0-9_]*",
    "Igual": r"=",
    "Valor": "",
    "PuntoComa": r";"
}
var_inv = {v: k for k, v in var.items()}

def variables(cadena):
    try:
        pila = list(var.values())
        cadena = cadena.split()

        tipo = cadena[0]
        recorrido = []
        i = 0

        while pila:
            x = pila[0]
            a = cadena[i]

            print(f"Pila: {pila[::-1]}")

            if len(pila) == 2:
                if tipo == "int":
                    if re.match(r"([0-9]+)", a):
                        recorrido.append(var_inv[x])
                        pila.pop(0)
                        i += 1
                    else:
                        raise ValueError(f"Error en la cadena: {a} no es un valor válido para tipo {tipo}")
                elif tipo == "string":
                    if re.match(r'"([a-zA-Z0-9]+)"', a):
                        recorrido.append(var_inv[x])
                        pila.pop(0)
                        i += 1
                    else:
                        raise ValueError(f"Error en la cadena: {a} no es un valor válido para tipo {tipo}")
                elif tipo == "boolean":
                    if re.match(r"(true|false)", a):
                        recorrido.append(var_inv[x])
                        pila.pop(0)
                        i += 1
                    else:
                        raise ValueError(f"Error en la cadena: {a} no es un valor válido para tipo {tipo}")
                elif tipo == "float":
                    if re.match(r"([0-9]+\.[0-9]+)", a):
                        recorrido.append(var_inv[x])
                        pila.pop(0)
                        i += 1
                    else:
                        raise ValueError(f"Error en la cadena: {a} no es un valor válido para tipo {tipo}")
                else:
                    raise ValueError(f"Error en la cadena: Tipo no reconocido {tipo}")
            elif re.match(x, a):
                recorrido.append(var_inv[x])
                pila.pop(0)
                i += 1
            else:
                raise ValueError(f"Error en la cadena: Se esperaba {x} pero se encontró {a}")
        return True, recorrido
    except Exception as e:
        return False, [str(e)]
    
ifs = {
    "IF": r"if",
    "Nombre": r"[a-zA-Z][a-zA-Z0-9_]*",
    "Simbolo": r"[<|>|==|<=|>=]",
    "Digito": r"[0-9]+",
    "Puntos": r":",
    "Contenido": r"C",
    "Else": r"else",
    "DosPuntos": r":",
    "MasContenido": r"MC",
}
ifs_inv = {v: k for k, v in ifs.items()}

def condicional(cadena):
    try:
        pila = list(ifs.values())
        cadena = cadena.split()

        recorrido = []
        i = 0

        while pila:
            x = pila[0]
            if i < len(cadena):
                a = cadena[i]
                if x in {"Else", "MasContenido"}:
                    if x == "Else" and a == "else":
                        pila.pop(0)
                        recorrido.append(ifs_inv[x])
                        continue
                    elif x == "MasContenido":
                        recorrido.append(ifs_inv[x])
                        pila.pop(0)
                        i += 1
                        continue

                print(f"Pila: {pila[::-1]}")

                if re.match(x, a):
                    recorrido.append(ifs_inv[x])
                    pila.pop(0)
                    i += 1
                else:
                    raise ValueError(f"Error en la cadena: Se esperaba {x} pero se encontró {a}")
            else:
                break
        return True, recorrido
    except Exception as e:
        return False, [str(e)]

fors = {
    "FOR": r"for",
    "Nombre1": r"[a-zA-Z][a-zA-Z0-9_]*",
    "In": r"in",
    "Nombre": r"[a-zA-Z][a-zA-Z0-9_]*",
    "Puntos": r":",
    "Contenido": r"MC",
}
fors_inv = {v: k for k, v in fors.items()}

def ciclo(cadena):
    try:
        pila = list(fors.values())
        cadena = cadena.split()

        recorrido = []
        i = 0

        while pila:
            x = pila[0]
            a = cadena[i]

            print(f"Pila: {pila[::-1]}")

            if re.match(x, a):
                recorrido.append(fors_inv[x])
                pila.pop(0)
                i += 1
            else:
                raise ValueError(f"Error en la cadena: Se esperaba {x} pero se encontró {a}")
        return True, recorrido
    except Exception as e:
        return False, [str(e)]

whiles = {
    "WHILE": r"while",
    "Nombre": r"[a-zA-Z][a-zA-Z0-9_]*",
    "Simbolo": r"[<|>|==|<=|>=]",
    "Digito": r"[0-9]+",
    "Puntos": r":",
    "Contenido": r"C",
}
whiles_inv = {v: k for k, v in whiles.items()}

def bucle(cadena):
    try:
        pila = list(whiles.values())
        cadena = cadena.split()

        recorrido = []
        i = 0

        while pila:
            x = pila[0]
            a = cadena[i]

            print(f"Pila: {pila[::-1]}")

            if re.match(x, a):
                recorrido.append(whiles_inv[x])
                pila.pop(0)
                i += 1
            else:
                raise ValueError(f"Error en la cadena: Se esperaba {x} pero se encontró {a}")
        return True, recorrido
    except Exception as e:
        return False, [str(e)]


func = {
    "Def": r"def",
    "Nombre1": r"[a-zA-Z][a-zA-Z0-9_]*",
    "Parentesis": r"\(\)",
    "Puntos": r":",
    "Contenido": r"C",

    "Return": r"return",
    "Nombre": r"[a-zA-Z][a-zA-Z0-9_]*",
    "PuntoComa": r";",
}
func_inv = {v: k for k, v in func.items()}

def funcion(cadena):
    try:
        pila = list(func.values())
        cadena = cadena.split()

        recorrido = []
        i = 0

        while pila:
            x = pila[0]

            if i < len(cadena):
                a = cadena[i]
                if x in {"Return", "Nombre", "PuntoComa"}:
                    if x == "Return" and a == "return":
                        pila.pop(0)
                        recorrido.append(func_inv[x])
                        continue
                    elif x == "Nombre":
                        recorrido.append(func_inv[x])
                        pila.pop(0)
                        i += 1
                        continue
                    elif x == "PuntoComa" and a == ";":
                        recorrido.append(func_inv[x])
                        pila.pop(0)
                        i += 1
                        continue

                print(f"Pila: {pila[::-1]}")

                if re.match(x, a):
                    recorrido.append(func_inv[x])
                    pila.pop(0)
                    i += 1
                else:
                    raise ValueError(f"Error en la cadena: Se esperaba {x} pero se encontró {a}")
            else:
                break
        return True, recorrido
    except Exception as e:
        return False, [str(e)]


def imprimir_resultado(tipo, resultado, recorrido):
    print(f"Cadena evaluada como: {tipo}")
    print(f"Resultado: {resultado}")
    print(f"Recorrido: {recorrido[::-1]}")
    print()

def evaluar_cadena(cadena):
    try:
        if cadena.startswith("if"):
            resultado, recorrido = condicional(cadena)
            imprimir_resultado("Condicional If", resultado, recorrido)
        elif cadena.startswith("for"):
            resultado, recorrido = ciclo(cadena)
            imprimir_resultado("Ciclo for ", resultado, recorrido)
        elif cadena.startswith("while"):
            resultado, recorrido = bucle(cadena)
            imprimir_resultado("Bucle while", resultado, recorrido)
        elif cadena.startswith("def"):
            resultado, recorrido = funcion(cadena)
            imprimir_resultado("Definicion de funcion", resultado, recorrido)
        else:
            resultado, recorrido = variables(cadena)
            imprimir_resultado("Definicion de variable", resultado, recorrido)
    except Exception as e:
        print(f"Error general: {e}")

if __name__ == '__main__':
    cadena = input("Ingrese la cadena a evaluar: ")
    evaluar_cadena(cadena)
