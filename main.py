import json
import random
import auth
import scores

def load_questions():
    try:
        with open('questions.json', 'r') as f:
            data = json.load(f)
        questions = data.get('questions', [])
        if not questions:
            raise ValueError("No questions to pull from.")
        return questions
    except FileNotFoundError:
        raise ValueError("questions.json file not found.")
    except json.JSONDecodeError:
        raise ValueError("questions.json is malformed.")

def main():
    print("Welcome to the Python Quiz App!")
    
    # Load questions early to check
    try:
        questions = load_questions()
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    # Authentication
    username = None
    while True:
        choice = input("Do you want to (l)ogin or (r)egister? ").strip().lower()
        if choice not in ['l', 'r']:
            print("Invalid choice. Please enter 'l' or 'r'.")
            continue
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        try:
            if choice == 'r':
                auth.register(username, password)
                break
            else:
                auth.login(username, password)
                break
        except ValueError as e:
            print(f"Error: {e}")
            continue
    total_questions = len(questions)
    
    # Ask number of questions
    while True:
        try:
            num_str = input(f"How many questions do you want to answer? (1-{total_questions}): ").strip()
            if not num_str.isdigit():
                raise ValueError("Invalid input. Please enter a number.")
            num_questions = int(num_str)
            if 1 <= num_questions <= total_questions:
                break
            else:
                raise ValueError(f"Please enter a number between 1 and {total_questions}.")
        except ValueError as e:
            print(f"Error: {e}")
            continue
    
    # Select random questions
    selected_questions = random.sample(questions, num_questions)
    
    total_score = 0
    
    for q in selected_questions:
        print(f"\nCategory: {q['category']}")
        print(q['question'])
        if q['type'] == 'multiple_choice':
            for i, opt in enumerate(q['options'], 1):
                print(f"{i}. {opt}")
        
        # Offer hint
        hint_used = False
        while True:
            hint_input = input("Do you want a hint? (y/n): ").strip().lower()
            if hint_input in ['y', 'n']:
                break
            print("Error: Invalid input for hint. Please enter 'y' or 'n'.")
        if hint_input == 'y':
            print(f"Hint: {q['hint']}")
            hint_used = True
        
        # Get answer
        if q['type'] == 'multiple_choice':
            while True:
                try:
                    ans_str = input("Your answer (number): ").strip()
                    if not ans_str.isdigit():
                        raise ValueError("Please enter a number.")
                    ans_num = int(ans_str)
                    if 1 <= ans_num <= len(q['options']):
                        user_answer = q['options'][ans_num - 1]
                        break
                    else:
                        raise ValueError("Invalid number.")
                except ValueError as e:
                    print(f"Error: {e}")
                    continue
        elif q['type'] == 'true_false':
            while True:
                user_answer = input("Your answer (true/false): ").strip().lower()
                if user_answer in ['true', 'false']:
                    break
                print("Error: Please enter 'true' or 'false'.")
        else:  # short answer
            while True:
                user_answer = input("Your answer: ").strip()
                if user_answer:
                    break
                print("Error: Answer cannot be empty.")
        
        # Check answer
        correct = user_answer == q['answer']
        points = 10 if not hint_used else 5
        if correct:
            print("Correct!")
            total_score += points
        else:
            print(f"Incorrect. The correct answer is: {q['answer']}")
            if not hint_used:
                total_score += 0
    
    print(f"\nQuiz complete! Your total score: {total_score}")
    scores.update_score(username, total_score)

if __name__ == "__main__":
    main()