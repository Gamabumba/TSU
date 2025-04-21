import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
nodes = list(range(12))
G.add_nodes_from(nodes)

# Грани с формой центральности
edges = [
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 5),  # Линейная часть
    (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11),  # Продолжение линейной части
    (1, 3), (3, 5), (5, 7), (7, 9), (9, 11),  # Дополнительные связи для "горба"
    (2, 4), (4, 6), (6, 8), (8, 10)  # Дополнительные связи для "ямы"
]
G.add_edges_from(edges)

# Вычисление центральности в собственных векторах
eigenvector_centrality = nx.eigenvector_centrality(G)
sorted_eigenvector_centrality = dict(sorted(eigenvector_centrality.items(), key=lambda item: item[1]))

# Вывод центральности для каждого
print("Центральность в собственных векторах:")
for node, centrality in sorted_eigenvector_centrality.items():
    print(f"Узел {node}: {centrality:.4f}")

# Узлы с самой низкой центральностью (начало "ямы")
print("\nКлючевые точки:")
print(f"Узел с минимальной центральностью: Узел 0, Центральность: {sorted_eigenvector_centrality[0]:.4f}")
print(f"Узел с минимальной центральностью: Узел 11, Центральность: {sorted_eigenvector_centrality[11]:.4f}")

# Узлы с увеличением центральности (начало "горба")
print(f"Узел с низкой центральностью: Узел 1, Центральность: {sorted_eigenvector_centrality[1]:.4f}")
print(f"Узел с низкой центральностью: Узел 10, Центральность: {sorted_eigenvector_centrality[10]:.4f}")

# Узлы с максимальной центральностью (пик "горба")
print(f"Узел с максимальной центральностью: Узел 5, Центральность: {sorted_eigenvector_centrality[5]:.4f}")
print(f"Узел с максимальной центральностью: Узел 6, Центральность: {sorted_eigenvector_centrality[6]:.4f}")

# Узлы с уменьшением центральности (конец "горба")
print(f"Узел с высокой центральностью: Узел 4, Центральность: {sorted_eigenvector_centrality[4]:.4f}")
print(f"Узел с высокой центральностью: Узел 7, Центральность: {sorted_eigenvector_centrality[7]:.4f}")

# Граф
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_weight='bold')
plt.show()
