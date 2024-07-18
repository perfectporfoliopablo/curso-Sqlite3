import sqlite3

con = sqlite3.connect('C:\\Programacion\\Data Analist\\company.db')

def eliminar_registro(ident):
    cursor.execute(f'''DELETE FROM empleados WHERE id='{ident}' ''')
    con.commit()


cursor = con.cursor()  
eliminar_registro(2)