import mysql.connector as mc
import PySimpleGUI as sg
import pandas as pd

mydb = mc.connect(host = 'localhost',
                  database = 'project',
                  user = 'root',
                  password = 'root')
cursor = mydb.cursor(buffered=True)


def retrieve_stock():
    result = []
    query = 'SELECT * FROM Stock_Inventory'
    cursor.execute(query)
    for row in cursor:
        result.append(list(row))
    return result

def retrieve_employees():
    query2 = 'SELECT * FROM employee'
    cursor.execute(query2)
    record = cursor.fetchall()
    df = pd.DataFrame(record,columns=list(cursor.column_names))
    return df
