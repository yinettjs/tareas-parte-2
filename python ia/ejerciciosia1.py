import math

# --- Conversión de números romanos ---
def roman_to_decimal(roman):
    valores = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }
    
    total = 0
    prev = 0
    
    for letra in reversed(roman):
        valor = valores[letra]
        if valor < prev:
            total -= valor
        else:
            total += valor
        prev = valor
    
    return total


# --- Clase Esfera ---
class Esfera:
    def __init__(self, radio):
        self.radio = radio
    
    def superficie(self):
        return 4 * math.pi * (self.radio ** 2)
    
    def volumen(self):
        return (4/3) * math.pi * (self.radio ** 3)
    
    def diametro(self):
        return 2 * self.radio


# --- Algoritmo Insertion Sort ---
def insertion_sort(lista):
    for i in range(1, len(lista)):
        j = i
        while j > 0 and lista[j-1] > lista[j]:
            lista[j], lista[j-1] = lista[j-1], lista[j]
            j -= 1
    return lista


# --- Menú principal ---
def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Convertir número romano a decimal")
        print("2. Calcular propiedades de una esfera")
        print("3. Ordenar lista con Insertion Sort")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            romano = input("Ingrese un número romano: ")
            print("Decimal:", roman_to_decimal(romano))
        
        elif opcion == "2":
            radio = float(input("Ingrese el radio de la esfera: "))
            esfera = Esfera(radio)
            print(f"Área de la superficie: {esfera.superficie():.2f}")
            print(f"Volumen: {esfera.volumen():.2f}")
            print(f"Diámetro: {esfera.diametro():.2f}")
        
        elif opcion == "3":
            datos = input("Ingrese números separados por espacio: ")
            lista = [int(x) for x in datos.split()]
            print("Lista ordenada:", insertion_sort(lista))
        
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida, intente de nuevo.")


# --- Ejecución del programa ---
if __name__ == "__main__":
    menu()
