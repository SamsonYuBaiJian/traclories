import React, { Component } from 'react';
import { BrowserRouter as Link, NavLink } from 'react-router-dom';
import axios from 'axios';

class Menu extends Component {

    constructor() {
        super();

        this.state ={
            items: []
        };

        axios.get('http://127.0.0.1:5000/menu')
            .then((response) => {
                console.log("response", response);
                var arr = []
                for (var i = 0; i < response.data.length; i++) {
                    arr.push(response.data[i]);
                }
                this.setState({
                    items: arr
                });
            })
            .catch((error) => {
                console.log(error);
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

                {this.state.items.map(function(item,index){
                        return <div className="Image">
                                <img src={item[0]}/>
                                <div className="Data"><u>Name</u>: {item[1]}</div>
                                <div className="Data"><u>Price</u>: ${item[2]}</div>
                                <div className="Data"><u>Calories</u>: {item[3]}</div>
                            </div>
                })}
          </div>
        </div>
        );
    }
}

export default Menu;
