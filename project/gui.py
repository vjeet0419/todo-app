import PySimpleGUI as sg

add_text=sg.Text("enter a todo")
input_text=sg.InputText(tooltip="enter here")
add_button=sg.Button("ADD")

window=sg.Window("todo application" , layout=[[add_text,input_text,add_button]])
window.read()
window.close()
