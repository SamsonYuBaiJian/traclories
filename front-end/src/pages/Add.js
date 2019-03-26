import React, { Component } from 'react';
import { BrowserRouter as Link, NavLink, Redirect } from 'react-router-dom';
import axios from 'axios';

class Add extends Component {

    constructor() {
        super();
        this.state ={
            name: '',
            image: '',
            calories: '',
            price: '',
            submit: 'Submit'
        }


        this.handleChangeName = this.handleChangeName.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChangePrice = this.handleChangePrice.bind(this);
        this.handleChangeImage = this.handleChangeImage.bind(this);
    }

    handleChangeImage(e) {
        e.preventDefault();

        this.setState({
          image: "http://www.springtomorrow.com/wp-content/uploads/2013/11/img_6039.jpg"
        });
    }

    handleChangeName(e) {
        this.setState({
          name: e.target.value
        });

        axios.post('http://127.0.0.1:5000/calculate', {
            name: e.target.value,
        })
            .then(res => {
                console.log(res.data);
                this.setState({
                    calories: res.data
                });
            });

    }

    handleChangePrice(e) {
        e.preventDefault();

        this.setState({
          price: e.target.value
        });
    }

    handleSubmit(e) {
        e.preventDefault();

        axios.post('http://127.0.0.1:5000/update_menu', {
            name: this.state.name,
            image: "http://www.springtomorrow.com/wp-content/uploads/2013/11/img_6039.jpg",
            calories: this.state.calories,
            price: this.state.price
        })
            .then(res => {
                console.log(res);
            });

        this.setState({
        	submit: 'Submitted!'
        });

        setTimeout(() => {
            this.setState({
            submit: 'Submit New Item?'
          })
        }, 1500);
    }


    render() {

        return (
        <div className="App">
          <div className="App__Aside"><img src="https://www.azamaraclubcruises.com/sites/default/files/heros/med-food-hero.jpg" style={{width: "100%",height:"100%"}}/>
          </div>

          <div className="Menu__Title">Traclories</div>

          <div className="App__FormTop">
              <div className="FormTitle">
                  <NavLink to="/menu" activeClassName="FormTitle__Link--Active" className="FormTitle__Link">Menu</NavLink>
                  <NavLink exact to="/add" activeClassName="FormTitle__Link--Active" className="FormTitle__Link">Add Items</NavLink>
                  <NavLink exact to="/" activeClassName="FormTitle__Link--Active" className="FormTitle__Link">Logout</NavLink>
              </div>
              <div className="Store__Name">
              Changi Chicken Rice
              </div>
          </div>
          <div className="App__FormBottom">

              <div className="FormFieldMin">
              <label className="FormField__LabelMenu" htmlFor="photo">Upload Photo</label>
              <div className="Gap"></div>

              <input type="file" id="image" name="image" onChange={this.handleChangeImage}/>
              </div>

              <div className="FormFieldMin">
                <label className="FormField__LabelMenu" htmlFor="name">Name</label>
                <input type="text" id="name" autocomplete="off" className="FormField__InputMin" name="name" value={this.state.name} onChange={this.handleChangeName} />
              </div>

              <div className="FormFieldMin">
                <label className="FormField__LabelMenu" htmlFor="price">Price</label>
                <input type="text" id="price" autocomplete="off" className="FormField__InputMin" name="price" value={this.state.price} onChange={this.handleChangePrice} />
              </div>
              <div className="FormFieldMin">
              <label className="FormField__LabelMenu" htmlFor="calories">Calories: {this.state.calories}</label>
              </div>

                 <button className="FormField__Button mr-20" onClick={this.handleSubmit}>{this.state.submit}</button>
                 </div>
        </div>
        );
    }
}

export default Add;
