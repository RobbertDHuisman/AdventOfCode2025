class IdChecker():
    def __init__(self, id_ranges):
        self.id_ranges = id_ranges
        self.valid_ids = []
        self.valid_ids_2 = []
        self.invalid_ids = []
        self.invalid_ids_2 = []
        self.check_id_in_range()

    def check_id_in_range(self):
        for id_range in self.id_ranges:
            start, end = map(str, id_range.split("-"))
            self.check_if_ids_valid(start, end)
            self.check_all_patterns(start, end)
    
    def check_if_ids_valid(self, start, end):
        # Go through each ID in the range
        for id in range(int(start), int(end) + 1):
            id = str(id)
            # If odd length, automatically valid
            if len(id) % 2 == 1:
                self.valid_ids.append(int(id))
            else:
                # Check if first half different from second half. If so, valid
                if id[:int(len(id)/2)] != id[int(len(id)/2):]:
                    self.valid_ids.append(int(id))
                # Else, invalid
                else:
                    self.invalid_ids.append(int(id))

    def check_all_patterns(self, start, end):
        # Go through each ID in the range
        for id in range(int(start), int(end) + 1):
            id = str(id)
            for i in range(1, int(len(id)/2) + 1):
                if self.check_options(id, i):
                    self.invalid_ids_2.append(int(id))
                    break

    def check_options(self, id, modulo):
        # Check if length of id is multiple of modulo
        if len(id) % modulo != 0:
            return False
        
        # If so, check each segment
        pair = id[0:modulo]
        for i in range(modulo, len(id), modulo):
            if id[i:i+modulo] != pair:
                return False
        return True