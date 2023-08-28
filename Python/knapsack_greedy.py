# Función que devuelve la cantidad máxima de objetos que se pueden llevar en la mochila
# Entrada: Lista de tuplas (valor, peso), capacidad de la mochila
# Salida: Dicciónario con el valor total de los objetos seleccionados y la lista de objetos seleccionados
# Complejidad: O(n*log(n))
def greedy_knapsack(items, capacity):
    # Calcula el valor/peso de cada objeto, agregamos tambien el valor y su peso
    # [valor, peso, valor/peso]
    value_weight_ratio = [[i[0], i[1], i[0] / i[1]] for i in items]

    # Ordenamos la lista de objetos de acuerdo a su valor/peso
    value_weight_ratio.sort(key=lambda elem : elem[-1], reverse=True)

    # Seleccionamos los objetos de mayor valor/peso hasta que no quepan en la mochila
    selected_items = []
    current_capacity = 0
    total_value = 0
    i = 0
    while current_capacity + value_weight_ratio[i][1] <= capacity: # Se repite hasta que llegue a la capacidad de la mochila
        selected_items.append(items.index((value_weight_ratio[i][0], value_weight_ratio[i][1]))) # Agregamos el producto seleccionado siempre y cuando quepa en la mochila
        current_capacity += value_weight_ratio[i][1]
        total_value += value_weight_ratio[i][0]
        i += 1

    return { "total_value" : total_value, "selected_items" : selected_items }

def main():
    # Prueba 1
    objects = [(7, 2), (8, 3), (10, 4), (12, 5)]
    capacity = 10
    result = greedy_knapsack(objects, capacity)
    print("Valor total:", result["total_value"])
    print("Objetos seleccionados:", result["selected_items"])
    
    # Prueba 2
    objects = [(4, 20), (9, 6), (11, 5), (13, 9), (15, 7)]
    capacity = 30
    result = greedy_knapsack(objects, capacity)
    print("Valor total:", result["total_value"])
    print("Objetos seleccionados:", result["selected_items"])

    # Prueba 3    
    objects = [(10, 269), (55, 95), (10, 4), (47, 60), (5, 32), (4, 23), (50, 72), (8, 80), (61, 62), (85, 65), (87, 46)]
    capacity = 300
    result = greedy_knapsack(objects, capacity)
    print("Valor total:", result["total_value"])
    print("Objetos seleccionados:", result["selected_items"])

    # Prueba 4
    objects = [(20, 878), (44, 92), (46, 4), (90, 43), (72, 83), (91, 84), (40, 68), (75, 92), (35, 82), (8, 6), (54, 44), (78, 32), (40, 18), (77, 56), (15, 83), (61, 25), (17, 96), (75, 70), (29, 48), (75, 14), (63, 58)]
    capacity = 100
    result = greedy_knapsack(objects, capacity)
    print("Valor total:", result["total_value"])
    print("Objetos seleccionados:", result["selected_items"])

if __name__ == '__main__':
    main()