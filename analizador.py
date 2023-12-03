import re
           
def analizar_variables(cadena, var, var_inv):
    try:
        pila = list(var.values())
        cadena = cadena.split()

        tipo = cadena[0]
        recorrido = []
        i = 0
        estados_pila = []
        
        while pila:
            x = pila[0]
            a = cadena[i]
            
            print(f"Pila: {pila[::-1]}")
            estados_pila.append(pila.copy())
            
            if len(pila) == 2:
                if tipo == "int" and re.match(r"([0-9]+)", a):
                    recorrido.append(var_inv[x])
                    pila.pop(0)
                    i += 1
                elif tipo == "string" and re.match(r'"([a-zA-Z0-9]+)"', a):
                    recorrido.append(var_inv[x])
                    pila.pop(0)
                    i += 1
                elif tipo == "boolean" and re.match(r"(true|false)", a):
                    recorrido.append(var_inv[x])
                    pila.pop(0)
                    i += 1
                elif tipo == "float" and re.match(r"([0-9]+\.[0-9]+)", a):
                    recorrido.append(var_inv[x])
                    pila.pop(0)
                    i += 1
                else:
                    raise ValueError(f"Error en la cadena: {a} no es un valor válido para tipo {tipo}")
            elif re.match(x, a):
                recorrido.append(var_inv[x])
                pila.pop(0)
                i += 1
            else:
                raise ValueError(f"Error en la cadena: Se esperaba {x} pero se encontró {a}")
        return True, recorrido, pila, estados_pila
    except Exception as e:
        return False, [str(e)], pila, estados_pila
    
    

def validar_ifs(cadena, ifs, ifs_inv):
    try:
        pila = list(ifs.values())
        cadena = cadena.split()
        estados_pila = []
        recorrido = []
        i = 0

        while pila and i < len(cadena):
            x = pila[0]
            a = cadena[i]
            estados_pila.append(pila.copy())
            if x == ifs["Contenido"]:
                if re.match(x, a):
                    recorrido.append(ifs_inv[x])
                    pila.pop(0)
                    i += 1
                else:
                    raise ValueError(f"Error en la cadena: Se esperaba {x} pero se encontró {a}")
            elif re.match(x, a):
                recorrido.append(ifs_inv[x])
                pila.pop(0)
                i += 1
            else:
                raise ValueError(f"Error en la cadena: Se esperaba {x} pero se encontró {a}")

        if not pila and i == len(cadena):
            # Check if the entire string has been processed and the stack is empty
            return True, recorrido, pila, estados_pila
        else:
            raise ValueError("Error: Incompleto o incorrecto.")

    except Exception as e:
        return False, [str(e)], pila, estados_pila


def validar_ifelse(cadena, ifelse, ifelse_inv):
    try:
        pila = list(ifelse.values())
        cadena = cadena.split()
        estados_pila = []
        recorrido = []
        i = 0

        while pila and i < len(cadena):
            x = pila[0]
            a = cadena[i]
            estados_pila.append(pila.copy())
            if re.match(x, a):
                recorrido.append(ifelse_inv[x])
                pila.pop(0)
                i += 1
            else:
                raise ValueError(f"Error en la cadena: Se esperaba {x} pero se encontró {a}")

        return True, recorrido, pila, estados_pila
    except Exception as e:
        return False, [str(e)], pila, estados_pila



def analizar_ciclo(cadena, fors, fors_inv):
    try:
        pila = list(fors.values())
        cadena = cadena.split()
        estados_pila = []
        recorrido = []
        i = 0

        while pila:
            x = pila[0]
            a = cadena[i]
            print(f"Pila: {pila[::-1]}")
            estados_pila.append(pila.copy())
            if re.match(x, a):
                recorrido.append(fors_inv[x])
                pila.pop(0)
                i += 1
            else:
                raise ValueError(f"Error en la cadena: Se esperaba {x} pero se encontró {a}")
        return True, recorrido,pila, estados_pila
    except Exception as e:
        return False, [str(e)],pila, estados_pila

def analizar_bucle(cadena, whiles, whiles_inv):
    try:
        pila = list(whiles.values())
        cadena = cadena.split()
        estados_pila = []
        recorrido = []
        i = 0

        while pila:
            x = pila[0]
            a = cadena[i]
            print(f"Pila: {pila[::-1]}")
            estados_pila.append(pila.copy())
            if re.match(x, a):
                recorrido.append(whiles_inv[x])
                pila.pop(0)
                i += 1
            else:
                raise ValueError(f"Error en la cadena: Se esperaba {x} pero se encontró {a}")
        return True, recorrido, pila, estados_pila
    except Exception as e:
        return False, [str(e)], pila, estados_pila

def analizar_declaracion_funciones(cadena, func, func_inv):
    try:
        pila = list(func.values())
        cadena = cadena.split()
        estados_pila = []
        recorrido = []
        i = 0

        while pila and i < len(cadena):
            x = pila[0]
            a = cadena[i]
            print(f"Pila: {pila[::-1]}")
            estados_pila.append(pila.copy())
            if x == func["Contenido"]:
                if re.match(x, a):
                    recorrido.append(func_inv[x])
                    pila.pop(0)
                    i += 1
                else:
                    raise ValueError(f"Error en la cadena: Se esperaba {x} pero se encontró {a}")
            elif re.match(x, a):
                recorrido.append(func_inv[x])
                pila.pop(0)
                i += 1
            else:
                raise ValueError(f"Error en la cadena: Se esperaba {x} pero se encontró {a}")

        return True, recorrido, pila, estados_pila
    except Exception as e:
        return False, [str(e)], pila, estados_pila

def analizar_declaracion_funciones_return(cadena, funcr, funcr_inv):
    try:
        pila = list(funcr.values())
        cadena = cadena.split()
        estados_pila = []
        recorrido = []
        i = 0

        while pila and i < len(cadena):
            x = pila[0]
            a = cadena[i]            
            print(f"Pila: {pila[::-1]}")
            estados_pila.append(pila.copy())
            if x == funcr["Contenido"]:
                if re.match(x, a):
                    recorrido.append(funcr_inv[x])
                    pila.pop(0)
                    i += 1
                else:
                    raise ValueError(f"Error en la cadena: Se esperaba {x} pero se encontró {a}")
            elif x == funcr["PuntoComa"]:
                if re.match(x, a):
                    recorrido.append(funcr_inv[x])
                    pila.pop(0)
                    i += 1
                else:
                    raise ValueError(f"Error en la cadena: Se esperaba {x} pero se encontró {a}")
            elif re.match(x, a):
                recorrido.append(funcr_inv[x])
                pila.pop(0)
                i += 1
            else:
                raise ValueError(f"Error en la cadena: Se esperaba {x} pero se encontró {a}")

        return True, recorrido, pila, estados_pila
    except Exception as e:
        return False, [str(e)], pila, estados_pila

    
def null_function():
    return False, [], [], []