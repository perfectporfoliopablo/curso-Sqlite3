import sqlite3

con = sqlite3.connect('C:\\Programacion\\Data Analist\\company.db')

def buscar_por_departamento(nombre_depa):
    cursor.execute(f''' SELECT * FROM empleados WHERE departamento='{nombre_depa}' ''')
    print(cursor.fetchall())




cursor = con.cursor()  
buscar_por_departamento('ventas')