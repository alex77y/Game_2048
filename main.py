import pygame
import numpy as np
import random
from helper import merge_list, color_gen, move
# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 4
TILE_SIZE = WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
COLORS = {
    0: (204, 192, 179)
}
for i in range(1,12):
    COLORS[2^i] = color_gen(2^i)
    print(color_gen(2^i))

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

def grid_init():
    grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    return grid

def add_random_tile(grid):
    empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = 2 if random.random() < 0.9 else 4
    else:
        pygame.quit()

def draw_grid(grid):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            value = grid[i][j]
            color = COLORS.get(value, (0, 0, 0))
            pygame.draw.rect(screen, color, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            if value != 0:
                font = pygame.font.Font(None, 36)
                text = font.render(str(value), True, BLACK)
                text_rect = text.get_rect(center=(j * TILE_SIZE + TILE_SIZE // 2, i * TILE_SIZE + TILE_SIZE // 2))
                screen.blit(text, text_rect)



def main():
    grid = grid_init()
    add_random_tile(grid)
    add_random_tile(grid)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move(grid,'up')
                elif event.key == pygame.K_DOWN:
                    move(grid,'down')
                elif event.key == pygame.K_LEFT:
                    move(grid,'left')
                elif event.key == pygame.K_RIGHT:
                    move(grid,'right')
                add_random_tile(grid)

        screen.fill(WHITE)
        draw_grid(grid)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()