import functions
import PySimpleGUI as sg

add_text=sg.Text("Enter a todo")
input_text=sg.InputText(tooltip="enter here", key="todo")
add_button=sg.Button("ADD")
edit_button=sg.Button("EDIT")
list_box=sg.Listbox(values=[functions.get_todos()],enable_events=True,
                    size=[45, 10])

window=sg.Window("todo application" , layout=[[add_text,input_text,add_button],[list_box, edit_button]],
                 font=('helvetica', 20))
while True:
    event,value=window.read()
    print(event)
    print(value)
    match event:
        case "ADD":
            todos=functions.get_todos()
            new_todos=value["todo"]+ '/n'
            todos.append(new_todos)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break



window.close()
