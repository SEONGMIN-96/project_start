import React, { useState } from 'react'
import './home.css'

const Home = () => {
    
    const [ number, setNumber ] = useState(0)
    
    const addClick = () => {
        setNumber (number + 1)
    }
    const subClcik = () => {
        setNumber (number - 1)
    }
    return (<>
    <h1> {number} </h1>
    <button onClick={addClick}>+</button>
    <button onClick={subClcik}>-</button>
    
    </>)
}

export default Home