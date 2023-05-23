import axios from "axios";
import React from "react";
import { useState, useEffect } from "react";
import { Link } from "react-router-dom";

export function Login() {
    let [login, setLogin] = useState('');

    const loginData = () => {
        if (login == null) {
            login = "1"
        }
        const data = {
            key: login
        };
        axios
            .post("http://localhost:7777/login", data)
            .then((response) => {
                console.log(response.data);
            })
            .catch((error) => {
                console.error(error);
            });
    };

    return (
        <div>
            <input
                type="text"
                placeholder="Chave"
                value={login}
                onChange={(e) => setLogin(e.target.value)}
            />
            <button onClick={loginData}>
                <Link to="/home">Logar</Link>
                </button>
        </div>
    )
} 