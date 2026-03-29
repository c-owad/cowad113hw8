# Phase 3: Fixes after AI review
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

def get_valid_int(prompt, min_val, max_val):
    while True:
        try:
            val_str = input(prompt).strip()
            if not val_str.isdigit():
                raise ValueError("Invalid input. Please enter a number.")
            val = int(val_str)
            if min_val <= val <= max_val:
                return val
            else:
                raise ValueError(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError as e:
            print(f"Error: {e}")

def get_valid_choice(prompt, options):
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice
        print(f"Error: Invalid input. Please enter one of {options}.")

def get_non_empty_input(prompt):
    while True:
        inp = input(prompt).strip()
        if inp:
            return inp
        print("Error: Input cannot be empty.")

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
    num_questions = get_valid_int(f"How many questions do you want to answer? (1-{total_questions}): ", 1, total_questions)
    
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
        hint_input = get_valid_choice("Do you want a hint? (y/n): ", ['y', 'n'])
        if hint_input == 'y':
            print(f"Hint: {q['hint']}")
            hint_used = True
        
        # Get answer
        if q['type'] == 'multiple_choice':
            ans_num = get_valid_int("Your answer (number): ", 1, len(q['options']))
            user_answer = q['options'][ans_num - 1]
        elif q['type'] == 'true_false':
            user_answer = get_valid_choice("Your answer (true/false): ", ['true', 'false'])
        else:  # short answer
            user_answer = get_non_empty_input("Your answer: ")
        
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