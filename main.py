# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from interfaz import Ui_Automata
from analizador import analizar_variables, validar_ifs, validar_ifelse, analizar_ciclo, analizar_bucle, null_function, analizar_declaracion_funciones_return, analizar_declaracion_funciones
    

var = {
    "Tipo": r"int|string|boolean|float",
    "Nombre": r"[a-zA-Z][a-zA-Z0-9_]*",
    "Igual": r"=",
    "Valor": "",
    "PuntoComa": r";"
}
var_inv = {v: k for k, v in var.items()}

ifs = {
    "IF": r"if",
    "Nombre": r"[a-zA-Z][a-zA-Z0-9_]*",
    "Simbolo": r"[<|>|==|<=|>=]",
    "Digito": r"[0-9]+",
    "Puntos": r":",
    "Contenido": r"C"
}
ifs_inv = {v: k for k, v in ifs.items()}

ifelse = {
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
ifelse_inv = {v: k for k, v in ifelse.items()}

fors = {
    "For": r"for",
    "Nombre1": r"[a-zA-Z][a-zA-Z0-9_]*",
    "In": r"in",
    "Nombre": r"[a-zA-Z][a-zA-Z0-9_]*",
    "Puntos": r":",
    "Contenido": r"C",
}
fors_inv = {v: k for k, v in fors.items()}

whiles = {
    "WHILE": r"while",
    "Nombre": r"[a-zA-Z][a-zA-Z0-9_]*",
    "Simbolo": r"[<|>|==|<=|>=]",
    "Digito": r"[0-9]+",
    "Puntos": r":",
    "Contenido": r"C",
}
whiles_inv = {v: k for k, v in whiles.items()}

func = {
    "Def": r"def",
    "Nombre1": r"[a-zA-Z][a-zA-Z0-9_]*",
    "Parentesis": r"()",
    "Puntos": r":",
    "Contenido": r"C"
}
func_inv = {v: k for k, v in func.items()}

funcr = {
    "Def": r"def",
    "Nombre1": r"[a-zA-Z][a-zA-Z0-9_]*",
    "Parentesis": r"()",
    "Puntos": r":",
    "Contenido": r"C",

    "Return": r"return",
    "Nombre": r"[a-zA-Z][a-zA-Z0-9_]*",
    "PuntoComa": r";",
}
funcr_inv = {v: k for k, v in funcr.items()}
        
class MyApp(QMainWindow, Ui_Automata):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.send.clicked.connect(self.verificar)


    def verificar(self):
        cadena = self.input.text()
        
        try:
            if cadena.endswith("MC"):
                resultado, recorrido, pila, estados_pila  = validar_ifelse(cadena, ifelse, ifelse_inv)
                tipo = "Condicional If con Else"
            elif cadena.startswith("if"):
                resultado, recorrido, pila,estados_pila  = validar_ifs(cadena, ifs, ifs_inv)
                tipo = "Condicional If"
            elif cadena.startswith("for"):
                resultado, recorrido, pila,estados_pila = analizar_ciclo(cadena, fors, fors_inv)
                tipo = "Ciclo for"
            elif cadena.startswith("while"):
                resultado, recorrido, pila,estados_pila = analizar_bucle(cadena, whiles, whiles_inv)
                tipo = "Bucle while"
            elif cadena.endswith("C"):
                resultado, recorrido, pila,estados_pila = analizar_declaracion_funciones(cadena, func, func_inv)
                tipo = "Definicion de funcion"
            elif cadena.endswith(";") and cadena.startswith("def"):
                resultado, recorrido, pila,estados_pila = analizar_declaracion_funciones_return(cadena, funcr, funcr_inv)
                tipo = "Definicion de funcion con return"
            elif cadena.startswith(("int", "string", "boolean", "float")):
                resultado, recorrido, pila,estados_pila = analizar_variables(cadena, var, var_inv)
                tipo = "Definicion de variable"
            else:
                tipo = "Desconocido"
                resultado, recorrido, pila, estados_pila = null_function()
                
                
            #clear
            self.recorrido.clear() 
            self.resultado.clear()
            self.cadena_evaluar.clear()
            self.tipo_cadena.clear() 
            
            #additem
            self.cadena_evaluar.addItem(cadena)
            self.tipo_cadena.addItem(tipo)
            if resultado:
                resultado = "VALIDO"
            else: 
                resultado = "INVALIDO"
                
            self.resultado.addItem(resultado)
            self.recorrido.addItem(f"Para la cadena: {cadena}")
            self.recorrido.addItem(f"Realiza el recorrido:")
            self.recorrido.addItems(recorrido[::-1])
            self.recorrido.addItem(f"")
            for estado in estados_pila:
                self.recorrido.addItem(f"Pila: {estado[::-1]}")
                
        except Exception as e:
            self.recorrido.addItems([f"Error general: {e}"])

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
