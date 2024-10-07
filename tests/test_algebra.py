import unittest
from math_exercise_generator.algebra import AlgebraExercise

class TestAlgebraExercise(unittest.TestCase):
    def test_generate_easy(self):
        exercise = AlgebraExercise("easy")
        self.assertIn("x + 2 = 5", exercise.generate())

    def test_generate_medium(self):
        exercise = AlgebraExercise("medium")
        self.assertIn("3x^2 + 2x - 5 = 0", exercise.generate())

    def test_generate_hard(self):
        exercise = AlgebraExercise("hard")
        self.assertIn("x^3 - 2x + 1 = 0", exercise.generate())

if __name__ == "__main__":
    unittest.main()
