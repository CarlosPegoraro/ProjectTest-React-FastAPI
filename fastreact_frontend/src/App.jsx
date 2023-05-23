import axios from "axios";
import { useState, useEffect } from "react";
import "./App.css"

function App() {
    const [ username, setUsername ] = useState('')
    const [ saldo, setSaldo ] = useState('')
    
    let saldoColor = ""

    useEffect( () => {
        axios
            .get("http://localhost:7777/get_data")
            .then((response) => {
                const data = response.data
                setUsername(data['username'])
                setSaldo(data['saldo'])
            })
            .catch( (e) => {
                // Placeholder
            })
    }, [])

    if (saldo > 1500) {
        saldoColor = "saldo positive"
    } else if (saldo <= 1500 && saldo > 500) {
        saldoColor = "saldo neutral"
    } else {
        saldoColor = "saldo negative"
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
                    <i class="bi bi-person"></i>
                </p> 
            </header>
        </div>
    );
}

export default App;
