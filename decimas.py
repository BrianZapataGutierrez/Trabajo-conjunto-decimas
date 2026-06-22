import os
import time

reservas =[]

def limpiar_pantalla(): 
    os.system('cls')

def calcular_categoria(total):
    if total < 200000:
        return "Economica"
    elif total <= 500000:
        return "Estandar"
    else:
        return "Premium"
    
def validar_codigo(codigo):
    return codigo.isdigit() and int(codigo) > 0 

def validar_nombre(nombre):
    return len(nombre.strip()) >=3 and nombre.replace("", "").isalpha()

def validar_noches(noches):
    return noches.isdigit () and int (noches) > 0

def validar_valor(valor):
    return valor.isdigit() and int (valor) > 0

def validar_total(total):
    return total > 0

def validar_categoria(categoria):
    return categoria in ["Economica","Estandar","Premium"]

def buscar_reserva(lista, codigo):
    for r in reservas:
        if r["codigo"] == codigo:
            return r
    return None

def registrar_reserva(lista):
    try:
        codigo = input("Codigo: ")
        if not validar_codigo(codigo) or buscar_reserva(codigo):
            print("Codigo invalido o ya existe")
            return
        
        nombre = input    ("Nombre : ").strip()
        noches = int(input("Noches: "))
        valor = int (input("Valor por noche: "))

        total = noches * valor 
        categoria = calcular_categoria(total)

        reserva = {"codigo": codigo, "nombre": nombre, "noches": noches,
                   "valor": valor, "total": total, "categoria": categoria}
        reservas.append(reserva)
        print(f"Listo! Total: ${total}, Categoria: {categoria}")
    except ValueError:
        print("ERROR: ingrese solo numeros donde corresponde ")