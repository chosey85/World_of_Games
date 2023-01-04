from pathlib import Path
from etc import Utils


def score_init():
    score_file = open(Utils.scores_file_name(), "w")
    score_file.write(str(0))
    score_file.close()


def add_score(difficulty):
    score_path = Path(Utils.scores_file_name())
    # verify the file exists and create it with value 0 if it doesn't exist
    if not score_path.is_file():
        score_init()
    # set the points calculation method into a variable
    points_of_winning = (int(difficulty)*3) + 5
    # open the file in read mode
    score_file = open(Utils.scores_file_name(), "r")
    old_score_value = score_file.read()
    score_file.close()
    # calculate the new score
    new_score_value = int(old_score_value) + points_of_winning
    # write the new score to the file
    score_file = open(Utils.scores_file_name(), "w")
    score_file.write(str(new_score_value))
    score_file.close()
