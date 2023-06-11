import billinggui
import PySimpleGUI as sg
import mysql.connector as mc
from datetime import date,datetime
import csv

mydb = mc.connect(host = 'localhost',
                    database = 'project',
                    user = 'root',
                    password = 'root')
cursor = mydb.cursor()
date2 = []
#sample barcode = 1232342237968
sg.theme('Green')
billing_layout = [ [sg.Text('Date & Time of Billing: '),sg.Text(datetime.today())],
        [sg.Text('Enter Customer Details:')],
        [sg.Text('Enter Customer Name:'),sg.InputText(key='-CUST_NAME-',do_not_clear=True,size=(20,1)),sg.Text('Enter Customer Phone:'),sg.InputText(key='-CUST_PHONE-',size=(10,1),do_not_clear=True)],
        [sg.Text('Enter Customer Address: '),sg.InputText(key='-ADDRESS-',size=(50,1),do_not_clear=True)],
        [sg.Text('Barcode Number:'),sg.InputText(key='-BARCODE-',size=(20,1),do_not_clear=False),sg.Text('Qty: '),sg.InputText(key='-QTY-',size=(5,1),do_not_clear=False),sg.Button('Add Item to Bill')],
        [sg.Button('Admin'),sg.Button('Generate Bill'),sg.Button('Exit')]]
window = sg.Window('Input auto-clear', billing_layout)
while True:
    events, values = window.read()
    print(events,values)
    if events in (sg.WIN_CLOSED,'Exit'):
        break
    elif events == 'Add Item to Bill':
        print("Yes")
        date1 = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        print('check for dupe')
        billinggui.add_customer(values['-CUST_NAME-'],values['-CUST_PHONE-'],values['-BARCODE-'],values['-ADDRESS-'],values['-QTY-'],date1)
        print(values)
        billinggui.check_availability(values['-QTY-'],values['-BARCODE-'],date1)
        print(events, values)
        date2 = date2 + [str(date1)]
        print(date2)
    elif events == 'Generate Bill':
        print("Yes")
        print(date2)
        billinggui.bill_gen(date2[0],date2[-1],values['-CUST_NAME-'])
        date2 = []
    elif events == 'Admin':
        import login
window.close()