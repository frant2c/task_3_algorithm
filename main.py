import random


def generate_map(m, n, land_percentage):
    total_cells_value = m * n
    land_amount = round(total_cells_value * land_percentage / 100)
    ocean_map = [[0] * n for _ in range(m)]
    for i in range(0, m):
        for j in range(0, n):
            # random value can be adjusted to shift land distribution
            if total_cells_value == land_amount or random.randint(0, 9) >= 6:
                ocean_map[i][j] = 1
                land_amount -= 1
            if land_amount <= 0:
                break
            total_cells_value -= 1
    for row in ocean_map:
        print(*row)
    return ocean_map


def find_paths(matrix, start, end):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    paths = []
    current_path = []

    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return
        if matrix[row][col] == 1 or visited[row][col]:
            return
        if (row, col) == end:
            current_path.append((row, col))
            paths.append(current_path[:])
            current_path.pop()
            return

        visited[row][col] = True
        current_path.append((row, col))

        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

        visited[row][col] = False
        current_path.pop()

    dfs(start[0], start[1])
    if not paths:
        raise Exception("No paths found from start to end.")
    return paths


def get_min_path(paths):
    min_path = paths[0]
    for path in paths:
        if len(min_path) > len(path):
            min_path = path
    return min_path


def input_valid_cell(param):
    while True:
        try:
            target_cell = tuple(map(int, input(f"Set coordinates of {param}:").split()))
        except ValueError:
            print("Cell is not ocean.")
            continue
        if world_map[target_cell[0]][target_cell[1]] == 0:
            print("Cell is ocean.")
            return target_cell
        else:
            print("Chosen cell must be an ocean cell.")


if __name__ == '__main__':
    m, n = map(int, input("Set map size").split())
    world_map = generate_map(m, n, 30)

    A = input_valid_cell("Starting point")
    B = input_valid_cell("End point")

    paths = find_paths(world_map, A, B)

    min_path = get_min_path(paths)
    print(min_path)
