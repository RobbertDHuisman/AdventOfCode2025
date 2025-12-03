import re

class Bank():
    def __init__(self, batteries, nr_of_batteries):
        self.batteries = batteries
        self.nr_of_batteries = nr_of_batteries
        self.highest_number_to_search = 9
        self.lowest_index = 0
        self.batteries_found = []
        self.joltage = ""
        self.find_batteries()
        self.get_joltage()

    def find_batteries(self):      
        # Find all the strongest batteries. 
        for i in range(self.nr_of_batteries):
            self.find_strongest_battery()

            # Set highest number for further searches
            self.highest_number_to_search = self.batteries_found[-1][0]

            self.update_lowest_index()

    def find_strongest_battery(self):
        # Go through numbers 9 to 1
        found = False
        for i in range(9, 0, -1):
            matches = self.find_number(i)
            for match in matches:
                start, end = match.span()
                # If there is a match, save it if it's not already found and break
                if end:
                    if ([i, start] not in self.batteries_found) and (start >= self.lowest_index):
                        self.batteries_found.append([i, start])
                        found = True
                        break
            if found:
                break
  
    def find_number(self, number):
        # Find all indices of a number in the string starting from start_index
        indices = re.finditer(f'{number}', self.batteries)
        return indices
    
    def update_lowest_index(self):
        # Nr of batteries to still find
        batteries_left = self.nr_of_batteries - len(self.batteries_found)

        # Set lowest index for next search
        self.lowest_index = 0

        # Check all batteries found so far
        for battery in self.batteries_found:
            
            # Count how many batteries have a higher index
            higher_index = 0
            for other_batteries in self.batteries_found:
                if other_batteries[1] > battery[1]:
                    higher_index += 1

            # If the battery has an index that allows for enough batteries to be found after it, update lowest_index
            if (battery[1] >= self.lowest_index) and (battery[1] < len(self.batteries) - batteries_left - higher_index):
                self.lowest_index = battery[1] + 1

    def get_joltage(self):
        # Sort batteries found by index
        self.batteries_found.sort(key=lambda x: x[1])

        # Create joltage string
        for battery in self.batteries_found:
            self.joltage += str(battery[0])
        
        # Set joltage as integer
        self.joltage = int(self.joltage)
