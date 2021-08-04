import React, {useState, useEffect} from "react";
import '../App.css';


const url = "http://localhost:5000/weatherlist"


function ConditionList(){
const [condition, setCondition] = useState("");

const configs = {
method: 'GET',
mode: 'cors'
}



return(
<h2>Condition List</h2>






)
}
export default ConditionList;