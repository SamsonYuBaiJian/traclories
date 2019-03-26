import React, { Component } from 'react';
import { BrowserRouter as Link, NavLink } from 'react-router-dom';

class SignInForm extends Component {
    constructor() {
        super();

        this.state = {
            email: '',
            password: ''
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(e) {
        let target = e.target;
        let value = target.type === 'checkbox' ? target.checked : target.value;
        let name = target.name;

        this.setState({
          [name]: value
        });
    }

    handleSubmit(e) {
        e.preventDefault();

        console.log('The form was submitted with the following data:');
        console.log(this.state);
        window.open('https://internet-banking.dbs.com.sg/ibAPL/Welcome', '_blank');
    }

    render() {
        return (
        <div className="App">

          <div className="App__Aside"><img src="https://totaleyecare.com.au/wp-content/uploads/2017/11/veg_lowres.jpg" style={{width: "100%",height:"100%"}}/>
</div>    

          <div className="App__Form">

                <div className="FormCenter">
                <div className="Big__Title">Traclories</div>
                    <form onSubmit={this.handleSubmit} onSubmit={this.handleSubmit}>
                    <div className="FormField">
                        <label className="FormField__Label" htmlFor="email">Email</label>
                        <input type="email" autocomplete="off" id="email" className="FormField__Input" name="email" value={this.state.email} onChange={this.handleChange} />
                      </div>

                      <div className="FormField">
                        <label className="FormField__Label" htmlFor="password">Password</label>
                        <input type="password" id="password" className="FormField__Input" name="password" value={this.state.password} onChange={this.handleChange} />
                      </div>

                      <div className="FormField">
                          <NavLink to="/menu" className="FormField"><button className="FormField__Button mr-20">Login</button></NavLink> 
                          <div className="Button__Gap"></div>
                          <button className="FormField__ButtonBottom mr-20">Get Started</button>
                      </div>
                      <div className="FormField__Bottom">
                        Forgot Email or Password
                        </div>
                        <div className="FormField__Bottom">
                        Frequently Asked Questions
                        </div>
                    </form>
                  </div>
            </div>
        </div>
        );
    }
}

export default SignInForm;
