import React from 'react'
import './App.css';
import { Route } from 'react-router-dom'
import { Home, Todo } from 'component/index'

const App = () => {
  return (
    <div>
     <Route exact path='/' component={Home}/>
     <Route exact path='/todo' component={Todo}/>
    </div>
  );
}

export default App;

