#study tracker- menu, add,view,remove,exit,invalid

tasks = []

def add_task():
        name = input("Enter task: ")
        new_task = {
            "task" : name,
            "done" : False
        }
        
        tasks.append(new_task)

def view_tasks():
        for task in tasks:
            if task["done"] == False:
                print(task["task"])

def remove_task():
        y = input("Enter which task you want to remove: ")
        for task in tasks:
            if y== task["task"]:
                task["done"] = True
                print("Task marked as completed.")
                return
        print("Invalid task name") 

while True:
    menu = "1. Add Task\n2. View Tasks \n3. Mark Task as Completed \n4. Exit"
    print(menu)

    x = input("Enter what action you want to do? ")

    if x=="1":
        add_task()
    elif x=="2":
        view_tasks()
    elif x=="3":
        remove_task()
    elif x=="4":
        break
    else:
        print("Invalid input")