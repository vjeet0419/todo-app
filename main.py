#from functions import get_todos,write_todos
import functions
import time

time_format = time.strftime("%a,%d-%m-%Y %H:%M:%S")
print("hi time is below")
print(f"Hi today date and time is:-{time_format}")



while True:

    USER_CHOICE = input("type add,show,edit,completed or exit")
    USER_CHOICE=USER_CHOICE.strip()


    if USER_CHOICE.startswith("add"):
        todo=USER_CHOICE[4:]


        todos=functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)


    elif USER_CHOICE.startswith("show"):
        todos=functions.get_todos()

        for index, item in enumerate(todos):
            item=item.strip('\n')
            row=f"{index+1}-{item}"
            print(row)

    elif USER_CHOICE.startswith("edit"):
        try:
            number=int(USER_CHOICE[5:])

            number=number-1

            todos=functions.get_todos()


            newtodo=input("enter the edit")
            todos[number]=newtodo+"\n"
            functions.write_todos(todos)



        except ValueError:
            print("enter a numeric (like 1, 2,3) you entered a wrong command  ")
            continue


    elif USER_CHOICE.startswith("completed"):
        try:
            number =int(USER_CHOICE[9:])
            number=number-1

            todos=functions.get_todos()


            todos.pop(number)

            functions.write_todos(todos)
        except ValueError:
             print("this is wrong enter a numeric")
        except IndexError:
             print("this is out of range")
        continue


    elif "exit" in USER_CHOICE:
        break
    else:
        print("command not found ")



print("bye come back soon")
print("choice not found")