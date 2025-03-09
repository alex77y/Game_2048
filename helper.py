import numpy as np
def merge_list(arr,grid_length):
    pointer = 1
    while pointer < len(arr):
        if arr[pointer - 1] == arr[pointer]:
            arr.pop(pointer - 1)
            arr[pointer-1] = 2 * arr[pointer-1]
            if pointer < len(arr) and arr[pointer] == arr[pointer-1]:
                pointer +=1
        else:
            pointer +=1
    return [0]*(grid_length - len(arr)) + arr


def color_gen(value):

    base_color = (238, 228, 218)
    log_value = int(np.log2(value).item()) if value > 0 else 0

    red = int(min(255, base_color[0] + log_value * 5))
    green = int(max(0, base_color[1] - log_value * 20))
    blue = int(max(0, base_color[2] - log_value * 20))
    return (red, green, blue)


def move(grid,direction):
    if direction == 'up':
        for col in range(len(grid)):
            vals = []
            for row in range(len(grid))[::-1]:
                if grid[row][col] != 0:
                    vals.append(grid[row][col])
            if vals:
                new_val = merge_list(vals,len(grid))[::-1]
                for row in range(len(grid)):
                    grid[row][col] = new_val[row]
            else:
                continue 
    elif direction == 'down':
        for col in range(len(grid)):
            vals = []
            for row in range(len(grid)):
                if grid[row][col] != 0:
                    vals.append(grid[row][col])
            if vals:
                new_val = merge_list(vals,len(grid))
                for row in range(len(grid)):
                    grid[row][col] = new_val[row]
            else:
                continue 
    elif direction == 'left':
        for row in range(len(grid)):
            vals = []
            for col in range(len(grid))[::-1]:
                if grid[row][col] != 0:
                    vals.append(grid[row][col])
            if vals:
                print(vals)
                new_val = merge_list(vals,len(grid))[::-1]
                print(new_val)
                for col in range(len(grid)):
                    grid[row][col] = new_val[col]
            else:
                continue 
    else:
        for row in range(len(grid)):
            vals = []
            for col in range(len(grid)):
                if grid[row][col] != 0:
                    vals.append(grid[row][col])
            if vals:
                new_val = merge_list(vals,len(grid))
                for col in range(len(grid)):
                    grid[row][col] = new_val[col]
            else:
                continue 

    return grid