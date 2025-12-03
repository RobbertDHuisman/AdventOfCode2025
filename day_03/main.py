from pathlib import Path
from dataloader.dataloader import Dataloader
from day_03.battery import Bank 

data = Dataloader(Path("day_03/input.csv")).data
numbers_of_batteries_to_find = [2, 12]
power_banks = []

for number in numbers_of_batteries_to_find:
    for banks in data:
        bank = Bank(banks, number)
        power_banks.append(bank)
        # print(f"Joltage for bank {banks} is {bank.joltage}")

    print(f"Total joltage using {number} of betteries is {sum([bank.joltage for bank in power_banks])}")
