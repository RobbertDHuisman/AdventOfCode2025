from pathlib import Path
from dataloader.dataloader import Dataloader
from day_06.homework import Homework

data = Dataloader(Path("day_06/input.csv"), isstrip=False).data
homework = Homework(data)

print(f"Part 1: {sum(homework.answers)}")
print(f"Part 2: {sum(homework.correct_answers)}")