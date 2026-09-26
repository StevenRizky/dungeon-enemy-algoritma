from collections import deque

dungeon = [
    "########",
    "#E     #",
    "# ###  #",
    "#   #P #",
    "########"
]

DETECTION_RANGE = 6

def find_position(symbol):
    """Mencari posisi Enemy atau Player."""
    for y, row in enumerate(dungeon):
        for x, cell in enumerate(row):
            if cell == symbol:
                return (x, y)
    return None

def find_path(start, target):
    """Mencari jalur terpendek menggunakan BFS."""
    queue = deque([(start, [start])])
    visited = {start}
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    height = len(dungeon)
    width = len(dungeon[0])

    while queue:
        position, path = queue.popleft()
        if position == target:
            return path

        for dx, dy in directions:
            x = position[0] + dx
            y = position[1] + dy
            if 0 <= x < width and 0 <= y < height:
                next_pos = (x, y)
                if dungeon[y][x] != "#" and next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, path + [next_pos]))

    return None

enemy = find_position('E')
player = find_position('P')

print('Posisi Enemy :', enemy)
print('Posisi Player:', player)

distance = abs(enemy[0] - player[0]) + abs(enemy[1] - player[1])
print('Jarak Enemy ke Player:', distance)

if distance <= DETECTION_RANGE:
    print('\nPlayer terdeteksi!')
    path = find_path(enemy, player)
    if path:
        print('Jalur ditemukan:')
        print(path)
        if len(path) > 1:
            enemy = path[1]
            print('Enemy bergerak ke:', enemy)
        else:
            print('Enemy sudah berada di posisi Player.')
    else:
        print('Tidak ada jalur menuju Player.')
        print('Enemy tetap diam.')
else:
    print('\nPlayer berada di luar jangkauan.')
    print('Enemy tetap diam.')