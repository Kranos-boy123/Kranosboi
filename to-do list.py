task = []
#define the menu
def menu():
    print("""
1. Add a task
2. View task
3. Remove a task
4. Exit
          """)

#define to add a task
def add_task():
    user = input("Enter your task: ")
    if user:
        task.append(user)
        print(f"task '{user}' added")
    else:
        print("Task cannot be empty")

# define to view a task
def view():
    if len(task) == 0:
        print("You have no task to view here...")
    else:
        print(f"\nYour task:")
        for i, r in enumerate(task, 1):
            print(f"{i}. {r}")

# define to remove a specfic task
def remove():
    if len(task) == 0:
        print("You have no task to remove here...")
    else:
        view()
        remo = int(input("Enter what task you want to remove: "))
        if 1 <= remo <= len(task):
            wow = task.pop(remo - 1)
            print(f"Task '{wow}' removed!!")
        else:
            print("Invalid task number")

#define to selcet an option
def option():
    menu()
    while True:
        opt = int(input("Enter options: "))
        if opt == 1:
            add_task()
        elif opt == 2:
            view()
        elif opt == 3:
            remove()
        else:
            print("Invalid option")

# run the program
option()
    
    
