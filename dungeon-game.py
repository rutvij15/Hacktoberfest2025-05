import random

WIDTH, HEIGHT = 8, 8
PLAYER = "P"
TREASURE = "T"
TRAP = "X"
EMPTY = "."

def generate_dungeon():
    dungeon = [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]
    dungeon[random.randint(0, HEIGHT-1)][random.randint(0, WIDTH-1)] = TREASURE
    for _ in range(5):
        dungeon[random.randint(0, HEIGHT-1)][random.randint(0, WIDTH-1)] = TRAP
    return dungeon

def print_dungeon(dungeon, player_pos):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == player_pos:
                print(PLAYER, end=" ")
            else:
                print(dungeon[y][x], end=" ")
        print()
    print()

def move_player(pos, move):
    x, y = pos
    if move == "w" and y > 0: y -= 1
    elif move == "s" and y < HEIGHT-1: y += 1
    elif move == "a" and x > 0: x -= 1
    elif move == "d" and x < WIDTH-1: x += 1
    return x, y

def main():
    dungeon = generate_dungeon()
    player_pos = (0, 0)
    while True:
        print_dungeon(dungeon, player_pos)
        move = input("Move (WASD) or Q to quit: ").lower()
        if move == "q": break
        player_pos = move_player(player_pos, move)
        x, y = player_pos
        if dungeon[y][x] == TREASURE:
            print("🎉 You found the treasure! You win!")
            break
        elif dungeon[y][x] == TRAP:
            print("💀 You fell in a trap! Game over!")
            break

if __name__ == "__main__":
    main()
