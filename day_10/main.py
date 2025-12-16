from pathlib import Path
from dataloader.dataloader import Dataloader
from day_10.machine import Machine 

data = Dataloader(Path("day_10/input.csv")).data

machines = []
buttons_pressed = []
joltage_buttons_pressed = []
for line in data:
    machines.append(Machine(line))
    buttons_pressed.append(machines[-1].buttons_pressed)
    joltage_buttons_pressed.append(machines[-1].joltage_buttons_pressed)

for machine in machines:
    if machine.joltage_buttons_pressed != machine.joltage_buttons_pressed_scipy:
        print(machine.joltage)
        print(machine.buttons)
        print(f"Joltage - PuLP presses: {machine.joltage_buttons_pressed}, SciPy presses: {machine.joltage_buttons_pressed_scipy}")
        print(f"Joltage - PuLP button presses: {machine.button_presses}, SciPy button presses: {machine.button_presses_scipy}")

print(f"Part 1: {sum(buttons_pressed)}")
print(f"Part 2: {sum(joltage_buttons_pressed)}")
