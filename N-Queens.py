
def dfs_n_queens(n):
    if n <1:
        return []

    solutions = []
    solutions2 = []
    board = [["."] * n for _ in range(n)]
    # Sets to track occupied paths
    cols = set()
    pos_diag = set() # (r + c) is constant for positive diagonals
    neg_diag = set() # (r - c) is constant for negative diagonals

    def backtrack(r):
        # Base case: All queens placed
        if r == n:
            copy = [" ".join(row) for row in board]
            solutions.append(copy)
            copy2 = [index for row in board for index,col in enumerate(row)  if col=="Q"]
            solutions2.append(copy2)
            
            return

        for c in range(n):
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            # Place queen
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = "Q"

            # Recurse to next row
            backtrack(r + 1)

            # Backtrack: Remove queen
            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return solutions2


print(dfs_n_queens(4))
