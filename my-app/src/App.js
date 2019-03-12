import React, { Component } from 'react';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      fullname: "",
      emailaddress: "",
      password: "",
      eateryname: "",
      cuisine: "",
      terms: false,
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    const target = event.target;
    const value = target.type === "checkbox" ? target.checked : target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }

  handleSubmit(event) {
    event.preventDefault();
    console.log(this.state);
  }

  render() {
    return (
      <div className="App">
        <header>
          <div className="container">
            <nav className="navbar">
              <div className="navbar-brand">
                <span className="navbar-item">Vendor Signup Form</span>
              </div>
            </nav>
          </div>
        </header>
        <div className="container">
          <div className="columns">
            <div className="column is-9">
              <form className="form" onSubmit={this.handleSubmit}>
                <div className="field">
                  <label className="label">Full Name</label>
                  <div className="control">
                    <input
                      className="input"
                      type="text"
                      name="fullname"
                      value={this.state.fullname}
                      onChange={this.handleChange}
                    />
                  </div>
                </div>

                <div className="field">
                  <label className="label">Email Address</label>
                  <div className="control">
                    <input
                      className="input"
                      type="email"
                      name="emailaddress"
                      value={this.state.emailaddress}
                      onChange={this.handleChange}
                    />
                  </div>
                </div>

                <div className="field">
                  <label className="label">Password</label>
                  <div className="control">
                    <input
                      className="input"
                      type="password"
                      name="password"
                      value={this.state.password}
                      onChange={this.handleChange}
                    />
                  </div>
                </div>

                <div className="field">
                  <label className="label">Name of Eatery</label>
                  <div className="control">
                    <input
                      className="input"
                      type="text"
                      name="eateryname"
                      value={this.state.eateryname}
                      onChange={this.handleChange}
                    />
                  </div>
                </div>

                <div className="field">
                  <label className="label">Pick your Cuisine</label>
                  <div className="control">
                    <div className="select">
                      <select
                        value={this.state.cuisine}
                        name="cuisine"
                        onChange={this.handleChange}
                      >
                        <option value="japanese">Japanese</option>
                        <option value="western">Western</option>
                      </select>
                    </div>
                  </div>
                </div>

                <div className="field">
                  <div className="control">
                    <label className="checkbox">
                      <input
                        name="terms"
                        type="checkbox"
                        checked={this.state.terms}
                        onChange={this.handleChange}
                      />
                      I agree to the{" "}
                      <a href="https://google.com">terms and conditions</a>
                    </label>
                  </div>
                </div>

                <div className="field">
                  <div className="control">
                    <input
                      type="submit"
                      value="Submit"
                      className="button is-primary"
                    />
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
