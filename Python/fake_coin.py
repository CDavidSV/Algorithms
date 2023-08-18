import math

# Función que devuelve el índice de la moneda falsa
# Entrada: Array de enteros que representan el peso de cada moneda
# Salida: Índice de la moneda falsa
# Complejidad: O(n*log(n))
def fake_coin(coinArray):
    weightArray = []
    currentWeight = 0
    devisor = math.floor(len(coinArray) / 3)
    for i, v in enumerate(coinArray):
        currentWeight += v
        if (i + 1) % devisor == 0:
            weightArray.append(currentWeight)
            currentWeight = 0
    weightArray[2] += currentWeight

    sortedWeightArray = weightArray.copy()
    sortedWeightArray.sort()
    subArrayIndex = None

    for i in range(0, len(weightArray)):
        if sortedWeightArray[1] != weightArray[i]:
            subArrayIndex = i
            break

    if devisor == 1:
        return subArrayIndex
    
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