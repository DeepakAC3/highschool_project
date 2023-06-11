import PySimpleGUI as sg
import mysql.connector as mc
def signup():
    sg.theme("DarkAmber")
    col1=   [[sg.Text("TeacherCode")],
             [sg.Input("Code")],
             [sg.Text("TeacherName")],
             [sg.Input("Name")],
             [sg.Text("TeacherQualification")],
             [sg.Input("Qualification")],
             [sg.Text("Subject Handling")],
             [sg.Combo(["Maths","Physics","Chemistry","English"])],
             [sg.Text("Class")],
             [sg.Combo(["XI","XII"])],
             [sg.Text("Username")],
             [sg.Input("user ")],
             [sg.Text("Password")],
             [sg.Input("adminpass",password_char="*")],
             [sg.Button("create"),sg.Button("exit")]]
    layout=[[sg.Column(col1,background_color="black")]]
    window=sg.Window("Authentication",layout).finalize()
    event1,values1=window.read()
    window.close()
    return(event1,values1)
