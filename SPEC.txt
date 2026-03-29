The app greets the user, asks how many questions they want, and then randomly picks that many questions from the question bank, and uses them to quiz the user. It will be a command line interface quiz app. There will be a point system, as well as hints. a hint reduces the amount of points a user will be able to get for a correct answer. A hint will reveal the hint that corresponds to each of the questions below. Of course, a user may only use one hint per question (as there are not more, by convention).
{
  "questions": [
    {
      "id": 101,
      "question": "What is 10 // 3 in Python?",
      "type": "multiple_choice",
      "options": ["3.33", "3", "3.0", "1"],
      "answer": "3",
      "category": "Operations"
      "hint": "// is integer division"
    },
    {
      "id": 102,
      "question": "A Python dictionary can have duplicate keys.",
      "type": "true_false",
      "answer": "false",
      "category": "Dictionaries"
      "hint": "would two of the same key have different hash values?"
    },
    {
      "id": 103,
      "question": "Which method is used to remove and return an element of a list?",
      "type": "short answer",
      "answer": "pop()",
      "category": "Lists"
      "remember to include (), because it's a method"
    },
    {
      "id": 104,
      "question": "What is the value of 'Python'[1:3]?",
      "type": "multiple_choice",
      "options": ["Py", "yt", "ytho", "yth"],
      "answer": "yt",
      "category": "Strings"
      "hint": "Is the upper bound inclusive or exclusive?"
    },
    {
      "id": 105,
      "question": "5 in range(5)",
      "type": "true_false",
      "answer": "false",
      "category": "Loops"
      "hint": "is the range parameter inclusive or exclusive?"
    }
  ]
}
we should have main.py which has the loop + user interface + quiz taking logic.
questions.json, which stores the question bank
we need a local login system, so we need an auth.py file that can handle this logic
we also need to track scores and performance statistics securely (in a non-human readable format), and of course saves those results. im not sure how you want to go about that, but if we need an additional file for it please make sure we make one.

error verification:
if the json file is empty, we should raise an exception and state that no questions to pull from.
if a user inputs an invalid input (say a non-alphanumerical string), raise an exception with a print statement
if a tries to login with account information that hasn't been saved before, raise an exception with a print statement.
