class AlgebraExercise:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate(self):
        if self.difficulty == "0":
            return "Solve for x: x + 2 = 5"
        elif self.difficulty == "1":
            return "Solve for x: 3x^2 + 2x - 5 = 0"
        elif self.difficulty == "2":
            return "Solve for x: x^3 - 2x + 1 = 0"
