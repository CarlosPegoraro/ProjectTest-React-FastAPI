import mysql.connector

conexao = mysql.connector.connect(
    host="localhost", 
    port="3306",
    user="root",
    password="",
    database="testbd"
)

cursor = conexao.cursor()