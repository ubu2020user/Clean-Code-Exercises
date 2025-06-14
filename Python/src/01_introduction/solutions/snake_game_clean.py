import os
import sys
import time
import random
import keyboard

# Constants
WIDTH = 20
HEIGHT = 10
SNAKE_CHAR = 'O'
FOOD_CHAR = '*'
EMPTY_CHAR = ' '

# Initialize game state
snake = [(WIDTH // 2, HEIGHT // 2)]
direction = 'RIGHT'
food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
score = 0

def draw_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Score: {score}")
    
    # Top border
    print('#' * (WIDTH + 2))
    
    for y in range(HEIGHT):
        print('#', end='')  # Left border
        for x in range(WIDTH):
            if (x, y) in snake:
                print(SNAKE_CHAR, end='')
            elif (x, y) == food:
                print(FOOD_CHAR, end='')
            else:
                print(EMPTY_CHAR, end='')
        print('#')  # Right border
    
    # Bottom border
    print('#' * (WIDTH + 2))


def move_snake():
    global food, score
    head_x, head_y = snake[0]
    if direction == 'UP':
        head_y -= 1
    elif direction == 'DOWN':
        head_y += 1
    elif direction == 'LEFT':
        head_x -= 1
    elif direction == 'RIGHT':
        head_x += 1 

    new_head = (head_x, head_y)
 
    # Check collisions
    if new_head in snake or head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        print("Game Over!")
        sys.exit()

    snake.insert(0, new_head)

    # Check if food is eaten
    if new_head == food:
        score += 1
        food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
    else:
        snake.pop()

def update_direction():
    global direction
    if keyboard.is_pressed('w') and direction != 'DOWN':
        direction = 'UP'
    elif keyboard.is_pressed('s') and direction != 'UP':
        direction = 'DOWN'
    elif keyboard.is_pressed('a') and direction != 'RIGHT':
        direction = 'LEFT'
    elif keyboard.is_pressed('d') and direction != 'LEFT':
        direction = 'RIGHT'

def main():
    while True:
        draw_board()
        update_direction()
        move_snake()
        time.sleep(0.2)

if __name__ == "__main__":
    main()