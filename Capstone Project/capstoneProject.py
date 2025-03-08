# Python-Based Intelligent Study Planner

# Task Management System
def task_manager():
    tasks = []

    print("\n--- Task Management ---")
    while True:
        try:
            task_name = input("Enter task name (or type 'quit' to exit): ")
            if task_name.lower() == 'quit':
                break
            deadline = input("Enter task deadline (YYYY-MM-DD): ")
            priority = int(input("Enter task priority (1 = High, 2 = Medium, 3 = Low): "))
            
            if priority not in [1, 2, 3]:
                raise ValueError("Priority must be 1, 2, or 3.")
            
            # Append task as a dictionary with name, deadline, and priority
            tasks.append({"task": task_name, "deadline": deadline, "priority": priority})
        
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # Sorting tasks by priority (High = 1, Medium = 2, Low = 3) and deadline
    tasks_sorted = sorted(tasks, key=lambda x: (x["priority"], x["deadline"]))
    
    # Displaying sorted tasks with deadlines and priorities
    if tasks_sorted:
        print("\n--- Prioritized Task Schedule ---")
        for task in tasks_sorted:
            print(f"Task: {task['task']}, Deadline: {task['deadline']}, Priority: {task['priority']}")
    else:
        print("No tasks added.")

# Performance Tracking System with Actionable Feedback
def performance_tracking():
    scores = {}

    print("\n--- Performance Tracking ---")
    while True:
        try:
            subject = input("Enter subject name (or type 'quit' to exit): ")
            if subject.lower() == 'quit':
                break
            score = float(input(f"Enter your score for {subject}: "))
            
            if not (0 <= score <= 100):
                raise ValueError("Score must be between 0 and 100.")
            
            # Store the score for the subject
            scores[subject] = score
        
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # Calculate and display average score
    if scores:
        avg_score = sum(scores.values()) / len(scores)
        print("\n--- Performance Summary ---")
        for subject, score in scores.items():
            print(f"Subject: {subject}, Score: {score}")
        print(f"Average Score: {avg_score:.2f}")
        
        # Provide actionable feedback based on average score
        if avg_score >= 90:
            print("\nGreat job! You're performing excellently. Keep up the good work!")
        elif avg_score >= 75:
            print("\nYou're doing well, but there are areas where you could improve. Focus on subjects with lower scores.")
        else:
            print("\nIt looks like you're struggling. Consider revisiting your study plan and focusing on weaker subjects. Don't hesitate to ask for help.")

        # Provide subject-specific actionable feedback
        for subject, score in scores.items():
            if score < 70:
                print(f"\nIn {subject}, your score is below 70. Consider revisiting the basics and practicing problems in this subject.")
            elif score >= 70 and score < 80:
                print(f"\nIn {subject}, your score is average. Try reviewing key concepts and practicing more problems to improve.")
            elif score >= 80 and score < 90:
                print(f"\nIn {subject}, you're doing well! Continue reviewing and challenge yourself with more advanced material.")
            else:
                print(f"\nIn {subject}, excellent work! Keep it up and continue to push your limits for even better results.")

    else:
        print("No scores entered.")

# Main Application Loop
def main():
    while True:
        print("\n--- Study Planner ---")
        print("1. Manage Tasks")
        print("2. Track Performance")
        print("3. Quit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            task_manager()
        elif choice == '2':
            performance_tracking()
        elif choice == '3':
            print("Exiting Study Planner. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the Application
if __name__ == "__main__":
    main()
