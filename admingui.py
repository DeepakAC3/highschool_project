import PySimpleGUI as sg
import mysql.connector as mc
import mysql_table_connector
mydb=mc.connect(host="localhost",
                database= "project",
                user="root",
                password="root")

cursor = mydb.cursor(buffered=True)

def emp_edit():
    layout = [
        [sg.Text('Operations with employee table(sql)')],
        [sg.Button('Insert'),sg.Button('View'),sg.Button('Delete')],
        [sg.Button('Exit')]
    ]
    window = sg.Window('Edit Employee Table',layout)
    event, values = window.read()
    window.close()
    return(event,values)




def emp_view():
    result = mysql_table_connector.retrieve_employees()
    layout = [
        [sg.Table(values=result, headings= ['empno','name','job','hiredate','phone','salary','bonus'],
                   auto_size_columns=True,display_row_numbers=True, justification='right',max_col_width=30)],
        [sg.Button('Exit')]
    ]
    emp_view_window = sg.Window('Employee Table',layout)
    event, values = emp_view_window.read()
    emp_view_window.close()
    return(event,values)
    





def emp_insert():
    admin_insert_layout = [
        [sg.Text('Enter EmployeeID:')],    [sg.Input(key='-EMPID-')], #1
        [sg.Text('Enter Employee Name:')], [sg.Input(key='-EMPNAME-')], #2
        [sg.Text('Enter Job:')],           [sg.Input(key='-JOB-')],      #3
        [sg.Text('Enter Hire Date:')],     [sg.Input(key='-HIRE_DATE-')], #4
        [sg.Text('Enter Phone No.')],      [sg.Input(key='-PHONE-')],    #5
        [sg.Text('Enter Salary')],         [sg.Input(key='-SALARY-')],    #6
        [sg.Text('Bonus:')],               [sg.Input(key='-BONUS-')],    #7
        [sg.Button('Insert'),sg.Button('Exit')]
    ]
    window=sg.Window('Insert New Admin',admin_insert_layout)
    event, values = window.read()
    while True:
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Insert':
            query = '''
                       INSERT INTO employee VALUES
                        (%s,%s,%s,%s,%s,%s,%s);'''
            cursor.execute(query,(values['-EMPID-'],values['-EMPNAME-'],values['-JOB-'],values['-HIRE_DATE-'],values['-PHONE-'],values['-SALARY-'],values['-BONUS-']))
            mydb.commit()
    window.close()
    return(event,values)


def emp_delete():
    admin_delete_layout = [
        [sg.Text('EmployeeID:')],
        [sg.Input(key='-EMPID-')],
        [sg.Button('Delete'),sg.Button('Exit')]
        ]
    window = sg.Window('Delete Admin',admin_delete_layout)
    event, values = window.read()
    while True:
        if event in (sg.WIN_CLOSED,'Exit'):
            break
        elif event == 'Delete':
            cursor.execute('''DELETE FROM employee
                              WHERE EMPID = %s ;''',(values['-EMPID-']))
            mydb.commit()
    window.close()
    return(event, values)


def create_stock_table():
    stock_inventory_layout = [
        [sg.Table(mysql_table_connector.retrieve_stock(),headings=['Barcode_No','Item_Name','Price','Qty'],  auto_size_columns=True, max_col_width=35,
                   display_row_numbers=True,
                   justification='right',
                   num_rows=10,
                   key='-TABLE-',
                   row_height=35,
                   tooltip='Stock Inventory')],
        [sg.Button('Add New Products'),sg.Button('Modify Existing Stock'),sg.Button('Exit')]
    ]
    stock_inventory_window = sg.Window('Stock Inventory',stock_inventory_layout)
    event1, values1 = stock_inventory_window.read()
    stock_inventory_window.close()
    return(event1,values1)



def view_stock_table():
    stock_inventory_layout = [
        [sg.Table(mysql_table_connector.retrieve_stock(),headings=['Barcode_No','Item_Name','Price','Qty'],  auto_size_columns=True, max_col_width=35,
         display_row_numbers=True,
         justification='right',
         num_rows=10,
         key='-TABLE-',
         row_height=35,
         tooltip='Stock Inventory')],[sg.Button('Exit')]]
    stock_inventory_window = sg.Window('Stock Inventory',stock_inventory_layout)
    event_view, values_view = stock_inventory_window.read()
    stock_inventory_window.close()
    return(event_view, values_view)

def add_new():
    add_new_layout = [
        [sg.Text('Barcode No. :'), sg.Input(key='-BARCODE-')],
        [sg.Text('Item Name:'),sg.Input(key='-ITEM_NAME-')],
        [sg.Text('Price:'),sg.Input(key='-PRICE-')],
        [sg.Text('Qty:'),sg.Input(key='-QTY-')],
        [sg.Button('Insert'),sg.Button('Exit'),sg.Button('View Stock Inventory')]
    ]
    add_new_window = sg.Window('Add New Products',add_new_layout)
    while True:
        event_add, values_add = add_new_window.read()
        if event_add in (sg.WIN_CLOSED, "Exit"):
            break
        elif event_add == 'Insert':
            query = '''INSERT INTO Stock_Inventory VALUES(
                    %s,%s,%s,%s);'''
            cursor.execute(query,(values_add['-BARCODE-'],values_add['-ITEM_NAME-'],values_add['-PRICE-'],values_add['-QTY-']))
            mydb.commit()
        elif event_add == 'View Stock Inventory':
            view_stock_table()
        print('bruh')
    add_new_window.close()

def remove_stock():
    delete_layout = [
        [sg.Text('Barcode No. :'),sg.Input(key='-BARCODE-')],
        [sg.Text('Qty :'),sg.Input(key='-QTY-')],
        [sg.Button('Remove'),sg.Button('Exit'),sg.Button('Delete (Deletes Product From the Table)')]
    ]
    delete_window = sg.Window('Remove Stock',delete_layout)
    event_delete, values_delete = delete_window.read()
    while True:
        if event_delete in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event_delete == 'Remove':
            query = ''' 
                        UPDATE Stock_Inventory SET QTY = QTY - %i
                        WHERE Barcode_No = %s;
                        '''
            cursor.execute(query,(values_delete['-QTY-'],values_delete['-BARCODE-']))
            mydb.commit()
        elif event_delete == 'Delete':
            query = '''
                       DELETE FROM Stock_Inventory
                       WHERE Barcode_No = %s'''
            cursor.execute(query,values_delete['-BARCODE-'])
            mydb.commit()
    delete_window.close()