import PySimpleGUI as sg
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector as mc
from datetime import datetime

mydb = mc.connect(host = 'localhost',
                  database = 'project',
                  user = 'root',
                  password = 'root')
cursor = mydb.cursor(buffered=True)
cursor2 = mydb.cursor(buffered=True)


def graph():
    query = '''   SELECT BARCODE_NO, SUM(QTY) FROM customer
                                GROUP BY BARCODE_NO;'''
    cursor.execute(query)
    record = cursor.fetchall()
    df=pd.DataFrame(record, columns = ['Barcode_No','Qty'])
    print(df)

    query2 = ''' SELECT DISTINCT(Barcode_No), Item_Name FROM Stock_Inventory;'''
    cursor2.execute(query2)
    record2 = cursor2.fetchall()
    df2 = pd.DataFrame(record2, columns = ['Barcode_No', 'Item_Name'])
    print(df2)

    df['Item_Name'] = df2['Item_Name']
    print(df)

    item_name = df['Item_Name']
    qty = df['Qty']
    plt.bar(item_name, qty, width = 0.2)
    plt.xlabel('Item Name')
    plt.ylabel('Qty Purchased')
    plt.show()