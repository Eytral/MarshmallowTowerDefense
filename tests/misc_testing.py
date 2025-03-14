def find_path(map):
    # Find the start position (3)
    start = None
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] == 3:
                start = (r, c)
                break
        if start:
            break

    # Directions for movement: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Initialize the path list starting from the start position
    path = [start]
    visited = set([start])
    current_position = start

    while True:
        found_next_step = False
        # Check all possible directions (up, down, left, right)
        for dr, dc in directions:
            nr, nc = current_position[0] + dr, current_position[1] + dc

            if 0 <= nr < len(map) and 0 <= nc < len(map[0]) and map[nr][nc] == 1 and (nr, nc) not in visited:
                # Valid path, add to the path
                visited.add((nr, nc))
                path.append((nr, nc))
                current_position = (nr, nc)
                found_next_step = True
                break  # Move in the first valid direction found

        if not found_next_step:
            break  # No valid path found, end the search

    
    return path


# Example usage:
map = [
    [0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

path = find_path(map)
print("Path:", path)
