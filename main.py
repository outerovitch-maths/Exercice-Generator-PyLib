from math_exercise_generator.exercise_factory import ExerciseFactory


def main():
    print("Welcome to the Math Exercise Generator!")
    print("\n(0) easy\n(1) medium\n(2) hard\n")
    difficulty = input(
        "Choose difficulty : ").lower()

    factory = ExerciseFactory(difficulty)
    exercise = factory.get_random_exercise()

    print("Here is your exercise:")
    print(exercise)


if __name__ == "__main__":
    main()
