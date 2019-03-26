import React, { Component } from 'react';
import { BrowserRouter as Router, Route} from 'react-router-dom';
import SignInForm from './pages/SignInForm';
import Menu from './pages/Menu';
import Add from './pages/Add'

import './App.css';

class App extends Component {
  render() {
    return (
      <Router basename="/">
        <Route exact path="/" component={SignInForm}>
        </Route>
        <Route path="/menu" component={Menu}></Route>
        <Route path="/add" component={Add}></Route>
      </Router>
    );
  }
}

export default App;
