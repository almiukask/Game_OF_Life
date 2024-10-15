from pprint import pprint
import random

def data_generation(grid_size):
    random.seed(10)
    grid_list = []
    for num in range(grid_size): 
        grid_list.append(list(range(grid_size)))
    #suprastinti iki 1 ciklo
    for i, single_list in enumerate(grid_list):
        for j, num in enumerate(single_list):
            num = int(random.random()*6/5) #defining odds of 1 appearing 
            grid_list[i][j]=num
    return grid_list

def population_count(grid_snip):
    # flat_list = []
    # for x in grid_snip:
    #     for y in x:
    #         flat_list.append(y)  
    # return sum(y > 0 for y in flat_list)
    sum_ = 0
    for x in grid_snip:
        sum_ += sum(x)
    return sum_

def get_next_gen_state(grid_snip, curr_x, curr_y):
    flat_list = []
    neighbour_count = 0
    pprint(f"Current state {grid_snip[curr_x][curr_y]} of selected cell")

    for i, x in enumerate(grid_snip[curr_x-1:curr_x+2]):
        for j, y in enumerate(x[curr_y-1:curr_y+2]):
            if not(i==curr_x and j==curr_y):
                flat_list.append(y)

    pprint(flat_list)
    neighbour_count = sum(y > 0 for y in flat_list)
    pprint(f"Alive neighbours count {neighbour_count}")

    if grid_snip[curr_x][curr_y] == 1:
        if neighbour_count < 2:
            return 0
        elif neighbour_count >= 2 and neighbour_count <= 3:
            return 1
        elif neighbour_count > 3:
            return 0
        else: 
            return grid_snip[curr_x][curr_y]
    else:
        if neighbour_count == 3:
          return 1  
        else:
            return grid_snip[curr_x][curr_y]

local_grid=[]
local_grid=data_generation(10)
local_population=0
local_population=population_count(local_grid)

pprint(f"Grid and population of {local_population}")
for x in local_grid:
    pprint(f"{x}")

pprint(f"Upcoming generation cell state {get_next_gen_state(local_grid, 9, 9)}")

 