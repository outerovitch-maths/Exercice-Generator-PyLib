class GeometryExercise:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate(self):
        if self.difficulty == "0":
            return "Find the area of a rectangle with length 5 and width 3."
        elif self.difficulty == "1":
            return "Find the area of a circle with radius 4."
        elif self.difficulty == "2":
            return "Find the volume of a cylinder with radius 3 and height 7."
