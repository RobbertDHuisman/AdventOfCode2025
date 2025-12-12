import numpy as np

class MovieTheater:
    def __init__(self, red_tiles):
        self.red_tiles = red_tiles
        self.create_area_matrix()
        self.new_area_matrix = self.area_matrix.copy()
        self.create_tile_matrix()
        # print(self.tile_matrix)

        # self.largest_rectangle = 0
        # self.determine_areas()

    def create_area_matrix(self):
        diff = self.red_tiles[:, np.newaxis, :] - self.red_tiles[np.newaxis, :, :]
        self.area_matrix = np.prod(abs(diff) + 1, axis=2)
        
    def create_tile_matrix(self):
        dimensions = self.red_tiles.max(axis=0) + 2
        self.tile_matrix = np.ones((dimensions[1], dimensions[0]), dtype=np.int8)
        for i in range(1, len(self.red_tiles)):
            print(i)
            x0, y0 = self.red_tiles[i-1]
            x1, y1 = self.red_tiles[i]
            self.create_line_and_determine_out_of_area(x0, y0, x1, y1)
            # print(self.tile_matrix)
        
        # Add last connection
        x0, y0 = self.red_tiles[-1]
        x1, y1 = self.red_tiles[0]
        self.create_line_and_determine_out_of_area(x0, y0, x1, y1)

        # Set self.borders to 1
        # self.tile_matrix[self.tile_matrix == 2] = 1
        
    def create_line_and_determine_out_of_area(self, x0, y0, x1, y1):
        self.create_line_between_tiles(x0, y0, x1, y1)
        self.update_tiles(x0, y0, x1, y1)

    def create_line_between_tiles(self, x0, y0, x1, y1):
        self.tile_matrix[min(y0, y1):max(y0, y1)+1, min(x0, x1):max(x0, x1)+1] = 2
        
    def update_tiles(self, x0, y0, x1, y1):
        # Going right means up out of area and down till next border in area
        if x1 > x0:
            self.matrix_above = self.tile_matrix[:y0, x0:x1 + 1]
            if np.where(self.matrix_above == 2)[0].size > 0:
                for x in range(x0, x1 + 1):
                    self.matrix_above = self.tile_matrix[:y0, x]
                    if max(self.matrix_above) == 2:
                        self.borders = np.where(self.matrix_above == 2)[0]
                        self.limit = self.borders[-1]
                        self.tile_matrix[self.limit + 1:y0, x] = 0
                    else:
                        self.tile_matrix[:y0, x] = 0
            else:
                self.tile_matrix[:y0, x0:x1 + 1] = 0

            self.matrix_below = self.tile_matrix[y0 + 1:, x0:x1 + 1]
            if np.where(self.matrix_below == 2)[0].size > 0:
                for x in range(x0, x1 + 1):
                    self.matrix_below = self.tile_matrix[y0 + 1:, x]
                    if max(self.matrix_below) == 2:
                        self.borders = np.where(self.matrix_below == 2)[0]
                        self.limit = self.borders[0] + y0
                        self.tile_matrix[y0 + 1:self.limit, x] = 1
                    else:
                        self.tile_matrix[y0 + 1:, x] = 1
            else:
                self.tile_matrix[y0 + 1:, x0:x1 + 1] = 1

        # Going left means down out of area and up till next border in area
        elif x1 < x0:
            self.matrix_above = self.tile_matrix[:y0, x1:x0 + 1]
            if np.where(self.matrix_above == 2)[0].size > 0:
                for x in range(x1, x0 + 1):
                    self.matrix_above = self.tile_matrix[:y0, x]
                    if max(self.matrix_above) == 2:
                        self.borders = np.where(self.matrix_above == 2)[0]
                        self.limit = self.borders[-1]
                        self.tile_matrix[self.limit + 1:y0, x] = 1
                    else:
                        self.tile_matrix[:y0, x] = 1
            else:
                self.tile_matrix[:y0, x1:x0 + 1] = 1

            self.matrix_below = self.tile_matrix[y0 + 1:, x1:x0 + 1]
            if np.where(self.matrix_below == 2)[0].size > 0:
                for x in range(x1, x0 + 1):
                    self.matrix_below = self.tile_matrix[y0 + 1:, x]
                    if max(self.matrix_below) == 2:
                        self.borders = np.where(self.matrix_below == 2)[0]
                        self.limit = self.borders[0] + y0
                        self.tile_matrix[y0 + 1:self.limit, x] = 0
                    else:
                        self.tile_matrix[y0 + 1:, x] = 0
            else:
                self.tile_matrix[y0 + 1:, x1:x0 + 1] = 0

        # Going down means right out of area and left till next border in area
        elif y1 > y0:
            self.matrix_right = self.tile_matrix[y0:y1 + 1, x0 + 1:]
            if np.where(self.matrix_right == 2)[0].size > 0:
                for y in range(y0, y1 + 1):
                    self.matrix_right = self.tile_matrix[y, x0 + 1:]
                    if max(self.matrix_right) == 2:
                        self.borders = np.where(self.matrix_right == 2)[0]
                        self.limit = self.borders[0] + x0
                        self.tile_matrix[y, x0 + 1:self.limit] = 0
                    else:
                        self.tile_matrix[y, x0 + 1:] = 0
            else:
                self.tile_matrix[y0:y1 + 1, x0 + 1:] = 0

            self.matrix_left = self.tile_matrix[y0:y1 + 1, :x0]
            if np.where(self.matrix_left == 2)[0].size > 0:
                for y in range(y0, y1 + 1):
                    self.matrix_left = self.tile_matrix[y, :x0]
                    if max(self.matrix_left) == 2:
                        self.borders = np.where(self.matrix_left == 2)[0]
                        self.limit = self.borders[-1]
                        self.tile_matrix[y, self.limit + 1:x0] = 1
                    else:
                        self.tile_matrix[y, :x0] = 1
            else:
                self.tile_matrix[y0:y1+ 1, :x0] = 1

        # Going up means left out of area and right till next border in area
        elif y1 < y0:
            self.matrix_right = self.tile_matrix[y1:y0 + 1, x0 + 1:]
            if np.where(self.matrix_right == 2)[0].size > 0:
                for y in range(y1, y0 + 1):
                    self.matrix_right = self.tile_matrix[y, x0 + 1:]
                    if max(self.matrix_right) == 2:
                        self.borders = np.where(self.matrix_right == 2)[0]
                        self.limit = self.borders[0] + x0
                        self.tile_matrix[y, x0 + 1:self.limit] = 1
                    else:
                        self.tile_matrix[y, x0 + 1:] = 1
            else:
                self.tile_matrix[y1:y0 + 1, x0 + 1:] = 1

            self.matrix_left = self.tile_matrix[y1:y0 + 1, :x0]
            if np.where(self.matrix_left == 2)[0].size > 0:
                for y in range(y1, y0 + 1):
                    self.matrix_left = self.tile_matrix[y, :x0]
                    if max(self.matrix_left) == 2:
                        self.borders = np.where(self.matrix_left == 2)[0]
                        self.limit = self.borders[-1]
                        self.tile_matrix[y, self.limit + 1:x0] = 0
                    else:
                        self.tile_matrix[y, :x0] = 0
            else:
                self.tile_matrix[y1:y0 + 1, :x0] = 0
        
    def determine_areas(self):
        for i in range(len(self.red_tiles)):
            for j in range(i + 1, len(self.red_tiles)):
                # print(i, j, self.red_tiles[i], self.red_tiles[j])
                x0, y0 = self.red_tiles[i]
                x1, y1 = self.red_tiles[j]
                if not self.check_validity(x0, x1, y0, y1):
                    self.new_area_matrix[i, j] = 0
                    self.new_area_matrix[j, i] = 0

                # matrix = self.tile_matrix[min(y0, y1):max(y0, y1)+1, min(x0, x1):max(x0, x1)+1]
                # if np.where(matrix == 0)[0].size == 0:
                #     if sum(matrix.flatten()) > self.largest_rectangle:
                        # self.largest_rectangle = sum(matrix.flatten())

    def check_validity(self, x0, x1, y0, y1):
        check_corners = [
            [y0, x1],
            [y1, x0]
        ]
        for corner in check_corners:
            xaxis = self.tile_matrix[:y0, corner[1]]
            yaxis = self.tile_matrix[corner[0], :x0]
            xaxis_borders = np.where(xaxis == 2)[0].size
            yaxis_borders = np.where(yaxis == 2)[0].size
            if xaxis_borders % 2 == 1 or xaxis_borders == 0 or yaxis_borders % 2 == 1 or yaxis_borders == 0:
                return False
        print(f"valid area {self.tile_matrix[min(y0, y1):max(y0, y1)+1, min(x0, x1):max(x0, x1)+1]}")
        return True
        # new_area_matrix = self.tile_matrix[min(y0, y1):max(y0, y1)+1, min(x0, x1):max(x0, x1)+1]
        # print(new_area_matrix)
