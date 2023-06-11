import PySimpleGUI as sg
import pandas as pd
from datetime import date, datetime
import mysql.connector as mc
import csv
mydb = mc.connect(host = 'localhost',
                    database = 'project',
                    user = 'root',
                    password = 'root')

cursor = mydb.cursor(buffered=True)
cursor2 = mydb.cursor(buffered=True)
cursor3 = mydb.cursor(buffered=True)
cursor4 = mydb.cursor(buffered = True)

def add_customer(name,phone,barcode,address,qty,timestamp1):
    query = '''INSERT INTO Customer
                VALUES(%s,%s,%s,%s,%s,%s);'''
    cursor2.execute(query,(name,phone,barcode,address,qty,timestamp1))
    mydb.commit()


def check_availability(qty,Barcode,timestamp1):
    print(qty,Barcode,timestamp1)
    query = "SELECT si.Barcode_No,si.Item_Name, si.Price FROM Stock_Inventory si WHERE (si.BARCODE_No=%s)  AND (si.Qty >= %s) "
    cursor.execute(query,(Barcode,qty))
    record=cursor.fetchone()
    print(record)
    print(cursor.rowcount)
    if cursor.rowcount == 1:
        sg.popup('Products Available')
        query="UPDATE Stock_Inventory SET Qty=Qty-%s WHERE BARCODE_No=%s"
        cursor4.execute(query,(qty,Barcode))
        mydb.commit()
        print('Available')
    else:
        sg.popup('Products Out of stock')
        

def bill_gen(time_start,time_end,cust_name):
    print("Yes",time_start)
    print("No",time_end)
    print("customername",cust_name)     
    query1 = '''SELECT cu.BARCODE_NO , Item_Name, Price, cu.QTY FROM Customer cu, Stock_Inventory si
                WHERE ( cu.BARCODE_NO =si.Barcode_No )AND
                (DATE >= %s AND DATE <= %s) AND NAME = %s;'''
    cursor3.execute(query1,(time_start,time_end,cust_name))
    record = cursor3.fetchall()
    print(record)
    print(cursor3.column_names)
    df=pd.DataFrame(record,columns=list(cursor3.column_names))
    heading=list(df.columns)
    records=df.values.tolist()
    amt = df.Price * df.QTY
    amt = amt.values.tolist()
    amt1 = 0
    for i in amt:
        amt1 = amt1 + i
    print(amt1)
    print(heading)
    layout = [
        [sg.Table(values=records,
        headings=heading, 
        max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=10,
                    key='-TABLE-',
                    row_height=35)],
        [sg.Text('Amount payable :'),sg.Text(str(amt1))],
        [sg.Button('Save as CSV'),sg.Button('Exit')]
    ]
    window = sg.Window("Bill", layout,resizable=True)
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == 'Save as CSV':
            e_csv, val_csv = csv_window()
            if e_csv in ('Exit', sg.WIN_CLOSED):
                break
            elif e_csv == 'Save':
                csv_writer(heading, records, val_csv['-CSV_NAME-'])
    window.close()

def csv_window():
    csv_array = [[sg.Text('CSV Name:'),sg.InputText(key='-CSV_NAME-')],
                    [sg.Button('Save'),sg.Button('Exit')]]
    csv_window = sg.Window('CSV Window',csv_array)
    event, values = csv_window.read()
    return(event, values)

def csv_writer(heading, records,name):
    bill_array = records
    file = open(name+'.csv', 'w', encoding='UTF8')
    writer = csv.writer(file)
    writer.writerow(heading)
    writer.writerows(bill_array)
    file.close()5
