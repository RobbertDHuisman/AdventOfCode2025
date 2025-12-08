from pathlib import Path
from dataloader.dataloader import Dataloader
from day_08.junction_box import JunctionBox 
import numpy as np

data = Dataloader(Path("day_08/input.csv")).data

points_list = []
for line in data:
    coordinates = []
    point = line.split(',')
    for coordinate in point:
        coordinates.append(int(coordinate))
    points_list.append(coordinates)

points = np.array(points_list)
junction_box = JunctionBox(points, 10)

print(f"Part 1: product = {junction_box.lengths[0] * junction_box.lengths[1] * junction_box.lengths[2]}")
print(f"Part 2: final_length = {junction_box.final_length}")
