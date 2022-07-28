__author__ = 'Dheeraj'

import os

from pylint import lint


def check_score_for(list_of_files_or_module, threshold):
    run = lint.Run(list_of_files_or_module, do_exit=False)
    print(run)
    score = run.linter.stats['global_note']
    print("\n\n----------------------------------")
    print("YOUR SCORE IS  : " + str(score))
    print("----------------------------------")
    print("REQUIRED SCORE : " + str(threshold))
    print("----------------------------------\n\n")
    if score < threshold:
        raise ValueError("Your Score is less than the standards for ML-Personalised-FrameWork to commit. Please "
                         "update your code changes")
    else:
        print("OK")


files_to_check = []

for root, dirs, files in os.walk("main"):
    for file in files:
        if file.endswith(".py"):
            files_to_check.append(os.path.join(root, file))

check_score_for(["ML-Personalised-FrameWork"], 9.01)
check_score_for(files_to_check, 8.40)
