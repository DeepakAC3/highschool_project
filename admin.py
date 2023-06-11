import PySimpleGUI as sg
import mysql.connector as mc
import mysql_table_connector
import admingui
import data_visualisation

admin_layout = [
        [sg.Text('Welcome ')],
        [sg.Button('View Stock Inventory'),sg.Button('View Employees'),sg.Button('Graph')],
        [sg.Button('Exit')]
    ]
window = sg.Window('Admin Screen',layout=admin_layout)
event, values = window.read()

while True:
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'View Stock Inventory':
        event_create, values_create = admingui.create_stock_table()
        if event_create in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event_create == 'Add New Products':
            admingui.add_new()
        elif event_create == 'Modify Existing Stock':
            admingui.remove_stock()
    elif event == 'View Employees':
        event1, values1 = admingui.emp_edit()
        if event1 in (sg.WIN_CLOSED , 'Exit'):
            break
        elif event1 == 'Insert':
            admingui.emp_insert()
        elif event1 == 'View':
            e_view, v_view = admingui.emp_view()
            if e_view in (sg.WIN_CLOSED, 'Exit'):
                break
        elif event1 == 'Delete':
            admingui.emp_delete()
    elif event == 'Graph':
        data_visualisation.graph()
        sg.popup('Run Program Again from first to continue')
        break