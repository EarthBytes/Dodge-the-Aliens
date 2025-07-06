import os
import datetime

HIGH_SCORE_FILE = "high_scores.txt"

def save_score(name, score):
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{name},{score},{time_now}\n"
    with open(HIGH_SCORE_FILE, "a") as f:
        f.write(line)

def get_high_scores(limit=5):
    if not os.path.exists(HIGH_SCORE_FILE):
        return []
    with open(HIGH_SCORE_FILE, "r") as f:
        lines = f.readlines()
    scores = [line.strip().split(",") for line in lines]
    scores.sort(key=lambda x: int(x[1]), reverse=True)
    return scores[:limit]
