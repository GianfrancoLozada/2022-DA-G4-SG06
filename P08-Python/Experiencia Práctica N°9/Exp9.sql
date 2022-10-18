import sqlite3 
conn = sqlite3.connect(r'Experiencia9.db') 
print("Base de datos abierta satisfactoriamente"); 
cur = conn.cursor() 
cur.execute("""CREATE TABLE ejemplo1""") 
cur.execute("""CREATE TABLE IF NOT EXISTS users(userid INT PRIMARY KEY,fname TEXT,lname TEXT,gender TEXT);""") 
conn.commit() 
cur.execute("""CREATE TABLE IF NOT EXISTS orders(orderid INT PRIMARY KEY,date TEXT,userid TEXT,total TEXT);""") 
conn.commit() 