import functions
import PySimpleGUI as sg

label=sg.Text("Enter a todo")
input_text=sg.InputText(tooltip="Enter here", key="todo")
add_button=sg.Button("ADD")
edit_button=sg.Button("EDIT")
list_box=sg.Listbox(values=functions.get_todos(),key="todos", enable_events=True,
                    size=[45, 10])

window=sg.Window("todo application" ,
                 layout=[[label],[input_text,add_button],[list_box, edit_button]],
                 font=('helvetica', 20))
while True:
    event,value=window.read()
    print(event)
    print(value)
    match event:
        case "ADD":
            todos=functions.get_todos()
            new_todos=value["todo"]+ '\n'
            todos.append(new_todos)
            functions.write_todos(todos)
            window['todos'].update(values=todos)


        case "EDIT":
            todos_to_edited=value['todos'][0]
            print(todos_to_edited)
            new_todo=value['todo']


            todos=functions.get_todos()
            index=todos.index(todos_to_edited)
            todos[index]=new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value= value['todos'][0])
        case sg.WINDOW_CLOSED:
            break









window.close()
