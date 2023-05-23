import random
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from connection import MySQLConnection, MySQLClose
from watchgod import run_process
from typing import Optional

# Database connect
conexao = MySQLConnection()

cursor = conexao.cursor()

# Variáveis globais para armazenar os dados
username = None
saldo = None

#  FastAPI connection
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    expose_headers=["*"],
    allow_origins=["http://localhost:3000"],
)

#  Data insert

@app.post("/")
async def post_data(request: Request):
    body = await request.json()
    name = body.get("name")
    saldo = body.get("saldo")
    if not name and not saldo:
        return {"message": "Erro ao inserir dados"}
    
    command = "INSERT INTO users (NAME, SALDO) VALUES (%s, %s)"
    
    cursor.execute(command, (name, saldo))
    conexao.commit()

# Data update

def update_data(key):
    command = f"SELECT NAME FROM users WHERE ID={key}"
    cursor.execute(command)
    resultName = cursor.fetchone()
    command = f"SELECT SALDO FROM users WHERE ID={key}"
    cursor.execute(command)
    resultSaldo = cursor.fetchone()
    return resultName, resultSaldo

@app.post("/login")
async def login_data(request: Request):
    login = await request.json()
    
    key = int(login.get("key"))
    
    if not key:
        return {"message": "Erro de chave"}
    
    dbName, dbSaldo = update_data(key)
    
    global username, saldo
    username = dbName
    saldo = dbSaldo

# Função para retornar os dados atualizados
@app.get('/')
async def get_data():
    return {
        'username': username,
        'saldo': saldo
    }
    
# Backend server start

def start_server():
    uvicorn.run(app, host='localhost', port=7777)

if __name__ == '__main__':
    run_process('.', start_server)
    
MySQLClose()
