from datetime import date

def next_id(tasks):
    if not tasks:
        return 1
    return max(t["id"] for t in tasks) + 1

def is_valid_date(date_string):
    try:
        date.fromisoformat(date_string)
        return True
    except ValueError:
        return False
    
def make_task(tasks, title, due_date = None, done = False):
    id = next_id(tasks)
    task = {"id": id,"title": title, "done": done, "due_date": due_date}
    tasks.append(task)
    print(f"Task added: {title}")
    return tasks

def get_task(tasks, task_id):
    if tasks is None:
        raise TypeError("Tasks is not iterable.")
    for t in tasks:
        if t["id"] == task_id:
            return t
    return None

def toggle_done(tasks, task_id):
    t = get_task(tasks, task_id)
    if t is not None:
        t["done"] = not t["done"]
        print(f"Task {task_id} is marked as {t["done"]}")
    else:
        print(f"Task {task_id} is not found.")
    return tasks

def show_task(tasks, task_id):
    t = get_task(tasks, task_id)
    if t is not None:
        status = "[✓]" if t['done'] else "[ ]"
        print(f"{t["id"]}. {status} {t["title"]} (Due Date: {t["due_date"]})")
        return
    print(f"Task {task_id} not found. Try again.")

def show_tasks(tasks):
    if tasks == []:
        print("Empty list found. Add tasks to show.")
    for t in tasks:
        try:
            status = "[✓]" if t['done'] else "[ ]"
            print(f"{t["id"]}. {status} {t["title"]} (Due Date: {t["due_date"]})")
        except (KeyError):
            print(f"Invalid task: {t}")

def delete_task(tasks, task_id):
    t = get_task(tasks, task_id)
    
    if t is not None:
        updated_tasks = [t for t in tasks if t["id"] != task_id]
        print(f"Task {task_id} is deleted successfully.")
        return updated_tasks
    else:
        print(f"Task {task_id} not found. Try again.")
        return tasks