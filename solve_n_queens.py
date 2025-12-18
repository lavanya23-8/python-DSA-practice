def solve_n_queens(n):
    col = set()
    d1 = set()
    d2 = set()

    def backtrack(r):
        if r == n:
            print("Solution found")
            return
        for c in range(n):
            if c in col or (r-c) in d1 or (r+c) in d2:
                continue
            col.add(c); d1.add(r-c); d2.add(r+c)
            backtrack(r+1)
            col.remove(c); d1.remove(r-c); d2.remove(r+c)

    backtrack(0)

solve_n_queens(4)
