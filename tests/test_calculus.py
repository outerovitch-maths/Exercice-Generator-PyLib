import unittest
from math_exercise_generator.calculus import CalculusExercise

class TestCalculusExercise(unittest.TestCase):
    def test_generate_easy(self):
        exercise = CalculusExercise("easy")
        self.assertIn("Differentiate", exercise.generate())

    def test_generate_medium(self):
        exercise = CalculusExercise("medium")
        self.assertIn("Integrate", exercise.generate())

    def test_generate_hard(self):
        exercise = CalculusExercise("hard")
        self.assertIn("differential equation", exercise.generate())

if __name__ == "__main__":
    unittest.main()
