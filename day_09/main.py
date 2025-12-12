from pathlib import Path
from dataloader.dataloader import Dataloader
from day_09.movie_theater import MovieTheater
import numpy as np

data = Dataloader(Path("day_09/extra_example.csv")).data

red_tiles = []
for line in data:
    coordinates = []
    point = line.split(',')
    for coordinate in point:
        coordinates.append(int(coordinate))
    red_tiles.append(coordinates)

red_tiles = np.array(red_tiles)
movie_theater = MovieTheater(red_tiles)

print(f"Part 1: area = {movie_theater.area_matrix.max()}")
print(f"Part 2: new area = {movie_theater.new_area_matrix.max()}")
