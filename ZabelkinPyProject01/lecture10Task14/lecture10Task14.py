class Task:
    def __init__(self, title: str, description: str, completed: bool = False):
        self.title = title
        self.description = description
        self.completed = completed

    def toggleCompleted(self):
        self.completed = not self.completed

    def __str__(self):
        if self.completed:
            return f"[ok] {self.title}: {self.description}"
        else:
            return f"[ ] {self.title}: {self.description}"

class TaskList:
    def __init__(self):
        self.tasks = []


    def logActivity(func):
        def wrapper(*args):
            result = func(*args)
            if result == "task added":
                print(f"[LOG] Action: addTask, Task: {args[1].title}, Result: {result}")
            elif result == "task completed" or result == "task not completed":
                print(f"[LOG] Action: completeTaskByTitle, Task: {args[1]}, Result: {result}")
            return result
        return wrapper

    @logActivity
    def addTask(self, task):
        self.tasks.append(task)
        return "task added"

    @logActivity
    def completeTaskByTitle(self, taskName):
        taskName = taskName
        taskFound = False
        for i in range(len(self.tasks)):
            if taskName == self.tasks[i].title:
                taskFound = True
                self.tasks[i].completed = True
                break
            
        if taskFound:           
            return "task completed"
        else:
            return "task not completed"


    def __str__(self):
        self.complCounter = 0
        self.notComplCounter = 0
        self.allTasksStr = "\nTasks list:\n"

        for i in range(len(self.tasks)):
            self.allTasksStr += f"{self.tasks[i]}\n"
            if self.tasks[i].completed:
                self.complCounter += 1
            else:
                self.notComplCounter += 1

        self.allTasksStr += f"Total: {self.complCounter}/{self.complCounter + self.notComplCounter} completed"


        return self.allTasksStr


task1 = Task("First task", "Do exercises")
task2 = Task("Second task", "Brush your teeth")
task3 = Task("Third task", "Have breakfast")
task4 = Task("Fourth task", "Take a shower")
task5 = Task("Fifth task", "Go to work")

taskList = TaskList()

taskList.addTask(task1)
taskList.addTask(task2)
taskList.addTask(task3)
taskList.addTask(task4)
taskList.addTask(task5)

taskList.completeTaskByTitle("To do")

taskList.completeTaskByTitle("First task")
taskList.completeTaskByTitle("Second task")

print(taskList)