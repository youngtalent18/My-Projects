
class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"{status} {self.title}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self,title):
        task = Task(title)
        self.tasks.append(task)
        print(f"🥳{task.title} has been added to the list")


    def mark_done(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                if not task.completed:
                    task.completed = True
                    print(f"✅ {task.title} ")
                else:
                    task.completed = False
                    print(f"{task.title} not completed")


    def delete_task(self,title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                if not task.completed or task.completed:
                    self.tasks.remove(task)
                    print(f"🔫 {task.title} removed")
                else:
                    print(f"{task.title} not found ")



    def view_task(self):
        if not self.tasks:
            print("Your list is empty")
        else:
            print("-----Tasks------")
            for task in self.tasks:
                print(task)



def main():

    todo = ToDoList()

    while True:
        print('===Welcome To Your Task===')
        print("1) Add Task")
        print("2) Delete Task")
        print("3) Mark done")
        print("4) View Task")
        print("5) Exit To-Do-List")

        choice = input('Make a choice(1-5): ')

        if choice == '1':
            title = input("Enter the name of the task to add: ")
            todo.add_task(title)
        elif choice == '2':
            title = input("Enter the name of the task to delete ❌: ")
            todo.delete_task(title)
        elif choice == '3':
            title = input("Enter the title of the task to mark ✅:  ")
            todo.mark_done(title)
        elif choice == '4':
            todo.view_task()
        elif choice == '5':
            print("👋 Bye Stephen! Catch up with your tasks soon")
            break
        else:
            print("Invalid Selection")



if __name__ == '__main__':
     main()
