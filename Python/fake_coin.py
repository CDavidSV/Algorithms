import math

# Función que devuelve el índice de la moneda falsa
# Entrada: Array de enteros que representan el peso de cada moneda
# Salida: Índice de la moneda falsa
# Complejidad: O(n*log(n))
def fake_coin(coinArray):
    # Declaramos un arreglo de peso para cada subarreglo (3 subarreglos).
    weightArray = []

    # Para calccular el peso de los 3 subarreglos, recorremos el arreglo de monedas y sumamos el peso de cada moneda correspondiente a cada subarreglo.
    currentWeight = 0
    devisor = math.floor(len(coinArray) / 3)
    for i, v in enumerate(coinArray):
        currentWeight += v
        if (i + 1) % devisor == 0: # Determinamos si ya se completó el peso de un subarreglo
            weightArray.append(currentWeight)
            currentWeight = 0
    weightArray[2] += currentWeight # Agregamos el peso restante al último subarreglo

    
    sortedWeightArray = weightArray.copy()
    sortedWeightArray.sort() # Obtenemos el arreglo ordenado de menor a mayor.
    subArrayIndex = None
    
    # Buscamos el subarreglo que tiene peso diferente
    for i in range(0, len(weightArray)): # Comparamos el peso del arreglo ordenado con el arreglo original para asi poder obtener el índice del subarreglo que tiene peso diferente.
        if sortedWeightArray[1] != weightArray[i]:
            subArrayIndex = i
            break

    # Si el divisor es 1, significa que el indice de la moneda falsa es el mismo que el indice del subarreglo que tiene peso diferente.
    if devisor == 1:
        return subArrayIndex
    
    # Dependiendo del subarreglo que tiene peso diferente, llamamos recursivamente a la función fake_coin() con el subarreglo correspondiente.
    match subArrayIndex:
        case 0:
            result = fake_coin(coinArray[0:devisor])
            return result if result != None else None
        case 1:
            result = fake_coin(coinArray[devisor:devisor * 2])
            return result + devisor if result != None else None
        case 2:
            result = fake_coin(coinArray[devisor * 2:])
            return result + devisor * 2 if result != None else None
        case _:
            return None

def main():
    # Prueba 1
    coinArray = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5] # Todas las monedas son reales
    print(fake_coin(coinArray))

    # Prueba 2
    coinArray = [5, 5, 5, 5, 5, 5, 5, 5, 5, 3] # 9ma moneda es falsa
    print(fake_coin(coinArray))

    # Prueba 3
    coinArray = [5, 5, 5, 5, 5, 5, 5, 5, 3, 5] # 8va moneda es falsa
    print(fake_coin(coinArray))

    # Prueba 4
    coinArray = [5, 5, 5, 5, 5, 5, 5, 3, 5, 5] # 7ma moneda es falsa
    print(fake_coin(coinArray))

    # Prueba 5
    coinArray = [5, 5, 5, 5, 5, 5, 3, 5, 5, 5] # 6ta moneda es falsa
    print(fake_coin(coinArray))

if __name__ == '__main__':
    main()