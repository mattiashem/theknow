import React, { Component } from 'react';
import {BrowserRouter as Router ,Link } from 'react-router-dom'


class Alertfiles extends Component {
  

constructor(props) {
    super(props);
    this.state = {alerts:[]};
  }



componentDidMount() {
  // Typical usage (don't forget to compare props):
         var xhr = new XMLHttpRequest();
         xhr.open('GET','/api/alerts');
         xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
         xhr.setRequestHeader('Authorization', '1234');
         xhr.onload = function() {
                        if (xhr.status === 200) {
                        	console.log('got files')
                          this.setState({alerts : JSON.parse(xhr.responseText)})
                        }
                        else{
                            console.log("error connect to API")
                        }
                        }.bind(this);
                        xhr.send();
   }

  render() {
    return (<div><h1>Alert</h1>
    	 	<Router>
    	<div>
    	<table className='table table-dark'>
    	 { Object.keys(this.state.alerts).map(function (key) {

                    return (

                              <tr><p key={this.state.alerts.id}> <td>{this.state.alerts[key].site}</td><td><Link to={'url/'+this.state.alerts[key].id}>{this.state.alerts[key].url}</Link></td><td>{this.state.alerts[key].date}</td> </p></tr>

                          );
                }, this)}
       

        </table>
        </div></Router>
        </div>


    	);
  }
}

export default Alertfiles;