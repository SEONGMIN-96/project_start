import React from 'react'
import { Route } from "react-router-dom"
import { Home } from './common/index'
import { Login, Signup, UserDetail, UserEdit, UserList } from './user/index'

const App = () => {
  return (<div>
    <Route exact path='/' component={ Home } />
    <Route exact path='/login' component={ Login } />
    <Route exact path='/signup' component={ Signup } />
    <Route exact path='/userlist' component={ UserList } />
    <Route exact path='/userdetail' component={ UserDetail } />
    <Route exact path='/useredit' component={ UserEdit } />
  </div>)
}

export default App