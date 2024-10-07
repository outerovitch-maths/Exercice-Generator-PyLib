import unittest
from math_exercise_generator.geometry import GeometryExercise

class TestGeometryExercise(unittest.TestCase):
    def test_generate_easy(self):
        exercise = GeometryExercise("easy")
        self.assertIn("area of a rectangle", exercise.generate())

    def test_generate_medium(self):
        exercise = GeometryExercise("medium")
        self.assertIn("area of a circle", exercise.generate())

    def test_generate_hard(self):
        exercise = GeometryExercise("hard")
        self.assertIn("volume of a cylinder", exercise.generate())

if __name__ == "__main__":
    unittest.main()
