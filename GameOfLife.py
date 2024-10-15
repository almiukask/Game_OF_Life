from pprint import pprint
import random

def data_generation(grid_size):
    random.seed(10)
    grid_list = []
    for i in range(grid_size):
        single_list = []
        for j in range(grid_size):
            single_list.append(int(random.random()*6/5)) #defining odds of 1 appearing 
        grid_list.append(single_list)
    return grid_list

def population_count(grid_snip):
    sum_ = 0
    for x in grid_snip:
        sum_ += sum(x)
    return sum_

def get_next_gen_state(grid_snip, curr_x, curr_y):
    flat_list = []
    neighbour_count = 0

    lower_x = curr_x - 1 if curr_x >= 1 else curr_x
    lower_y = curr_y - 1 if curr_y >= 1 else curr_y
    upper_x = curr_x + 2 if curr_x <= len(grid_snip) else curr_x
    upper_y = curr_y + 2 if curr_y <= len(grid_snip) else curr_y

    self_x = 1 if curr_x > 0 else 0
    self_y = 1 if curr_y > 0 else 0

    #pprint(f"Current state {grid_snip[curr_x][curr_y]} of selected cell")
    #pprint(f"l_x {lower_x}, l_y {lower_y}, u_x {upper_x}, u_y {upper_y}")
    for i, x in enumerate(grid_snip[lower_x:upper_x]):
        #pprint(f"fist slice {x} index i {i}")
        for j, y in enumerate(x[lower_y:upper_y]):
            #pprint(f"second slice {y} index y {j}")
            if not(i==self_x and j== self_y):
                flat_list.append(y)
            else:
                pprint(f"self state {y}")

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

pprint(f"Upcoming generation cell state {get_next_gen_state(local_grid, 1, 5)}")

 