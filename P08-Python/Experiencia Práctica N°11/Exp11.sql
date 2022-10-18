import sqlite3 

conn = sqlite3.connect(r'Experiencia11.db') 

print("Base de datos abierta satisfactoriamente"); 
cur = conn.cursor() 
cur.execute("SELECT * FROM orders;") 
one_result = cur.fetchone() 

print(one_result) 
print("Consulta  realizada satisfactoriamente"); 

conn.close() 