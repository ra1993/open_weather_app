import React from 'react';
import './../App.css';

//routes/components
import ConditionList from './SelectCondition'
import ConditionMenu from './ConditionMenu';


// import {BrowserRouter, Route, Switch} from 'react-router-dom';
// import {useSelector} from 'react-redux'

function Homepage(props) {
    // const pToken = useSelector(state => state.token)
    // console.log('Token', pToken)
    return (
    <div className="userHomepage">
      <h1>Weather</h1>
  
      <center><h2>Weather Condition Finder</h2></center>
       <ConditionMenu/>
      
      <br></br>
        <ConditionList/>    
      <br></br>
    
      {/* <div className="notepad">Notes Component</div>*/}
     
      {/* </div>   */}
      </div>
    )}
  
  export default Homepage; 
  