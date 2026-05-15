# def tower_of_hanoi(n, source, destination, auxiliary):
#     if n == 1:
#         print(f"Move disk 1 from {source} to {destination}")
#         return
    
#     # Move n-1 disks from source to auxiliary
#     tower_of_hanoi(n - 1, source, auxiliary, destination)
    
#     # Move the nth disk from source to destination
#     print(f"Move disk {n} from {source} to {destination}")
    
#     # Move n-1 disks from auxiliary to destination
#     tower_of_hanoi(n - 1, auxiliary, destination, source)

# # Example: 3 disks, rods A, B, C
# n = 2
# tower_of_hanoi(n, 'A', 'C', 'B')


def hanoi_solver(number_of_disk)-> str:
    rods = [list(range(number_of_disk, 0, -1)), [], []]
    
    # min_move_required = 2 ** number_of_disk - 1

    moves = f"{str(rods[0])} {str(rods[1])} {str(rods[2])}"

    return tower_of_hanoi(number_of_disk, 0, 1, 2,moves,rods)

def tower_of_hanoi(n, source, destination, auxiliary, moves, rods):

    if n == 1:
        rods[destination].append(n)
        if len(rods[source]) > 0 :
            rods[source].pop()
        move = f"{str(rods[0])} {str(rods[2])} {str(rods[1])}"
        
        if len(moves) > 0:
            moves = moves + '\n' + move
        else:
            moves = moves + move
        return moves 
    
    # Move n-1 disks from source to auxiliary
    moves = tower_of_hanoi(n - 1, source, auxiliary, destination,moves, rods)
    
    # Move the nth disk from source to destination
    #print(f"Move disk {n} from {source} to {destination}")
    rods[destination].append(n)
    if len(rods[source]) > 0 :
            rods[source].pop()
    move = f"{str(rods[0])} {str(rods[2])} {str(rods[1])}"
    if len(moves) > 0:
        moves = moves + '\n' + move
    else:
        moves = moves + move



    # Move n-1 disks from auxiliary to destination
    moves = tower_of_hanoi(n - 1, auxiliary, destination, source, moves,rods)

    return moves 

print(hanoi_solver(3))
