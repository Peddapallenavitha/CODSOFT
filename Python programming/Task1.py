import json

class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {'title': self.title, 'completed': self.completed}

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(Task(title))

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def update_task(self, old_title, new_title):
        for task in self.tasks:
            if task.title == old_title:
                task.title = new_title

    def mark_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.completed = True

    def view_tasks(self):
        for task in self.tasks:
            status = 'Completed' if task.completed else 'Pending'
            print(f"{task.title} - {status}")

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file)

    def load_tasks(self, filename):
        with open(filename, 'r') as file:
            task_dicts = json.load(file)
            self.tasks = [Task(**task) for task in task_dicts]

def main():
    todo_list = ToDoList()
    while True:
        command = input("Enter command (add, remove, update, view, complete, save, load, exit): ")
        if command == "add":
            title = input("Enter task title: ")
            todo_list.add_task(title)
        elif command == "remove":
            title = input("Enter task title to remove: ")
            todo_list.remove_task(title)
        elif command == "update":
            old_title = input("Enter current task title: ")
            new_title = input("Enter new task title: ")
            todo_list.update_task(old_title, new_title)
        elif command == "complete":
            title = input("Enter task title to mark as complete: ")
            todo_list.mark_complete(title)
        elif command == "view":
            todo_list.view_tasks()
        elif command == "save":
            filename = input("Enter filename to save tasks: ")
            todo_list.save_tasks(filename)
        elif command == "load":
            filename = input("Enter filename to load tasks from: ")
            todo_list.load_tasks(filename)
        elif command == "exit":
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
