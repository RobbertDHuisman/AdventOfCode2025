from pathlib import Path
from dataloader.dataloader import Dataloader
from day_04.printing_department import PrintingDepartment 

data = Dataloader(Path("day_04/input.csv")).data
printing_department = PrintingDepartment(data)

print("Part 1:", printing_department.first_accessable)
print("Part 2:", printing_department.rolls_removed)