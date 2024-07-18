import sqlite3
con = sqlite3.connect('C:\\Programacion\\Data Analist\\company.db')

'''CREATE TABLE nombre_tabla(campos:tipo de datos)'''
'''CREATE TABLE IF NOT EXIST nombre_tabla(campos:tipos de dato)'''
''' INSERT INTO nombre_tabla(campos a llenar) VALUES (valores de los campos)'''

def insertar():
    nombre=input('Nombre: ')
    departamento = input('Departamentos: ')
    salario = int(input('Salario: '))
    datos=(nombre,departamento,salario)
    cursor.execute('INSERT INTO Empleados(nombre,departamento,salario) VALUES (?,?,?)',datos)
    con.commit()
cursor=con.cursor()
for i in range (5):
    insertar()