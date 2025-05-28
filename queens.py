import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from collections import deque

# Board size (e.g. 7 for 7×7)
N = 7

# Directions for region-growing
DIRS = [(-1,0),(1,0),(0,-1),(0,1)]

def generate_colored_regions(n):
    grid = np.full((n, n), -1)
    region_id = 0
    unfilled = {(r, c) for r in range(n) for c in range(n)}

    while unfilled:
        r, c = random.choice(list(unfilled))
        queue = deque([(r, c)])
        region_cells = set()
        target_size = n  # aim for ~n cells per region

        while queue and len(region_cells) < target_size:
            cr, cc = queue.popleft()
            if (cr, cc) in unfilled:
                region_cells.add((cr, cc))
                unfilled.remove((cr, cc))
                random.shuffle(DIRS)
                for dr, dc in DIRS:
                    nr, nc = cr + dr, cc + dc
                    if (0 <= nr < n and 0 <= nc < n and
                        (nr, nc) in unfilled and len(region_cells) < target_size):
                        queue.append((nr, nc))

        for rr, cc in region_cells:
            grid[rr][cc] = region_id
        region_id += 1

    return grid

def is_safe(board, row, col, queens, regions, region_used):
    # no same column or diagonal
    for qr, qc in queens:
        if qc == col or abs(qr-row) == abs(qc-col):
            return False
    # each region only once
    if regions[row][col] in region_used:
        return False
    return True

def solve(board, row, queens, regions, region_used):
    if row == len(board):
        return True
    for col in range(len(board)):
        if is_safe(board, row, col, queens, regions, region_used):
            queens.append((row, col))
            region_used.add(regions[row][col])
            if solve(board, row+1, queens, regions, region_used):
                return True
            queens.pop()
            region_used.remove(regions[row][col])
    return False

# 1) Generate colored regions and find a valid queen placement
while True:
    regions = generate_colored_regions(N)
    solution_queens = []
    if solve(np.zeros((N, N)), 0, solution_queens, regions, set()):
        break

# 2) Game state: what the player has placed
player_queens = set()
dots = set()

# 3) Set up plotting
fig, ax = plt.subplots()
cmap = plt.cm.get_cmap("tab20", N)

def draw_board():
    ax.clear()
    # draw regions
    for r in range(N):
        for c in range(N):
            color = cmap(regions[r][c])
            rect = patches.Rectangle((c, N-1-r), 1, 1, edgecolor='black',
                                     facecolor=color)
            ax.add_patch(rect)
    # draw queens
    for (r, c) in player_queens:
        ax.text(c+0.5, N-1-r+0.5, '♛', ha='center', va='center', fontsize=24)
    # draw dots
    for (r, c) in dots:
        ax.text(c+0.5, N-1-r+0.5, '•', ha='center', va='center', fontsize=18, color='red')
    ax.set_xlim(0, N)
    ax.set_ylim(0, N)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')
    plt.draw()

# 4) Interaction handlers
right_button_held = False
drag_action = None   # 'add' or 'remove'
processed_positions = set()

def on_press(event):
    global right_button_held, drag_action, processed_positions
    if event.inaxes != ax:
        return
    col = int(event.xdata)
    row = N-1 - int(event.ydata)
    pos = (row, col)
    processed_positions = set()

    if event.button == 1:  # left click
        if pos in player_queens:
            player_queens.remove(pos)
        else:
            player_queens.add(pos)
            dots.discard(pos)

    elif event.button == 3:  # right click down
        right_button_held = True
        if pos in dots:
            drag_action = 'remove'
            dots.remove(pos)
        else:
            drag_action = 'add'
            dots.add(pos)
        player_queens.discard(pos)
        processed_positions.add(pos)

    draw_board()

def on_release(event):
    global right_button_held, drag_action
    if event.button == 3:
        right_button_held = False
        drag_action = None

def on_motion(event):
    global processed_positions
    if not right_button_held or event.inaxes != ax or drag_action is None:
        return
    col = int(event.xdata)
    row = N-1 - int(event.ydata)
    pos = (row, col)
    if pos in processed_positions:
        return
    processed_positions.add(pos)

    if drag_action == 'add':
        dots.add(pos)
        player_queens.discard(pos)
    else:  # remove
        dots.discard(pos)

    draw_board()

# 5) Launch
draw_board()
fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('button_release_event', on_release)
fig.canvas.mpl_connect('motion_notify_event', on_motion)
plt.show()
