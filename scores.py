# Phase 3: Fixes after AI review
import pickle
import os

SCORES_FILE = 'scores.pkl'

def load_scores():
    if os.path.exists(SCORES_FILE):
        try:
            with open(SCORES_FILE, 'rb') as f:
                return pickle.load(f)
        except Exception:
            raise ValueError("scores.pkl is corrupted.")
    return {}

def save_scores(scores):
    with open(SCORES_FILE, 'wb') as f:
        pickle.dump(scores, f)

def update_score(username, score):
    scores = load_scores()
    if username not in scores:
        scores[username] = {'total_score': 0, 'quizzes_taken': 0}
    scores[username]['total_score'] += score
    scores[username]['quizzes_taken'] += 1
    save_scores(scores)