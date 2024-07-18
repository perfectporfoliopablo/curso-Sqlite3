import sqlite3

con = sqlite3.connect('C:\\Programacion\\Data Analist\\company.db')

def mostrar_todo():
    cursor.execute('SELECT * FROM empleados')
    #print(cursor.fetchall()[1][1])
    print(cursor.fetchall())



cursor = con.cursor()  

mostrar_todo()