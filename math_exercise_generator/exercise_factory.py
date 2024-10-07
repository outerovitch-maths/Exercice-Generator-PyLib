import random
from math_exercise_generator.algebra import AlgebraExercise
from math_exercise_generator.geometry import GeometryExercise
from math_exercise_generator.calculus import CalculusExercise

class ExerciseFactory:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def get_random_exercise(self):
        exercise_type = random.choice(["algebra", "geometry", "calculus"])

        if exercise_type == "algebra":
            return AlgebraExercise(self.difficulty).generate()
        elif exercise_type == "geometry":
            return GeometryExercise(self.difficulty).generate()
        elif exercise_type == "calculus":
            return CalculusExercise(self.difficulty).generate()
