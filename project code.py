# AI-BASED STUDENT STUDY PLANNER
# Python Console Project
# Concepts: OOP, Lists, Dictionaries, Sorting, Priority Calculation,
# File Handling, Input Validation and Recommendation Logic

from datetime import datetime, date
import json
import os


class Subject:
    def __init__(self, name, difficulty, exam_date, study_hours):
        self.name = name
        self.difficulty = difficulty
        self.exam_date = exam_date
        self.study_hours = study_hours
        self.priority = 0

    def calculate_priority(self):
        today = date.today()
        exam = datetime.strptime(self.exam_date, "%Y-%m-%d").date()

        days_left = (exam - today).days

        if days_left <= 0:
            days_left = 1

        # AI-inspired priority calculation
        urgency = 30 / days_left
        difficulty_score = self.difficulty * 10

        self.priority = round(difficulty_score + urgency, 2)

        return self.priority

    def to_dict(self):
        return {
            "name": self.name,
            "difficulty": self.difficulty,
            "exam_date": self.exam_date,
            "study_hours": self.study_hours,
            "priority": self.priority
        }


class StudyTask:
    def __init__(self, subject, title, hours, priority):
        self.subject = subject
        self.title = title
        self.hours = hours
        self.priority = priority
        self.status = "Pending"

    def complete(self):
        self.status = "Completed"

    def to_dict(self):
        return {
            "subject": self.subject,
            "title": self.title,
            "hours": self.hours,
            "priority": self.priority,
            "status": self.status
        }


class AIStudyPlanner:

    def __init__(self):
        self.subjects = []
        self.tasks = []

    # ---------------- SUBJECT MANAGEMENT ----------------

    def add_subject(self):
        print("\n========== ADD SUBJECT ==========")

        name = input("Enter subject name: ").strip()

        if not name:
            print("Subject name cannot be empty.")
            return

        try:
            difficulty = int(input("Enter difficulty (1-5): "))

            if difficulty < 1 or difficulty > 5:
                print("Difficulty must be between 1 and 5.")
                return

            exam_date = input(
                "Enter exam date (YYYY-MM-DD): "
            ).strip()

            datetime.strptime(exam_date, "%Y-%m-%d")

            study_hours = float(
                input("Enter available study hours: ")
            )

            if study_hours <= 0:
                print("Study hours must be greater than zero.")
                return

            subject = Subject(
                name,
                difficulty,
                exam_date,
                study_hours
            )

            subject.calculate_priority()

            self.subjects.append(subject)

            print("\nSubject added successfully!")
            print("Priority:", subject.priority)

        except ValueError:
            print("Invalid input.")

    def view_subjects(self):

        print("\n========== SUBJECTS ==========")

        if not self.subjects:
            print("No subjects available.")
            return

        for i, subject in enumerate(self.subjects, 1):

            subject.calculate_priority()

            today = date.today()
            exam = datetime.strptime(
                subject.exam_date,
                "%Y-%m-%d"
            ).date()

            days_left = (exam - today).days

            print(f"""
{i}. {subject.name}
   Difficulty     : {subject.difficulty}/5
   Exam Date      : {subject.exam_date}
   Days Remaining : {days_left}
   Study Hours    : {subject.study_hours}
   Priority Score : {subject.priority}
""")

    def delete_subject(self):

        if not self.subjects:
            print("No subjects available.")
            return

        self.view_subjects()

        try:
            number = int(input("Enter subject number to delete: "))

            if number < 1 or number > len(self.subjects):
                print("Invalid number.")
                return

            deleted = self.subjects.pop(number - 1)

            self.tasks = [
                task for task in self.tasks
                if task.subject != deleted.name
            ]

            print(deleted.name, "deleted successfully.")

        except ValueError:
            print("Invalid input.")

    # ---------------- AI PLANNER ----------------

    def generate_study_plan(self):

        print("\n========== AI STUDY PLAN ==========")

        if not self.subjects:
            print("Please add subjects first.")
            return

        self.tasks.clear()

        # Calculate priority for every subject
        for subject in self.subjects:
            subject.calculate_priority()

        # Highest priority first
        sorted_subjects = sorted(
            self.subjects,
            key=lambda x: x.priority,
            reverse=True
        )

        for subject in sorted_subjects:

            remaining_hours = subject.study_hours
            session_number = 1

            while remaining_hours > 0:

                # Maximum 2 hours per study session
                session_hours = min(2, remaining_hours)

                title = (
                    f"{subject.name} - "
                    f"Study Session {session_number}"
                )

                task = StudyTask(
                    subject.name,
                    title,
                    session_hours,
                    subject.priority
                )

                self.tasks.append(task)

                remaining_hours -= session_hours
                session_number += 1

        print("\nAI-generated study plan:")
        self.display_tasks()

    # ---------------- TASK MANAGEMENT ----------------

    def display_tasks(self):

        if not self.tasks:
            print("No study tasks available.")
            return

        for i, task in enumerate(self.tasks, 1):

            print(
                f"{i}. {task.title} | "
                f"Hours: {task.hours} | "
                f"Priority: {task.priority} | "
                f"Status: {task.status}"
            )

    def complete_task(self):

        if not self.tasks:
            print("No tasks available.")
            return

        self.display_tasks()

        try:
            number = int(
                input("\nEnter task number to complete: ")
            )

            if number < 1 or number > len(self.tasks):
                print("Invalid task number.")
                return

            task = self.tasks[number - 1]

            if task.status == "Completed":
                print("Task is already completed.")
                return

            task.complete()

            print("\nTask completed successfully!")

        except ValueError:
            print("Invalid input.")

    # ---------------- RECOMMENDATION ----------------

    def recommend_next_task(self):

        print("\n========== AI RECOMMENDATION ==========")

        pending_tasks = [
            task for task in self.tasks
            if task.status == "Pending"
        ]

        if not pending_tasks:
            print("No pending tasks.")
            return

        # Highest priority first
        pending_tasks.sort(
            key=lambda task: task.priority,
            reverse=True
        )

        task = pending_tasks[0]

        print("\nRecommended task:")
        print("Subject :", task.subject)
        print("Task    :", task.title)
        print("Hours   :", task.hours)
        print("Priority:", task.priority)

        print(
            "\nReason: This subject has a high priority "
            "based on difficulty and exam urgency."
        )

    # ---------------- ANALYTICS ----------------

    def show_progress(self):

        print("\n========== STUDY ANALYTICS ==========")

        total_tasks = len(self.tasks)

        if total_tasks == 0:
            print("No study data available.")
            return

        completed_tasks = sum(
            1 for task in self.tasks
            if task.status == "Completed"
        )

        total_hours = sum(
            task.hours for task in self.tasks
        )

        completed_hours = sum(
            task.hours
            for task in self.tasks
            if task.status == "Completed"
        )

        progress = (
            completed_tasks / total_tasks
        ) * 100

        print("Total Subjects       :", len(self.subjects))
        print("Total Study Sessions :", total_tasks)
        print("Completed Sessions   :", completed_tasks)
        print("Total Study Hours    :", total_hours)
        print("Completed Hours      :", completed_hours)
        print("Overall Progress     :", round(progress, 2), "%")

        # Progress bar
        bars = int(progress / 5)

        print(
            "[" +
            "#" * bars +
            "-" * (20 - bars) +
            "]"
        )

    # ---------------- FILE HANDLING ----------------

    def save_data(self):

        data = {
            "subjects": [
                subject.to_dict()
                for subject in self.subjects
            ],
            "tasks": [
                task.to_dict()
                for task in self.tasks
            ]
        }

        with open(
            "study_planner_data.json",
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

        print("Data saved successfully.")

    def load_data(self):

        if not os.path.exists(
            "study_planner_data.json"
        ):
            print("No saved data found.")
            return

        try:

            with open(
                "study_planner_data.json",
                "r"
            ) as file:

                data = json.load(file)

            self.subjects.clear()
            self.tasks.clear()

            for item in data["subjects"]:

                subject = Subject(
                    item["name"],
                    item["difficulty"],
                    item["exam_date"],
                    item["study_hours"]
                )

                subject.priority = item["priority"]

                self.subjects.append(subject)

            for item in data["tasks"]:

                task = StudyTask(
                    item["subject"],
                    item["title"],
                    item["hours"],
                    item["priority"]
                )

                task.status = item["status"]

                self.tasks.append(task)

            print("Data loaded successfully.")

        except Exception as error:
            print("Error loading data:", error)


# =========================================================
# MAIN PROGRAM
# =========================================================

def main():

    planner = AIStudyPlanner()

    # Automatically load previous data
    planner.load_data()

    while True:

        print("""
====================================================
        AI-BASED STUDENT STUDY PLANNER
====================================================

1. Add Subject
2. View Subjects
3. Delete Subject
4. Generate AI Study Plan
5. View Study Tasks
6. Complete Study Task
7. Get AI Recommendation
8. View Progress & Analytics
9. Save Data
10. Exit

====================================================
""")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            planner.add_subject()

        elif choice == "2":
            planner.view_subjects()

        elif choice == "3":
            planner.delete_subject()

        elif choice == "4":
            planner.generate_study_plan()

        elif choice == "5":
            print("\n========== STUDY TASKS ==========")
            planner.display_tasks()

        elif choice == "6":
            planner.complete_task()

        elif choice == "7":
            planner.recommend_next_task()

        elif choice == "8":
            planner.show_progress()

        elif choice == "9":
            planner.save_data()

        elif choice == "10":
            planner.save_data()
            print("\nThank you for using AI Study Planner!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
