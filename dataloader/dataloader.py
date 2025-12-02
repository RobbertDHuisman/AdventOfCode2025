class Dataloader():
    def __init__(self, path, ):
        self.path = path
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.path, 'r') as file:
                data = file.readlines()
            return [line.strip() for line in data]
        except FileNotFoundError:
            print(f"Error: The file at {self.path} was not found.")
            return []