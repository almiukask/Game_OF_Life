from pprint import pprint
import random
import matplotlib.pyplot as plt
import argparse


def get_initial_data(grid_size: int) -> list[list[int]]:
    """
    Generates matrix of 1 and 0. Takes the size of matrix
    """
    random.seed(10)
    grid_list = []
    for _ in range(grid_size):
        row = []
        for _ in range(grid_size):
            row.append(int(random.random() * 3 / 2))  # defining odds of 1 appearing
        grid_list.append(row)
    return grid_list


def population_count(grid_snip: list[list[int]]) -> int:
    """
    Counts and retruns sum of 1s in the given matrix
    """
    sum_ = 0
    for x in grid_snip:
        sum_ += sum(x)
    return sum_


def get_neighbours_count(grid_snip: list[list[int]], curr_x: int, curr_y: int) -> int:
    """
    Takes a matrix, location of current element and gives out alive neighbour count
    """
    neighbour_count = 0
    if type(curr_x) is not int or type(curr_y) is not int:
        raise Exception("index Contains NaN")

    if curr_x < 0 or curr_y < 0:
        raise ValueError("index cannot be a negative number")

    lower_x = curr_x - 1 if curr_x >= 1 else curr_x
    lower_y = curr_y - 1 if curr_y >= 1 else curr_y
    upper_x = curr_x + 2 if curr_x <= len(grid_snip) else curr_x
    upper_y = curr_y + 2 if curr_y <= len(grid_snip) else curr_y

    self_x = 1 if curr_x > 0 else 0
    self_y = 1 if curr_y > 0 else 0

    # range(curr_x-1; curr_x+2)

    for idx_x, row in enumerate(grid_snip[lower_x:upper_x]):
        for idx_y, cell in enumerate(row[lower_y:upper_y]):
            if not (idx_x == self_x and idx_y == self_y):
                if type(cell) is not int:
                    raise TypeError("Data Contains NaN")
                else:
                    neighbour_count += 1 if cell != 0 else (cell if cell == 1 else 0)
    return neighbour_count


def get_next_gen_state(grid_snip: list[list[int]], curr_x: int, curr_y: int) -> int:
    """
    Given the the state of a current element and its neighbour states returns upcoming state for a matrix element
    """
    neighbour_count = get_neighbours_count(grid_snip, curr_x, curr_y)

    if grid_snip[curr_x][curr_y] == 1:
        if neighbour_count < 2:
            return 0
        elif neighbour_count in (2, 3):
            return 1
        elif neighbour_count > 3:
            return 0
        else:
            raise Exception("")
            return 1

    # not alive
    if neighbour_count == 3:
        return 1
    else:
        return 0


def fill_new_gen_grid(grid_snip: list[list[int]]) -> list[list[int]]:
    """
    Constructs matrix for upcoming generation given the previous one
    """
    new_grid = []

    for i, _ in enumerate(grid_snip):
        single_list = []
        for j, _ in enumerate(grid_snip):
            new_state = get_next_gen_state(grid_snip, i, j)
            single_list.append(new_state)
        new_grid.append(single_list)
    return new_grid


def get_arguments() -> list[int, int]:
    parser = argparse.ArgumentParser(
        prog="GameOfLife", description="Runs game for finite genrations"
    )
    parser.add_argument("-d", "--dim", help="matrix dimesnion")
    parser.add_argument("-g", "--gens", help="generations to play")
    args = parser.parse_args()
    try:
        grid_size = abs(int(args.dim))  # if int(args.dim) >= 0 else 50
    except:
        grid_size = 50
        pprint("Values for --dim not provided properly - using defaults")
    try:
        gen_count = abs(int(args.gens))  # if int(args.gens) >= 0 else 500
    except:
        gen_count = 500
        pprint("Values for --gens not provided properly - using defaults")
    return [grid_size, gen_count]


if __name__ == "__main__":

    grid_size, gen_count = get_arguments()

    local_grid = get_initial_data(grid_size)
    pprint(local_grid)

    fig, ax = plt.subplots()

    for i in range(gen_count):
        next_grid = fill_new_gen_grid(local_grid)
        ax.clear()
        ax.imshow(next_grid)
        ax.set_title(f"frame {i}")
        plt.pause(0.5)
        local_grid = next_grid.copy()
