import numpy as np

class JunctionBox:
    def __init__(self, points, nr_connections):
        self.points = points
        self.nr_connections = nr_connections
        self.shortest_distance_found = 0
        self.circuits = [[i] for i in range(len(points))]
        # print(self.circuits)
        self.create_matrix()
        self.create_nr_of_circuits()
        self.calculate_product()
        self.creat_one_big_circuit()
        self.find_final_length()

    def create_nr_of_circuits(self):
        for _ in range(self.nr_connections):
            self.find_closest_points()
            self.update_circuits()
            self.update_distance_matrix()

    def create_matrix(self):
        diff = self.points[:, np.newaxis, :] - self.points[np.newaxis, :, :]
        self.distance_matrix = np.sqrt(np.sum(diff**2, axis=2))
        
    def find_closest_points(self):
        np.fill_diagonal(self.distance_matrix, np.inf)
        self.min_idx = np.unravel_index(self.distance_matrix.argmin(), self.distance_matrix.shape)
        self.min_distance = self.distance_matrix[self.min_idx]
        # print(f"found points {self.min_idx} with distance {self.min_distance}")

    def update_circuits(self):
        first, second = self.min_idx
        for i in range(len(self.circuits)):
            if first in self.circuits[i]:
                first_circuit = i
            if second in self.circuits[i]:
                second_cicuit = i

        if first_circuit != second_cicuit:
            for point in self.circuits[first_circuit]:
                if point not in self.circuits[second_cicuit]:
                    self.circuits[second_cicuit].append(point)
            self.circuits.remove(self.circuits[first_circuit])
        
        # print(self.circuits)

    def update_distance_matrix(self):
        first, second = self.min_idx
        self.distance_matrix[self.min_idx] = np.inf
        self.distance_matrix[(second, first)] = np.inf

    def calculate_product(self):
        self.lengths = [len(circuit) for circuit in self.circuits]
        self.lengths.sort(reverse=True)

    # Part 2
    def creat_one_big_circuit(self):
        while len(self.circuits) > 1:
            self.find_closest_points()
            self.update_circuits()
            self.update_distance_matrix()

    def find_final_length(self):
        first, second = self.min_idx
        x1, y1, z1 = self.points[first]
        x2, y2, z2 = self.points[second]
        self.final_length = x1*x2
