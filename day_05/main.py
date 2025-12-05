from pathlib import Path
from dataloader.dataloader import Dataloader
from day_05.inventory import Inventory

data = Dataloader(Path("day_05/input.csv")).data
inventory = Inventory(data)

print(f"Part 1: nr of fresh ingredients: {len(inventory.fresh_ingredients)}")
print(f"Part 2: nr of fresh id's: {inventory.nr_fresh_ids}")