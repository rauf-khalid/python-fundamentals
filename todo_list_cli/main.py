from storage import load_data, save_data
from task import show_tasks, show_task, toggle_done, make_task, is_valid_date, delete_task
from datetime import date

def is_valid_id(id_string):
    try:
        id = int(id_string)
        return id
    except ValueError:
        return None

def toggle_command(tasks, command):
    raw_value = command[6:].strip()

    try:
        id = int(raw_value)
        toggle_done(tasks, id)
    except ValueError:
        print("Please enter a valid ID.")
        return

def add_command(tasks, command):
    raw_value = command[3:].strip() 
    
    if not raw_value:
        title = input("Please provide a task title: ").strip()
        if not title:
            print("Title is not provided.")
            return
    else:
        title = raw_value

    due_date = input("Type due date in format: YYYY-MM-DD (Optional): ").strip()
    

    if is_valid_date(due_date):
        make_task(tasks, title, due_date)
        return
    else:                                     
        if not due_date:
            print("Due date is not provided.")
        else:
            print("Invalid due date provided. Please use YYYY-MM-DD format.")
    make_task(tasks, title, None)
    
def del_command(tasks, command):
    raw_value = command[3:].strip()

    if not raw_value:
        raw_value = input("Please enter the task ID: ").strip()
        if not raw_value:
            print("Task ID not provided. Try again.")
            return tasks
        
    task_id = is_valid_id(raw_value)

    if task_id is not None:
        return delete_task(tasks, task_id)
    else:
        print("Invalid ID provided.")
        return tasks
    
def show_command(tasks, command):
    raw_val = command[4:]

    if not raw_val:
        raw_val = input("Please enter the ID: ").strip()
        if not raw_val:
            print("Task ID is not provided. Try again.")
            return
        
    task_id = is_valid_id(raw_val)

    if task_id is not None:
        show_task(tasks, task_id)
    else:
        print("Invalid ID provided.")

def due_date_key(t):
    if t["due_date"] is None:
        return date.max
    return date.fromisoformat(t["due_date"])

def sort_command(tasks):
    raw_val = input("Sort tasks by (title, length, date): ").strip()

    if raw_val == "":
        raw_val = input("Provide the sorting style (title, length, date): ").strip()
        if raw_val == "":
            print("Try again. Style not provided.")
            return tasks
    
    sort_type = raw_val

    if sort_type == 'title':
        sorted_tasks =  sorted(tasks, key=lambda t: t["title"])
    elif sort_type == 'length':
        sorted_tasks = sorted(tasks, key=lambda t: len(t["title"]))
    elif sort_type == 'date':
        sorted_tasks = sorted(tasks, key=due_date_key)
    else:
        print(f"Unknown sort option: {sort_type}")
        return tasks
    
    print(f"Tasks are sorted by: {sort_type}")
    return sorted_tasks
    
def main():
    tasks = load_data()

    while True:
        try:
            command = input("> ").strip()
            if command == 'exit':
                save_data(tasks)
                print("Goodbye!")
                break
            elif command == "list":
                show_tasks(tasks)
            elif command.startswith("toggle"):
                toggle_command(tasks, command)
            elif command.startswith("add"):
                add_command(tasks, command)
            elif command.startswith("del"):
                tasks = del_command(tasks, command)
            elif command.startswith("show"):
                show_command(tasks, command)
            elif command == 'sort':
                tasks = sort_command(tasks)
            else:
                print("Commands: add <title>, list, show <id>, toggle <id>, del <id>, sort, exit")
        except KeyboardInterrupt:
            print("\nInterrupted. Saving and exiting")
            save_data(tasks)
            break

if __name__ == "__main__":
    main()