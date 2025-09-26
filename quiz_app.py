import json

def load_questions(filename):
    """Load quiz questions from a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)

def ask_question(q):
    """Ask a single question and check if user's answer is correct."""
    print("\n" + q['question'])
    for i, option in enumerate(q['options'], 1):
        print(f"{i}. {option}")
    while True:
        try:
            answer = int(input("Your answer (1-4): "))
            if 1 <= answer <= len(q['options']):
                return answer == q['answer']
            else:
                print("Please enter a valid option number.")
        except ValueError:
            print("Please enter a number.")

def quiz():
    """Run the quiz game."""
    questions = load_questions('questions.json')
    score = 0
    for i, q in enumerate(questions, 1):
        if ask_question(q):
            print("Correct!")
            score += 1
        else:
            correct_option = q['options'][q['answer'] - 1]
            print(f"Wrong! The correct answer was: {correct_option}")
    print(f"\nQuiz completed! Your score: {score} out of {len(questions)}")

if __name__ == "__main__":
    quiz()
