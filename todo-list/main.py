from functions import get_todos, write_todos
#todos = ["eat", "sleep", "walk", "bath"]
#print(dir(todos))
#print(type(todos))
#print(help(todos))
while True:
    user_action = input("type add, show, edit, complete or exit")
    user_action = user_action.strip().lower()
    #match user_action:
        #case "add":
    if user_action.startswith('add'):#'add' in user_action or 'new' in user_action:
        todos = get_todos('todos.txt')
        todo = user_action[4:]
        #todo = input("enter todo")
        todos.append(todo+'\n')

        #file = open("todos.txt", "w")
        #file.writelines(todos)#file.write("\n".join(todos))
        #file.close()
        #with open('todos.txt', 'w') as files:
        #    files.writelines(todos)
        write_todos('todos.txt', todos)
        print(f"{todo} has been added to todos list")
    elif user_action.startswith('show'):#'show' in user_action:
    #case "show":
        todos = get_todos('todos.txt')

        #new_todos = []
        #for item in todos:
        #    new_todos.append(item.strip('\n'))

        #new_todos = [item.strip('\n') for item in todos]

        for i, todo in enumerate(todos):
            todo = todo.strip('\n')
            row = f"{i+1}-{todo}"
            print(row)
            #print(i, '-', todo)
    elif user_action.startswith('edit'):#'edit' in user_action:
    #case "edit":
        try:
            number = int(user_action[5:])
            #number = int(input("enter number to edit element")) #str(10),float('10.0')

            todos = get_todos('todos.txt')

            word = input("enter word to edit element")
            if number <= len(todos):
                todos[number-1] = word + '\n'
                with open('todos.txt', 'w') as files:
                    files.writelines(todos)
            else:
                print('oops wrong length')
        except ValueError:
            print('oops wrong number to edit')
            continue
    elif user_action.startswith('complete'):#'complete' in user_action:
    #case "complete":
        try:
            number = int(user_action[9:])
            #number = int(input("enter number to complete"))

            todos = get_todos('todos.txt')

            index = number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            #with open('todos.txt', 'w') as files:
            #    files.writelines(todos)
            write_todos('todos.txt', todos)
            message = f"Todo {todo_to_remove} is completed."
            print(message)
        except IndexError:
            print('oops wrong number to compete')
            continue
    elif user_action.startswith('exit'):#'exit' in user_action:
    #case "exit":
        break
    else:
    #case "_":
        print("oops try again")

#print(dir(str))
