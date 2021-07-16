from math import floor
edges = []
while True:
    line = input()
    if line.startswith('c '):
        continue
    elif line.startswith('p '):
        line = line.split()
        n_vertix, n_edge = int(line[-2]), int(line[-1])
        break
        
for i in range(n_edge):
    line = input()
    line = line.split()
    edges.append([int(line[-2]), int(line[-1])])
        
def score(solution):
    penalty = 0
    for edge in edges:
        if (edge[0] in solution[0] and edge[1] in solution[1]) or \
        (edge[0] in solution[1] and edge[1] in solution[0]):
            penalty += 1
    return penalty

def create_neighbors(solution):
    group_a = solution[0]
    group_b = solution[1]
    neighbors = [[[], []] for _ in range(len(group_a)*len(group_b))]
    swapped_pair = []
    i = 0
    for a in range(len(group_a)):
        for b in range(len(group_b)):
            neighbors[i][0] = list(group_a)
            neighbors[i][1] = list(group_b)
            temp = neighbors[i][0][a]
            neighbors[i][0][a] = neighbors[i][1][b]
            neighbors[i][1][b] = temp
            swapped_pair.append([neighbors[i][0][a], neighbors[i][1][b]])
            i += 1
    return neighbors, swapped_pair
            
def tabu_search(edges, n_vertix, conv_limit):
    # Stopping condition: after 'conv_limit' iterations, if the quality of the 
    # best solution does not improve, we terminate.
    group_a = [i for i in range(1, floor(n_vertix/2) + 1)]
    group_b = [i for i in range(group_a[-1] + 1, n_vertix + 1)]
    
    tabu_list = [[] for i in range(len(group_a))]
    
    best_solution = [list(group_a), list(group_b)]
    best_score = score(best_solution)
    current_solution = list(best_solution)
    
    conv = 0
    while conv < conv_limit:
        conv += 1
        # Calculate the fitness of neighbors, and check if that neighbor is tabu
        for j in range(10):
            neighbors, swapped_pair = create_neighbors(current_solution)
            scores = [[] for i in range(len(neighbors))]
            for i in range(len(group_a)*len(group_b)):
                # Aspiring condition
                if [swapped_pair[i][1], swapped_pair[i][0]] in tabu_list:
                    if score(neighbors[i]) < best_score:
                        tabu_list.remove(swapped_pair[i])
                        tabu_list.append([])
                        scores[i] = score(neighbors[i])
                    else:
                        scores[i] = float('inf')
                else:
                    scores[i] = score(neighbors[i])
            best_pos = scores.index(min(scores))
            
            # Update best solution and reset 'conv' if new one is found
            if scores[best_pos] < best_score:
                best_score = scores[best_pos]
                best_solution = neighbors[best_pos]
                conv = 0
                                
            # Update tabu list and set current solution
            tabu_list.insert(0, swapped_pair[best_pos])
            del tabu_list[-1]
            current_solution = neighbors[best_pos]
    print(" ".join([str(i) for i in best_solution[0]]))

tabu_search(edges, n_vertix, 5000)

