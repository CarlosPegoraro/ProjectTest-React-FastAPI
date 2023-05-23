import mysql.connector

def MySQLConnection():
    conexao = mysql.connector.connect(
        host="localhost", 
        port="3306",
        user="root",
        password="",
        database="testdb"
    )

    return conexao

def MySQLClose():
    
    conexao = MySQLConnection()
    cursor = conexao.cursor()
    
    cursor.close()
    conexao.close()