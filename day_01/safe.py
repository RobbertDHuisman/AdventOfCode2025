from math import ceil, floor

class Safe():
    def __init__(self, starting_position = 50):
        self.position = starting_position
        self.at_zero_counter = 0
        self.past_zero_counter = 0
    
    def rotate(self, step):
        # Determine starting position
        start_position = self.position

        # Determine which way to rotate and calculate new position
        if step[0] == 'L':
            new_position = self.position - (int(step[1:]))
        elif step[0] == 'R':
            new_position = self.position + int(step[1:])

        # Update counters
        self.update_at_zero()
        self.update_past_zero(new_position, start_position)

        # Update position within bounds 0-99
        self.position = new_position % 100

    def update_at_zero(self):
        # If ending position is zero, increment counter
        if self.position == 0:
            self.at_zero_counter += 1
    
    def update_past_zero(self, new_position, start_position):
        # Look at negative end positions
        if new_position < 0:
            # If starting at zero, take the floor to not count the start
            if start_position == 0:
                past_zero_steps = floor(abs(new_position) / 100)
            # Else take the ceil to count crossing the first zero
            else:
                past_zero_steps = ceil(abs(new_position) / 100)

        # Look at positive end positions and take floor as we always cross zero first time at 100
        elif new_position > 100:
            past_zero_steps = floor(new_position / 100)

        # Otherwise no crossing, so set to 0
        else:
            past_zero_steps = 0

        # If the end position is exactly on zero, reduce the count by 1 as we don't count stopping at zero
        if (new_position > 0) and (new_position % 100 == 0) and (past_zero_steps > 0):
            past_zero_steps -= 1
        
        # Add to counter
        self.past_zero_counter += past_zero_steps        

        # Print debug info
        # if past_zero_steps > 0:
            # print(f"start is {start_position}, steps is {steps}, new is {new_position} so times past zero is: {past_zero_steps}")
