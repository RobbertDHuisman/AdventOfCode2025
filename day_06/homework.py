import re

class Homework():
    def __init__(self, worksheet):
        self.worksheet = worksheet
        self.numbers = []
        self.operators = []
        self.answers = []
        self.right_to_left_numbers = []
        self.correct_answers = []
        self.find_values()
        self.calculate_answers()
        self.find_right_to_left_numbers()
        self.calculate_correct_answers()

    def find_values(self):
        for i in range(len(self.worksheet)):
            if i != len(self.worksheet) - 1:
                numbers, indices_num = self.find_regex(self.worksheet[i], r'\d+')
                self.numbers.append([numbers, indices_num])
            else:
                operators, indices_op = self.find_regex(self.worksheet[i], r'\+|\*')
                self.operators = [operators, indices_op]
            
    def find_regex(self, line, regex_pattern):
        found = []
        indices = []
        for match in re.findall(regex_pattern, line):
            found.append(match)
        for match in re.finditer(regex_pattern, line):
            indices.append(match.start())
        return found, indices

    def calculate_answers(self):
        for i in range(len(self.operators[0])):
            answer = 0
            for numbers in self.numbers:
                if self.operators[0][i] == '+':
                    answer += int(numbers[0][i])
                elif self.operators[0][i] == '*':
                    if answer == 0:
                        answer = int(numbers[0][i])
                    else:
                        answer *= int(numbers[0][i])
            self.answers.append(answer)

    def find_right_to_left_numbers(self):
        numbers = []
        for i in range(len(self.worksheet[0]) - 1, -1, -1):
            number = ''
            for j in range(len(self.worksheet)):
                # print(f"i: {i}, j: {j}")
                if self.worksheet[j][i].isdigit():
                    number += self.worksheet[j][i]
                elif self.worksheet[j][i] in ['+', '*']:
                    numbers.append(number)
                    self.right_to_left_numbers.append(numbers)
                    number = ''
                    numbers = []
            if number:
                numbers.append(number)
        
        # print(self.right_to_left_numbers)


    def calculate_correct_answers(self):
        for i in range(len(self.operators[0]) -1, -1, -1):
            answer = 0
            numbers = self.right_to_left_numbers[len(self.right_to_left_numbers) - 1 -i]
            if self.operators[0][i] == '+':
                for number in numbers:
                    answer += int(number)
            elif self.operators[0][i] == '*':
                for number in numbers:
                    if answer == 0:
                        answer = int(number)
                    else:
                        answer *= int(number)
            self.correct_answers.append(answer)
