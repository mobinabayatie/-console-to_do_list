def main():
    tasks = []

    def addtask():
        task = input("please enter your task:")
        tasks.append(task)
        print(F"task''{task} ''added to thee list")

    def listTask():
        if not tasks:
            print("there is no tasks currently.")

        else:
            print("current tasks:")
            for index, task in enumerate(tasks):
                print(f"task #{index}. {task}")

    def deletetask():
        listTask()
        try:
            taskToDelete = int(input("choose the number of the task that you want to delete:"))
            if taskToDelete >= 0 and taskToDelete > len(tasks):
                tasks.pop(taskToDelete)
                print(f"task{taskToDelete} has been deleted")
            else:
                print(f"task{taskToDelete} was not found")
        except:
            print("invalid input.")

    print("\n===== To-Do List =====")
    while True:
        print("please enter one of the following options")
        print("-----------------------------------------")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        print("5.delete a task")

        choice = input("what do you want to do dear user? ")

        if (choice == "1"):
            #  print()
            #  n_tasks = int(input("How may task you want to add: "))
            #  for i in range(n_tasks):
            #     task = input("Enter the task: ")
            #     tasks.append({"task": task, "done": False})
            #     print("Task added!")
            addtask()


        elif choice == '2':
            # print("\nTasks:")
            # for index, task in enumerate(tasks):
            #     status = "Done" if task["done"] else "Not Done"
            #     print(f"{index + 1}. {task['task']} - {status}")
            listTask()


        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")


        elif choice == '4':
            print("Exiting the To-Do List.")
            break

        elif choice == "5":
            deletetask()

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()