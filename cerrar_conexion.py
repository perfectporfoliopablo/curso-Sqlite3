import sqlite3

con = sqlite3.connect('C:\\Programacion\\Data Analist\\company.db')

cursor = con.cursor()  
cursor.close()
con.close()