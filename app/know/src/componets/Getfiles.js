import React, { Component } from 'react';
import {BrowserRouter as Router ,Link } from 'react-router-dom'


class Getfiles extends Component {
  

constructor(props) {
    super(props);
    this.state = {files:[]};
  }



componentDidMount() {
  // Typical usage (don't forget to compare props):
         var xhr = new XMLHttpRequest();
         xhr.open('GET','/api/files');
         xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
         xhr.setRequestHeader('Authorization', '1234');
         xhr.onload = function() {
                        if (xhr.status === 200) {
                        	console.log('got files')
                          this.setState({files : JSON.parse(xhr.responseText)})
                        }
                        else{
                            console.log("error connect to API")
                        }
                        }.bind(this);
                        xhr.send();
   }

  render() {
    return (<div><h1>Files Monitored</h1>
    	 	<Router>
    	<div>
    	<table className='table table-dark'>
    	 { Object.keys(this.state.files).map(function (key) {

                    return (

                              <tr><p key={this.state.files.id}> <td>{this.state.files[key].site}</td><td><Link to={'url/'+this.state.files[key].id}>{this.state.files[key].url}</Link></td><td>{this.state.files[key].date}</td> </p></tr>

                          );
                }, this)}
       

        </table>
        </div></Router>
        </div>


    	);
  }
}

export default Getfiles;