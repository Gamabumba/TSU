import networkx as nx
import matplotlib.pyplot as plt


n = 30
p = 0.85

G = nx.erdos_renyi_graph(n, p)

# Вычисление средней степени вершины
average_degree = sum(dict(G.degree()).values()) / n

# Теоретическое значение средней степени вершины для модели Эрдёша-Реньи
theoretical_average_degree = (n - 1) * p

# Вывод результатов
print(f"Средняя степень вершины (по вычислению): {average_degree:.2f}")
print(f"Теоретическое значение средней степени вершины: {theoretical_average_degree:.2f}")

# Визуализация графа
pos = nx.spring_layout(G)
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')
plt.title("Граф Эрдёша-Реньи с n=30 и p=0.85")
plt.show()

# Вывод по работе и графу
print("\nВывод:")
print(f"Для графа Эрдёша-Реньи с {n} вершинами и вероятностью ребра {p},")
print(f"средняя степень вершины, вычисленная по программе, составляет {average_degree:.2f}.")
print(f"Теоретическое значение средней степени вершины согласно формуле (n-1)*p равно {theoretical_average_degree:.2f}.")
print("Как видно, вычисленное значение хорошо согласуется с теоретическим.")
