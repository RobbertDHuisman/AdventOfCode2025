class Inventory():
    def __init__(self, data):
        self.data = data
        self.fresh_ranges = []
        self.non_overlapping_fresh_ranges = []
        self.ingredients = []
        self.fresh_ingredients = []
        self.spoiled_ingredients = []
        self.nr_fresh_ids = 0
        self.devide_input_data()
        self.check_freshness()
        self.determine_non_overlapping_fresh_ranges()
        self.determine_nr_fresh_ids()
        
    def devide_input_data(self):
        # Go through input data and devide it in ranges and ingredients
        for line in self.data:
            # Ranges have a '-' in them
            if '-' in line:
                start = line.split('-')[0]
                end = line.split('-')[1]
                self.fresh_ranges.append([int(start), int(end)])
            # Skipt the empty line
            elif line == "":
                continue
            # The rest are ingredients
            else:
                self.ingredients.append(int(line))
    
    def check_freshness(self):
        # Check each ingredient if it's within a fresh range
        for ingredient in self.ingredients:
            for fresh_range in self.fresh_ranges:
                if fresh_range[0] <= ingredient <= fresh_range[1]:
                    self.fresh_ingredients.append(ingredient)
                    break

            # If not found in any fresh range, it's spoiled
            self.spoiled_ingredients.append(ingredient)

    def determine_non_overlapping_fresh_ranges(self):
        # Sort ranges on start value
        self.fresh_ranges.sort(key=lambda x: x[0])

        # Go through each range
        for fresh_range in self.fresh_ranges:
            # Set the first range as non overlapping
            if not self.non_overlapping_fresh_ranges:
                self.non_overlapping_fresh_ranges.append(fresh_range)
            else:
                # Check if the current range overlaps with the last non overlapping range
                last_range = self.non_overlapping_fresh_ranges[-1]
                if fresh_range[0] <= last_range[1]:
                    # If so, extend the last non overlapping range with the end id of the current range
                    if fresh_range[1] > last_range[1]:
                        self.non_overlapping_fresh_ranges[-1][1] = fresh_range[1]
                
                # If they don't overlap, add the current range as new non overlapping range
                else:
                    self.non_overlapping_fresh_ranges.append(fresh_range)

    def determine_nr_fresh_ids(self):
        for fresh_range in self.non_overlapping_fresh_ranges:
            self.nr_fresh_ids += fresh_range[1] - fresh_range[0] + 1