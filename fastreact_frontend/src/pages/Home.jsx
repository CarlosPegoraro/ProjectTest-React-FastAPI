import axios from "axios";
import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "../App.css"

export function Home() {
    const [username, setUsername] = useState('');
    const [saldo, setSaldo] = useState('');
    const [newUser, setNewUser] = useState('');
    const [newSaldo, setNewSaldo] = useState('');
    

    let saldoColor = "";

    useEffect(() => {
        axios
            .get("http://localhost:7777/")
            .then((response) => {
                const data = response.data;
                setUsername(data['username']);
                setSaldo(data['saldo']);
            })
            .catch((error) => {
                console.error(error);
            });
    }, []);

    const submitData = () => {
        const data = {
            name: newUser,
            saldo: newSaldo
        };

        axios
            .post("http://localhost:7777/", data)
            .then((response) => {
                console.log(response.data);
            })
            .catch((error) => {
                console.error(error);
            });
    };

    if (saldo > 1500) {
        saldoColor = "saldo positive";
    } else if (saldo <= 1500 && saldo > 500) {
        saldoColor = "saldo neutral";
    } else {
        saldoColor = "saldo negative";
    }

    return (
        <div>
            <header className="header">
                <div className="userData">
                    <p className="username">
                        {username}
                    </p>
                    <p className={saldoColor}>
                        R$ {saldo}
                    </p>
                </div>
                <p className="username">
                    <i className="bi bi-person"></i>
                </p>
            </header>
            <div>
                <input
                    type="text"
                    placeholder="New User"
                    value={newUser}
                    onChange={(e) => setNewUser(e.target.value)}
                />
                <input
                    type="text"
                    placeholder="New Saldo"
                    value={newSaldo}
                    onChange={(e) => setNewSaldo(e.target.value)}
                />
                <button onClick={submitData}>Submit Data</button>
            </div>
            <Link to="/">Deslogar</Link>
        </div>
    );
}
