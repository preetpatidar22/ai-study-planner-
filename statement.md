Project Statement

Project Title

AI-Based Student Study Planner

Problem Statement

Students often face difficulty managing multiple subjects, different examination dates, varying subject difficulties, and limited study time. Manually deciding which subject to study first can result in poor time management and an unbalanced study schedule.

The purpose of this project is to develop an intelligent study-planning system that helps students organize their academic workload and automatically create a priority-based study plan.

Proposed Solution

The AI-Based Student Study Planner is a Python application that collects information such as:

- Subject name
- Subject difficulty
- Examination date
- Available study hours

The system analyzes these inputs using a rule-based AI approach. It calculates a priority score based on subject difficulty and examination urgency. Subjects with higher priority are scheduled earlier, and the available study hours are divided into manageable study sessions.

The system also recommends the next pending study task and tracks completed sessions to calculate the student's overall progress.

Main Objectives

1. Develop a simple and effective student study-planning application.
2. Automatically prioritize subjects based on difficulty and exam urgency.
3. Generate personalized study sessions.
4. Recommend the next important study task.
5. Track completed study sessions.
6. Calculate study progress and completed study hours.
7. Store and retrieve student data using JSON file handling.
8. Demonstrate the practical use of Python and rule-based artificial intelligence.

Core Features

- Subject management
- Difficulty-based prioritization
- Examination-urgency analysis
- Automatic study-plan generation
- Study-task management
- AI-based next-task recommendation
- Progress and analytics
- JSON data storage
- Input validation and error handling

AI Approach

The project uses an explainable rule-based AI approach.

The priority score is calculated using:

Priority Score = (Difficulty × 10) + (30 ÷ Days Remaining)

The calculated priority is used to sort subjects and determine which study tasks should receive attention first.

Technologies Used

- Python 3
- Object-Oriented Programming
- Lists and Dictionaries
- Sorting
- "datetime" module
- JSON file handling
- Exception handling
- Rule-based Artificial Intelligence

Expected Outcome

The completed system should allow a student to enter academic information and receive an automatically generated study plan. The student should also be able to track completed sessions, receive recommendations, and monitor overall study progress.

Future Scope

The project can be further enhanced by adding:

- Machine-learning-based recommendations
- Graphical User Interface
- Web or mobile application
- Daily notifications and reminders
- Calendar integration
- Performance prediction
- Study-time prediction
- Multiple student accounts
- Cloud database
- Personalized learning analytics

Conclusion

The AI-Based Student Study Planner provides a practical solution for student time management by combining Python programming, object-oriented design, data structures, file handling, and rule-based artificial intelligence. The project provides a foundation for developing a more advanced intelligent academic assistant in the future.
