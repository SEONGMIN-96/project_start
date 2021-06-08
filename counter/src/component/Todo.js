import React, { useState } from 'react'

const Todo = () => {

    const [count, setCount ] = useState(0)

    return (<>
    <h1>Todo({count})</h1>
    <button onClick={ () => setCount( count + 1)}>일+</button>
    <button onClick={ () => setCount( count - 1)}>일-</button>
    </>)
}

export default Todo