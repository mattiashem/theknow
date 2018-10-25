import React, { Component } from 'react';
import {BrowserRouter as Router  , Route} from 'react-router-dom'
import Getfiles from './componets/Getfiles'
import Alertfiles from './componets/Alertfiles'
import Menu from './componets/Menu' 

import './App.css';

class App extends Component {

  render() {
    return (
      <div className="App">
          <Menu/>
        
        <Router>
          <Route exact={true} path="/" component={Getfiles}/>
          <Route path="/alert/" component={Alertfiles}/>

       </Router>
      </div>
    );
  }
}

export default App;
