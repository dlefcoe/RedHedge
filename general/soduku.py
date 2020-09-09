
'''
by Darren Lefcoe
twitter: @dlefcoe
email: darren@redhedge.uk


desigend for interactive python in vs code.
'''
# %% soduku puzzle
## soduku puzzle solver

#%% imports

import numpy as np



print('imports done')


# %% code

def main():
    """
    the main code
    """
    global grid

    grid = [[1,0,0,2,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]
    
    print(np.matrix(grid))


def possible(y,x,n):
    """
    check if it is possible to put number in a square (y,x)
    
    return:
        True if possible
        False if impossible
    """
    global grid

    # if number exists return false
    for i in range(0,9):
        if grid[y][i] == n:
            return False
        if grid[i][x] == n:
            return False

    # check small square    
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True


def solve():
    """
    recursive function to find solution
    """
    global grid

    for y in range(9):
        for x in range(9):
            if grid[y][x] ==0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        # recursion
                        solve()
                        # backtracking
                        grid[y][x] = 0
                return
    # print solutions sequentially
    print(np.matrix(grid))



# run main
main()

# %% run possible

# for loop showing how the possible function works
for i in range(9):
    print(possible(i,0,2))

# %% solutions
solve()

