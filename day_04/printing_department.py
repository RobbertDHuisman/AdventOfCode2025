import re

class PrintingDepartment():
    def __init__(self, grid):
        self.grid = grid
        self.paper_rolls = []
        self.accessable_rolls = []
        self.first_accessable = 0
        self.rolls_removed = 0
        self.get_coordinates_rolls_of_paper()
        self.remove_all_rolls()

    def get_coordinates_rolls_of_paper(self):
        # Go through all rows and find all paper rolls
        for i in range(0, len(self.grid)):
            for match in re.finditer('@', self.grid[i]):
                self.paper_rolls.append((i, match.start()))
    
    def find_accessable_rolls(self):
        # Go through all paper rolls
        for i in range(len(self.paper_rolls)):
            # Set which rolls should be checked
            nr_adjacent = 0
            min_check = max(0, i - (len(self.grid[0]) + 2))
            max_check = min(len(self.paper_rolls), i + (len(self.grid[0]) + 2))

            # Go through roles adjacent in the list
            for other_roll in self.paper_rolls[min_check:max_check]:
                # Check if the other roll is adjacent
                if self.paper_rolls[i] != other_roll:
                    if (abs(self.paper_rolls[i][0] - other_roll[0]) <= 1) and (abs(self.paper_rolls[i][1] - other_roll[1]) <= 1):
                        nr_adjacent += 1
            
            # If less than 4 adjacent rolls, add to accessable rolls
            if nr_adjacent < 4:
                self.accessable_rolls.append(self.paper_rolls[i])

    def remove_rolls(self):
        print(f"Removing {len(self.accessable_rolls)} rolls")
        # On first removal, set first accessable
        if self.rolls_removed == 0:
            self.first_accessable += len(self.accessable_rolls)
        
        # Update amount of rolls removed
        self.rolls_removed += len(self.accessable_rolls)

        # Remove accessable rolls from paper rolls
        for roll in self.accessable_rolls:
            self.paper_rolls.remove(roll)

        # Reset accessable rolls
        self.accessable_rolls = []            
    
    def remove_all_rolls(self):
        # Find first set of accessable rolls
        self.find_accessable_rolls()

        # Continue until no rolls are accessable
        while len(self.accessable_rolls) > 0:
            self.remove_rolls()
            self.find_accessable_rolls()
