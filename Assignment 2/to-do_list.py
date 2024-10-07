#Creating the to-do list
todo_list =[]

#Defining the function that adds a task to the list
def add_task(task):
    todo_list.append(task)

#Defining the function that'll show the tasks
def show_tasks(list):
    for element in list:
        print(element)

show_tasks(todo_list)