def get_todos(filename):
    # file = open("todos.txt", "r")
    # todos = file.readlines()#read().splitlines()
    # file.close()
    with open(filename, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(filename, todos_arg):
    with open(filename, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Welcome to the Todos App")
