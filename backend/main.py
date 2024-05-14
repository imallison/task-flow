from flask import Flask, jsonify
from task_scheduler import TaskScheduler

app = Flask(__name__)

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = TaskScheduler.displayList()  # Assume this returns a list of tasks
    return jsonify(tasks)

# from task_scheduler import TaskScheduler

# def main():
#     tasks = TaskScheduler()

#     while True:
#         print("\nTask Flow")
#         print("1. Add task")
#         print("2. Display task list")
#         print("3. Exit")

#         option = input("Enter an option: ")

#         if option == "1":
#             taskName = input("Enter a task: ")
#             priority = int(input("Enter task priority number (1-10): "))
#             time = float(input("Enter estimated time (hours): "))
#             tasks.addTask(taskName)
#             print("Task added.")

#         elif option == "2":
#             print("\nCurrent tasks:")
#             tasks.displayList()
        
#         elif option == "3":
#             print("Exiting.")
#             break

#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()