with open('input.txt', 'r') as file:
    lines = file.readlines()
    inp = []
    for line in lines:
        inp.append(list(line.strip()))

    def find_xmas(grid):
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        # Direction vectors for all 8 possible directions
        directions = [
            (0, 1),   # right
            (0, -1),  # left
            (1, 0),   # down
            (-1, 0),  # up
            (1, 1),   # down-right
            (1, -1),  # down-left
            (-1, 1),  # up-right
            (-1, -1)  # up-left
        ]

        def check_xmas(row, col, dx, dy):
            if not (0 <= row + 3*dx < rows and 0 <= col + 3*dy < cols):
                return False
            return (grid[row][col] == 'X' and
                    grid[row + dx][col + dy] == 'M' and
                    grid[row + 2*dx][col + 2*dy] == 'A' and
                    grid[row + 3*dx][col + 3*dy] == 'S')

        # Convert input string to 2D list
        if isinstance(grid, str):
            grid = [list(row) for row in grid.strip().split('\n')]

        # Check each starting position and direction
        for i in range(rows):
            for j in range(cols):
                for dx, dy in directions:
                    if check_xmas(i, j, dx, dy):
                        count += 1

        return count
    ans = find_xmas(inp)
    print(ans)
