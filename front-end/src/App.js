import React, { Component } from 'react';
import { BrowserRouter as Router, Route} from 'react-router-dom';
import SignUpForm from './pages/SignUpForm';
import SignInForm from './pages/SignInForm';
import Menu from './pages/Menu';
import Add from './pages/Add'

import './App.css';

class App extends Component {
  render() {
    return (
      <Router basename="/">
        <Route exact path="/" component={SignUpForm}>
        </Route>
        <Route path="/sign-in" component={SignInForm}>
        </Route>
        <Route path="/menu" component={Menu}></Route>
        <Route path="/add-items" component={Add}></Route>
      </Router>
    );
  }
}

export default App;
