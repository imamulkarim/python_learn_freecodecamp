# Implement the Depth-First Search Algorithm

def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    # Mark the current node as visited
    visited.add(node)
    print(node, end=" ")

    # Recur for all the neighbors that haven't been visited
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Example Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Recursive DFS Traversal:")
dfs_recursive(graph, 'A')


# ******************************************************************


def dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    
    while stack:
        # Pop the last element added (LIFO)
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            #print(visited)
            
            # Add neighbors to the stack
            # Reversing ensures neighbors are visited in the same order as recursive DFS
            
            for index,neighbor in enumerate((graph[node])):
                if index not in visited and neighbor> 0:
                    stack.append(index)

    return list(visited)

# Example Graph (Adjacency List)
graph = [[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]]
#          .0 :1            1:0, 1:2     2:1,2:3         3:2

print("Recursive DFS Traversal:")
print( dfs(graph, 1))