import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import io
from disease import covid19 as disease
from scenario import epidemic_in_infected_pop as scenario

# Initialize the grid
N = 100
grid = np.random.choice([0, 1, 2], N * N, p=[scenario.S0, scenario.I0, scenario.R0]).reshape(N, N)


def count_infected_neighbors(i, j):
    infected_neighbors = 0
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if grid[ni, nj] == 1:
                    infected_neighbors += 1
    return infected_neighbors


beta = disease.beta  # infection probability
gamma = disease.gamma  # recovery probability
time = 100

frames = []  # for storing frames
infected_counts = []

for _ in range(time):  # time steps
    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            if grid[i, j] == 0:  # Susceptible
                infected_neighbors = count_infected_neighbors(i, j)
                if np.random.rand() < 1 - (1 - beta) ** infected_neighbors:
                    new_grid[i, j] = 1  # becomes Infected
            elif grid[i, j] == 1:  # Infected
                if np.random.rand() < gamma:
                    new_grid[i, j] = 2  # becomes Recovered
    grid = new_grid
    infected_count = np.count_nonzero(grid == 1)
    infected_counts.append(infected_count)

    # Visualization
    buf = io.BytesIO()
    plt.figure(figsize=(5, 5))
    plt.imshow(grid, vmin=0, vmax=2, cmap='viridis')
    plt.axis('off')
    plt.savefig(buf, format='png')
    buf.seek(0)
    frames.append(Image.open(buf))
    plt.close()

#plot
time_axis = np.arange(time)

# Plot the infected counts
plt.figure()
plt.plot(time_axis, infected_counts)
plt.xlabel('Time')
plt.ylabel('Number of Infected Individuals')
plt.title('Change in the Number of Infected Individuals over Time')
plt.grid(True)
plt.savefig('infected_counts.png')
plt.close()

# Save as a GIF
frames[0].save('simulation.gif', format='GIF', append_images=frames[1:], save_all=True, duration=200, loop=0)
