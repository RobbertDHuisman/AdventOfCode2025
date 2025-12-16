import re
import numpy as np
from sympy.solvers import solve
from sympy.abc import a, b, c, d, e, f, g, h, i, j, k, l, m
from scipy.optimize import milp, LinearConstraint, Bounds

class Machine:
    def __init__(self, instructions):
        self.instructions = instructions
        self.read_instructions()
        self.turn_off()
        self.reach_joltage()

    def read_instructions(self):
        lights = re.findall(r'\[.*\]', self.instructions)[0]
        self.lights = [True if x =='#' else False for x in lights[1:-1]]
        
        self.buttons = []
        buttons = re.findall(r'\([\d|,]*\)', self.instructions)
        for button in buttons:
            nums = button[1:-1].split(',')
            self.buttons.append([int(num) for num in nums])
        
        joltage = re.findall(r'\{.*\}', self.instructions)
        self.joltage = [int(x) for x in joltage[0][1:-1].split(',')]

    def turn_off(self):
        """Reverse of turn on to determine the amount of presses to turn off all lights"""
        all_lights = [self.lights.copy()]
        found = False
        self.buttons_pressed = 0
        while not found:
            self.buttons_pressed += 1
            new_lights = []
            for lights in all_lights:
                for button in self.buttons:
                    lights_copy = lights.copy()
                    for index in button:
                        if lights_copy[index]:
                            lights_copy[index] = False
                        else:
                            lights_copy[index] = True
                    new_lights.append(lights_copy)
                    if all(not light for light in lights_copy):
                        found = True
                        break
                if found:
                    break
            all_lights = new_lights

    def reach_joltage(self):
        joltage_buttons = []
        for button in self.buttons:
            new_button = np.array([])
            for p in range(len(self.joltage)):
                if p in button:
                    new_button = np.append(new_button, 1)
                else:
                    new_button = np.append(new_button, 0)
            joltage_buttons.append(new_button)

        # Convert joltage_buttons to coefficient matrix (each button is a column)
        A = np.array(joltage_buttons[:len(self.buttons)]).T  # Transpose to get equations x variables
        b = np.array(self.joltage)
        
        # Minimize sum of button presses: min(x1 + x2 + ... + xn)
        c = np.ones(len(self.buttons))  # Coefficients for objective function
        
        # Constraints: A * x = b (each equation must equal the target joltage)
        constraints = LinearConstraint(A, b, b)  # Equality constraint
        
        # Bounds: all variables >= 0
        bounds = Bounds(0, np.inf)
        
        # All variables must be integers (1 = integer, 0 = continuous)
        integrality = np.ones(len(self.buttons))
        
        # Solve the integer linear program
        result = milp(c, constraints=constraints, bounds=bounds, integrality=integrality)
        
        if result.success:
            self.joltage_buttons_pressed = int(result.fun)
            self.button_presses = result.x.astype(int)
            print(f"Minimum button presses: {self.joltage_buttons_pressed}")
            print(f"Button press counts: {self.button_presses}")
        else:
            print("No solution found")
            self.joltage_buttons_pressed = None

