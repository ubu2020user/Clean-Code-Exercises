import os as o  # Using single-letter aliases for modules reduces readability. Use descriptive names.
import sys as s  # Same issue as above; 'sys' should not be aliased to 's'.
import time as t  # Aliasing 'time' to 't' is unnecessary and makes the code harder to understand.
import random as r  # Aliasing 'random' to 'r' reduces clarity.
import keyboard as k  # Aliasing 'keyboard' to 'k' is not descriptive.

# Constants
W = 20  # Variable names like 'W' and 'H' are not descriptive. Use 'WIDTH' and 'HEIGHT' for clarity.
H = 10
S = 'O'  # 'S' is not descriptive. Use 'SNAKE_CHAR' or similar.
F = '*'  # 'F' is not descriptive. Use 'FOOD_CHAR' or similar.
E = ' '  # 'E' is not descriptive. Use 'EMPTY_CHAR' or similar.

# Initialize game state
snk = [(W // 2, H // 2)]  # 'snk' is not descriptive. Use 'snake' or 'snake_body'.
d = 'R'  # 'd' is not descriptive. Use 'direction'.
fd = (r.randint(0, W - 1), r.randint(0, H - 1))  # 'fd' is not descriptive. Use 'food_position'.
scr = 0  # 'scr' is not descriptive. Use 'score'.

def drw():  # Function name 'drw' is not descriptive. Use 'draw_board' or similar.
    o.system('cls' if o.name == 'nt' else 'clear')  # Using 'o' instead of 'os' reduces readability.
    print("Score: " + str(scr))
    print('#' * (W + 2))  # Magic numbers like '+2' should be explained or avoided.
    for y in range(H):
        print('#', end='')
        for x in range(W):
            if (x, y) in snk:
                print(S, end='')
            elif (x, y) == fd:
                print(F, end='')
            else:
                print(E, end='')
        print('#')
    print('#' * (W + 2))

def mv():  # Function name 'mv' is not descriptive. Use 'move_snake' or similar.
    global fd, scr  # Using global variables is not ideal. Pass them as arguments instead.
    hx, hy = snk[0]  # 'hx' and 'hy' are not descriptive. Use 'head_x' and 'head_y'.
    if d == 'U':  # Direction logic could be refactored into a dictionary or similar structure.
        hy -= 1
    elif d == 'D':
        hy += 1
    elif d == 'L':
        hx -= 1
    elif d == 'R':
        hx += 1
    nh = (hx, hy)  # 'nh' is not descriptive. Use 'new_head'.
    if nh in snk or hx < 0 or hx >= W or hy < 0 or hy >= H:  # Collision logic could be refactored.
        print("Game Over!")
        s.exit()  # Using 'sys.exit()' abruptly terminates the program. Consider a cleaner exit strategy.
    snk.insert(0, nh)
    if nh == fd:
        scr += 1
        fd = (r.randint(0, W - 1), r.randint(0, H - 1))  # Food placement logic does not check for collisions with the snake.
    else:
        snk.pop()

def upd():  # Function name 'upd' is not descriptive. Use 'update_direction' or similar.
    global d  # Using global variables is not ideal. Pass them as arguments instead.
    if k.is_pressed('w') and d != 'D':  # Hardcoded keys reduce flexibility. Use configurable key mappings.
        d = 'U'
    elif k.is_pressed('s') and d != 'U':
        d = 'D'
    elif k.is_pressed('a') and d != 'R':
        d = 'L'
    elif k.is_pressed('d') and d != 'L':
        d = 'R'

def m():  # Function name 'm' is not descriptive. Use 'main_loop' or similar.
    while True:
        drw()
        upd()
        mv()
        t.sleep(0.2)  # Hardcoded sleep duration reduces flexibility. Use a configurable constant.

if __name__ == "__main__":
    m()  # The main function name 'm' is not descriptive. Use 'main' or similar.
