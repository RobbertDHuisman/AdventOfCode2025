from pathlib import Path
from dataloader.dataloader import Dataloader
from day_07.tackyon_manifold import TackyonManifold 

data = Dataloader(Path("day_07/input.csv")).data
tackyon_manifold = TackyonManifold(data)

print(f"Part 1: splits = {tackyon_manifold.splits}")
print(f"Part 2: timelines = {tackyon_manifold.timelines[1]}")
