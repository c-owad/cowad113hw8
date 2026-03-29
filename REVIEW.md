Read [](file:///c%3A/Users/chris/Documents/GitHub/cowad113hw8/SPEC.md)

Read [](file:///c%3A/Users/chris/Documents/GitHub/cowad113hw8/main.py#1-1), lines 1 to 100

Read [](file:///c%3A/Users/chris/Documents/GitHub/cowad113hw8/main.py#101-101), lines 101 to 132

Read [](file:///c%3A/Users/chris/Documents/GitHub/cowad113hw8/auth.py)

Read [](file:///c%3A/Users/chris/Documents/GitHub/cowad113hw8/scores.py)

Read [](file:///c%3A/Users/chris/Documents/GitHub/cowad113hw8/questions.json)

Read [](file:///c%3A/Users/chris/Documents/GitHub/cowad113hw8/users.json)

1. **[PASS]** Greeting the user: The code in main.py correctly greets the user with "Welcome to the Python Quiz App!" as specified.

2. **[PASS]** Asking for number of questions: The code in main.py prompts the user for the number of questions, validates it as a digit, and ensures it's between 1 and the total available questions.

3. **[PASS]** Randomly selecting questions: The code in main.py uses `random.sample` to randomly pick the specified number of questions from the question bank.

4. **[PASS]** Displaying questions with category: For each question, the code in main.py prints the category and question text.

5. **[PASS]** Handling multiple-choice questions: The code in main.py displays options numbered 1 to n for multiple-choice questions.

6. **[PASS]** Offering hints: The code in main.py offers a hint with y/n input validation and displays the hint if requested, limiting to one per question.

7. **[PASS]** Point system with hint penalty: The code in main.py assigns 10 points for correct answers without hints and 5 points with hints; incorrect answers get 0 points.

8. **[PASS]** Answer validation for multiple-choice: The code in main.py validates the answer as a digit within the option range.

9. **[PASS]** Answer validation for true/false: The code in main.py ensures the answer is 'true' or 'false'.

10. **[PASS]** Answer validation for short answer: The code in main.py requires a non-empty string.

11. **[PASS]** Checking answers and providing feedback: The code in main.py compares the answer, prints "Correct!" or the correct answer, and updates the score accordingly.

12. **[PASS]** Displaying final score: The code in main.py prints the total score at the end.

13. **[PASS]** Authentication system: The code in main.py handles login/register with username/password input and calls auth functions.

14. **[PASS]** User registration: The auth.py function registers users, checks for alphanumeric username/password, ensures uniqueness, and saves to users.json.

15. **[PASS]** User login: The auth.py function logs in users, validates alphanumeric, checks credentials, and raises exceptions for invalid attempts.

16. **[PASS]** Score tracking: The scores.py function updates scores securely using pickle, tracking total_score and quizzes_taken.

17. **[PASS]** Loading questions with error handling: The main.py function loads questions.json, checks for emptiness, and raises ValueError with appropriate messages for missing or malformed files.

18. **[PASS]** Invalid input exception for username/password: The auth.py raises ValueError for non-alphanumeric inputs, and main.py prints the error.

19. **[PASS]** Login with unsaved account exception: The auth.py raises ValueError for invalid username/password, and main.py prints the error.

20. **[WARN]** Security concern: Passwords are stored in plain text in users.json, which is insecure. Consider hashing passwords (e.g., using bcrypt).

21. **[WARN]** Missing error handling in auth.py: If users.json is corrupted (e.g., invalid JSON), auth.py will raise an unhandled JSONDecodeError. Add try-except around json.load.

22. **[WARN]** Missing error handling in scores.py: If scores.pkl is corrupted, scores.py will raise an unhandled exception. Add try-except around pickle.load.

23. **[WARN]** Code quality: Repeated input validation loops in [main.py](main.py#L35-47, 62-68, 70-79, 81-85, 87-91) could be refactored into helper functions to reduce duplication.

24. **[PASS]** Question bank structure: The questions.json matches the spec with id, question, type, options (for MC), answer, category, hint.

25. **[PASS]** File structure: All required files (main.py, auth.py, scores.py, questions.json, users.json) are present and named correctly.
