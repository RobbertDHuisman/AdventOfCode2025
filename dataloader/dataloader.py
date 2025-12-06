class Dataloader():
    def __init__(self, path, isstrip=True):
        self.path = path
        self.isstrip = isstrip
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.path, 'r') as file:
                data = file.readlines()
            if self.isstrip:
                return [line.strip() for line in data]
            else:
                return data
        except FileNotFoundError:
            print(f"Error: The file at {self.path} was not found.")
            return []