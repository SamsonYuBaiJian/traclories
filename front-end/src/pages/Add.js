import React, { Component } from 'react';
import { BrowserRouter as Link, NavLink } from 'react-router-dom';
import axios from 'axios';

class Add extends Component {

    constructor() {
        super();
        this.state ={
            name: '',
            image: '',
            calories: '',
            price: ''
        }


        this.handleChangeName = this.handleChangeName.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChangePrice = this.handleChangePrice.bind(this);
        this.handleChangeImage = this.handleChangeImage.bind(this);
    }

    handleChangeImage(e) {
        e.preventDefault();

        this.setState({
          image: "https://upload.wikimedia.org/wikipedia/commons/7/71/Hainanese_Chicken_Rice.jpg"
        });
    }

    handleChangeName(e) {
        this.setState({
          name: e.target.value
        });

        axios.post('http://127.0.0.1:5000/calculate', {
            name: this.state.name,
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
            image: "https://upload.wikimedia.org/wikipedia/commons/7/71/Hainanese_Chicken_Rice.jpg",
            calories: this.state.calories,
            price: this.state.price
        })
            .then(res => {
                console.log(res);
            });
    }


    render() {

        return (
        <div className="App">
          <div className="App__AsideMenu">
          <div className="Small__Title">
          Traclories
          </div>
          </div>

          <div className="App__FormMenu">
              <div className="FormTitle">
                  <NavLink to="/menu" activeClassName="FormTitle__Link--Active" className="FormTitle__Link">Menu</NavLink>
                  or<NavLink exact to="/add-items" activeClassName="FormTitle__Link--Active" className="FormTitle__Link">Add Items</NavLink>
                  or<NavLink exact to="/sign-in" activeClassName="FormTitle__Link--Active" className="FormTitle__Link">Sign Out</NavLink>
              </div>
              <div className="Store__Name">
              Changi Chicken Rice
              </div>

              <div className="Gap">
              <input type="file" id="image" name="image" value={this.state.image} onChange={this.handleChangeImage}/>
              </div>

              <div className="FormField">
                <label className="FormField__Label" htmlFor="name">Item Name</label>
                <input type="text" id="name" className="FormField__Input" placeholder="Enter item name" name="name" value={this.state.name} onChange={this.handleChangeName} />
              </div>

              <div className="FormField">
                <label className="FormField__Label" htmlFor="price">Price</label>
                <input type="text" id="price" className="FormField__Input" placeholder="Enter price" name="price" value={this.state.price} onChange={this.handleChangePrice} />
              </div>
              <div className="Gap">
              <label className="FormField__Label" htmlFor="calories">Calories: {this.state.calories}</label>
              </div>

              <div className="FormField">
                 <button className="FormField__Button mr-20" onClick={this.handleSubmit}>Submit</button>
              </div>
          </div>
        </div>
        );
    }
}

export default Add;
