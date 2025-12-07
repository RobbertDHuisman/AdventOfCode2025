import re

class TackyonManifold:
    def __init__(self, diagram):
        self.diagram = diagram
        self.splits = 0
        self.split_beam()
        self.timelines = {}
        self.update_timelines()

    def split_beam(self):
        start_positions = self.find_start()
        for start in start_positions:
            self.propagate_beam(start)
        
        for i in range(2, len(self.diagram)):
            self.continue_or_split(i)
    
    def find_start(self):
        start_positions = []
        for match in re.finditer(r'S', self.diagram[0]):
            start_positions.append([0, match.start()])

        return start_positions
    
    def propagate_beam(self, position):
        self.diagram[position[0] + 1] = self.diagram[0][:position[1]] + '|' + self.diagram[0][position[1] + 1:]

    def continue_or_split(self, row):
        for match in re.finditer(r'\|', self.diagram[row - 1]):
            col = match.start()
            if self.diagram[row][col] == '.':
                self.diagram[row] = self.diagram[row][:col] + '|' + self.diagram[row][col + 1:]
            elif self.diagram[row][col] == '^':
                self.diagram[row] = self.diagram[row][:col - 1] + '|^|' + self.diagram[row][col + 2:]
                self.splits += 1

    def update_timelines(self):
        self.timelines[len(self.diagram) - 1] = {}
        for match in re.finditer(r'\|', self.diagram[-1]):
            col = match.start()
            self.timelines[len(self.diagram) - 1][col] = 1
        
        for i in range(len(self.diagram) - 2, -1, -1):
            self.timelines[i] = {}
            for match in re.finditer(r'\|', self.diagram[i]):
                col = match.start()
                if self.diagram[i + 1][col] == '|':
                    new_value = self.timelines[i + 1][col]
                elif self.diagram[i + 1][col] == '^':
                    new_value = self.timelines[i + 1][col - 1] + self.timelines[i + 1][col + 1]
                
                self.timelines[i][col] = new_value
