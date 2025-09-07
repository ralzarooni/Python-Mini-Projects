import json

# Function to read tasks from JSON file
def readTasks():
    with open('toDoList.json') as tasks:
        toDoList = json.load(tasks)
        tasks.close()
        return toDoList

# Function to write tasks to JSON file
def writeTasks(data, newData):
    with open('toDoList.json', 'w') as json_file:
        data.update(newData)
        json.dump(data, json_file, indent=4)

# Function to edit task in JSON file
def editTasks(data, index, name, status, category):
    data[index]['name'] = name
    data[index]['status'] = status
    data[index]['category'] = category
    writeTasks(data, data)

# Function to delete task in JSON file
def deleteTasks(data, index):
    data.pop(index)
    writeTasks(data, data)

# Function to verify user inputs
def inputCheck(text, maxNum):
    while True:
        try:
            userInp = int(input(f"{text}: "))
            if userInp >= 1 and userInp <= maxNum:
                return userInp
                break
            else:
                print(f"Please enter a number between 1 and {maxNum}.")
        except ValueError:
            print(f"Please enter a valid number between 1 and {maxNum}.")


# Function to find max task ID
def maxID(data):
    taskIDs = []
    for i in data:
        taskIDs.append(int(i))
    return max(taskIDs)


print("\033[95m\033[1mWelcome to the To-Do List CLI!\033[0m")
print("\033[94mPlease choose from the following functions:\033[0m\n")
print("\033[1m\033[96m1: Read Tasks\033[0m")
print("\033[1m\033[96m2: Write Tasks\033[0m")
print("\033[1m\033[93m3: Edit Task\033[0m")
print("\033[1m\033[91m4: Delete Task\033[0m")

choice = inputCheck('Your choice', 4)

# If the user chose to read
if choice == 1:
    tasks = readTasks()
    for i in tasks:
        print(f"\n\033[95m\033[1mTask {i}:\033[0m")
        print(f"\033[1mName: {tasks[i]['name']}")
        print(f"Status: {tasks[i]['status']}")
        print(f"Category: {tasks[i]['category']}\033[0m")

# If the user chose to write
elif choice == 2:
    print("\033[94m\033[1mPlease enter the following information:\033[0m")
    name = input("Please enter the name of the task: ")
    status = input("Please enter the current status of the task: ")
    category = input("Please enter the category of the task: ")

    data = readTasks()

    # To automatically assign the task ID
    number = maxID(data) + 1

    # Filling in the newly made data
    newData = {
        f"{number}":
        {
            "name": name,
            "status": status,
            "category": category
        }
    }
    writeTasks(data, newData)

# If the user chose to edit
elif choice == 3:
    data = readTasks()

    print("\033[94m\033[1mPlease enter the following information to edit a task:\033[0m")
    index = inputCheck('Please enter the ID of the task', maxID(data))
    name = input("Please enter the name of the task: ")
    status = input("Please enter the current status of the task: ")
    category = input("Please enter the category of the task: ")

    editTasks(data, str(index), name, status, category)

# If the user chose to delete
elif choice == 4:
    data = readTasks()
    print("\033[94m\033[1mPlease enter the following information to delete a task:\033[0m")
    index = inputCheck('Please enter the ID of the task', maxID(data))
    deleteTasks(data, str(index))