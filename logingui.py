import PySimpleGUI as sg
import mysql.connector as mc
import mysql_table_connector

mydb = mc.connect(host ='localhost',database='project',user='root',password='root')
def login():
    sg.theme("Green")
    col1=   [[sg.Text("Username",background_color= sg.theme_background_color(),text_color= 'white')],[sg.Input("")],
             [sg.Text("Password",background_color= sg.theme_background_color(),text_color= 'white')],[sg.Input("")],
             [sg.Button("Log In"),sg.Button("Exit")]]

    layout=[[sg.Column(col1,background_color= sg.theme_background_color())]]
    window=sg.Window("Login",layout, keep_on_top = True, grab_anywhere = True, no_titlebar = True).finalize()
    
    event,values=window.read()
    print(event, values[0],values[1]) #here we havent specified keys in col1 so we use the default keys like in dataframe in pandas
    
    window.close()
    return(event,values)




