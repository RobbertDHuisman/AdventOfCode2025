from pathlib import Path
from dataloader.dataloader import Dataloader
from day_01.safe import Safe

data = Dataloader(Path("day_01/input.csv")).data
safe = Safe()

for step in data:
    safe.rotate(step)

print(f"part 1: {safe.at_zero_counter}")
print(f"part 2: at zero counter is {safe.at_zero_counter}, past zero is {safe.past_zero_counter}, total is {safe.at_zero_counter + safe.past_zero_counter}")

