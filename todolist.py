from datetime import datetime

todo = []
status = ['todo', 'inprogress', 'done']
date = datetime.now()

def add_task(task):
    task = input("Enter a task: ")
    todo.append({'id': len(todo) + 1, 'task': task, 'status': 'todo', 'created_at': date.strftime("%Y-%m-%d %H:%M:%S")})
    return f"Task '{task}' added to the list."

def view_tasks():
    if not todo:
        return "No tasks in the list."
    task_list = ""
    for index, task in enumerate(todo):
        task_list += f"{index + 1}. {task['task']} - {task['status']} created at {task['created_at']}\n"
    return task_list.strip()

while True:
    choice = float(input("this is a todo list app \n1. add a task \n2. view tasks \n3. exit \nChoose an option: "))
    if choice == 1:
        print(add_task(todo))
    elif choice == 2:
        print(view_tasks())
    elif choice == 3:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

