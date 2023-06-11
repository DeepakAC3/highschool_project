import logingui
import PySimpleGUI as sg
import mysql.connector as mc
import mysql_table_connector
mydb=mc.connect(host="localhost",
                database= "project",
                user="root",
                password="root")
cursor=mydb.cursor()
event,userInput=logingui.login()
print(userInput[0],userInput[1])
#userid=tuple(userInput.values())
if event=="Log In":
    cursor.execute("SELECT * FROM Admin WHERE UserID =%s and Password=%s",(userInput[0],userInput[1]))
    record = cursor.fetchall()
    if cursor.rowcount==1:
        sg.popup("Welcome " +userInput[0])
        import admin
    else:
        sg.popup("Invalid Credentials")
        