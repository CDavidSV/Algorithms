# Función que devuelve la cantidad máxima de objetos que se pueden llevar en la mochila
# Entrada: Lista de tuplas (valor, peso), capacidad de la mochila
# Salida: Dicciónario con el valor total de los objetos seleccionados y la lista de objetos seleccionados
# Complejidad: O(n) en el caso promedio y O(n^2) en el peor caso
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

    # Seleccionamos los objetos de mayor valor/peso hasta que no quepan en la mochila
    for i in range(len(value_weight_ratio)):
        remaining_capacity = capacity - current_capacity # Capacidad restante de la mochila
        
        # Revisamos si el objeto actual cabe en la mochila verificando si su peso es menor o igual a la capacidad restante
        if current_capacity + value_weight_ratio[i][1] <= capacity:
            selected_items.append(items.index((value_weight_ratio[i][0], value_weight_ratio[i][1]))) # Agregamos el producto seleccionado siempre y cuando quepa en la mochila
            current_capacity += value_weight_ratio[i][1]
            total_value += value_weight_ratio[i][0]
        else: # Si no cabe y todavia queda espacio en la mochila, buscamos el siguiente objeto que quepa.
            # Esta es parte de la mejora del algoritmo ya que solo seleccionaba los primeros objetos que cabian en la mochila en base a su valor/peso
            # Esto tambien fue lo que aumentó la complejidad del algoritmo
            for j in range(i+1, len(value_weight_ratio)):
                if remaining_capacity >= value_weight_ratio[j][1]:
                    selected_items.append(items.index((value_weight_ratio[j][0], value_weight_ratio[j][1])))
                    current_capacity += value_weight_ratio[j][1]
                    total_value += value_weight_ratio[j][0]
                    break
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