FILEPATH= "todos.txt"

def get_todos(filepath1=FILEPATH):
    """
    read file in todos.txt and return the item
    """
    with open(filepath1, "r") as files:
        todos_local=files.readlines()
    return todos_local


def write_todos(todos_arg ,filepath1 =FILEPATH ):
    """ write the item in todos to text globexample"""
    with open(filepath1, "w") as files:
        files.writelines(todos_arg)
