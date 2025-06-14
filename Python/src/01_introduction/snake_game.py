import os as o
import sys as s
import time as t
import random as r
import keyboard as k

# Constants
W = 20
H = 10
S = 'O'
F = '*'
E = ' '

# Initialize game state
snk = [(W // 2, H // 2)]
d = 'R'
fd = (r.randint(0, W - 1), r.randint(0, H - 1))
scr = 0

def drw():
    o.system('cls' if o.name == 'nt' else 'clear')
    print("Score: " + str(scr))
    print('#' * (W + 2))
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

def mv():
    global fd, scr
    hx, hy = snk[0]
    if d == 'U':
        hy -= 1
    elif d == 'D':
        hy += 1
    elif d == 'L':
        hx -= 1
    elif d == 'R':
        hx += 1
    nh = (hx, hy)
    if nh in snk or hx < 0 or hx >= W or hy < 0 or hy >= H:
        print("Game Over!")
        s.exit()
    snk.insert(0, nh)
    if nh == fd:
        scr += 1
        fd = (r.randint(0, W - 1), r.randint(0, H - 1))
    else:
        snk.pop()

def upd():
    global d
    if k.is_pressed('w') and d != 'D':
        d = 'U'
    elif k.is_pressed('s') and d != 'U':
        d = 'D'
    elif k.is_pressed('a') and d != 'R':
        d = 'L'
    elif k.is_pressed('d') and d != 'L':
        d = 'R'

def m():
    while True:
        drw()
        upd()
        mv()
        t.sleep(0.2)

if __name__ == "__main__":
    m()
