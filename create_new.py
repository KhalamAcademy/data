# Crates a subject and/or a chapter in a subject
import os
import shutil
import sys
import common

info = common.load_yaml("core/info.yaml")
subjects = common.load_yaml("core/subjects.yaml")

# Create the grade
grade = common.input_int("Enter grade? ")

if grade > 12 or grade <= 0:
    print("Invalid grade")
    sys.exit(-1)

grade_path = f"grades/{grade}"

if not os.path.exists("grades"):
    os.mkdir("grades")

if not os.path.exists(grade_path):
    os.mkdir(grade_path)

board = input("Enter board? ")

if board.upper() not in info["boards"]:
    print("Board not in core/info.yaml!")
    sys.exit(-1)

board_path = f"{grade_path}/{board.lower()}"

if not os.path.exists(board_path):
    os.mkdir(board_path)

subject = input("Enter subject name? ")

if subject.lower() not in subjects["subjects"].keys():
    print("Subject not in info.yaml!")
    sys.exit(-1)  

subject_path = f"{board_path}/{subject.lower()}"

if not os.path.exists(subject_path):
    os.mkdir(subject_path)

chapters = [int(chapter) for chapter in os.listdir(subject_path)]

if chapters:
    chapters.sort()
    next_chapter = chapters[-1] + 1
else:
    next_chapter = 1

chapter_path = f"{subject_path}/{next_chapter}"

os.mkdir(chapter_path)

shutil.copyfile("templates/chapter_info.yaml", f"{chapter_path}/info.yaml")
shutil.copyfile("templates/chapter_resources.yaml", f"{chapter_path}/res.yaml")