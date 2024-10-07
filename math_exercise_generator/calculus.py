class CalculusExercise:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate(self):
        if self.difficulty == "0":
            return "Differentiate f(x) = 2x^2 + 3x."
        elif self.difficulty == "1":
            return "Integrate f(x) = 4x^3."
        elif self.difficulty == "2":
            return "Solve the differential equation dy/dx = x^2 + 1."
