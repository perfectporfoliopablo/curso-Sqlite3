import sqlite3

con = sqlite3.connect('C:\\Programacion\\Data Analist\\company.db')

def actualizar(ident,new_valor):
    cursor.execute(F'''UPDATE empleados SET departamento='{new_valor}' WHERE '{ident}' ''')
    con.commit()



cursor = con.cursor()  
actualizar(3,'ventas')