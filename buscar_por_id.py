import sqlite3

con = sqlite3.connect('C:\\Programacion\\Data Analist\\company.db')

def buscar_por_id(ident):
    cursor.execute(f'''SELECT * FROM empleados WHERE id='{ident}' ''')
    print(cursor.fetchone())




cursor = con.cursor()  
buscar_por_id(3)