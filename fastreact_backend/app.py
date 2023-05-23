import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import mysql.connector
from watchgod import run_process

conexao = mysql.connector.connect(
    host="127.0.0.1", 
    port="3306",
    user="root",
    password="",
    database="testdb"
)

cursor = conexao.cursor()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=["http://localhost:3000"]
)

def update_data():
    randomId = random.randint(1, 10)
    command = f"SELECT NAME FROM users WHERE ID={randomId}"
    cursor.execute(command)
    resultName = cursor.fetchone()
    command = f"SELECT SALDO FROM users WHERE ID={randomId}"
    cursor.execute(command)
    resultSaldo = cursor.fetchone()
    
    return resultName, resultSaldo

name, saldo = update_data()

@app.get('/get_data')
async def get_data():
    return {
        'username': name,
        'saldo': saldo
        }
    
def start_server():
    uvicorn.run(app, host='0.0.0.0', port=7777)

if __name__ == '__main__':
    run_process('.', start_server)
