import React from 'react'
import './App.css';
import { Route } from 'react-router-dom'
import { Home } from 'component/index'

const App = () => {
  return (
    <div>
     <Route exact path='/' component={Home}/>
    </div>
  );
}

export default App;

