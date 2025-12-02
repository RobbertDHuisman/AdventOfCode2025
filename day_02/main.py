from pathlib import Path
from dataloader.dataloader import Dataloader
from day_02.id_checker import IdChecker

data = Dataloader(Path("day_02/input.csv")).data
split = data[0].split(",")
id_checker = IdChecker(split)

print(f"part 1: sum is {sum(id_checker.invalid_ids)}")
print(f"part 2: sum is {sum(id_checker.invalid_ids_2)}")

