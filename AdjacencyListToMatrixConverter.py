# Adjacency List to Matrix Converter

def adjacency_list_to_matrix(adj_list):
    # Determine the number of vertices
    v = len(adj_list)
    
    # Initialize a V x V matrix with 0s
    matrix = [[0 for _ in range(v)] for _ in range(v)]
    
    # Fill the matrix: iterate through each node and its neighbors
    for node, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            matrix[node][neighbor] = 1
            
    return matrix

# Example usage:
# Adjacency List: Node 0 -> [1, 2], Node 1 -> [2], Node 2 -> [0]
adj_list = [[1, 2], [2], [0]]
print(adjacency_list_to_matrix(adj_list))


# ***************************************************
# ***************************************************


def adjacency_list_to_matrix(adj_list):
    # Determine the number of vertices
    v = len(adj_list)
    
    # Initialize a V x V matrix with 0s
    matrix = [[0 for _ in range(v)] for _ in range(v)]
    
    # Fill the matrix: iterate through each node and its neighbors
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1
        print(matrix[node])
            
    return matrix

# Example usage:
# Adjacency List: Node 0 -> [1, 2], Node 1 -> [2], Node 2 -> [0]
adj_list = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2]
}
print(adjacency_list_to_matrix(adj_list))