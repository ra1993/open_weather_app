import React, {useState, useEffect} from "react";
// import IncomingTime from './IncomingTime';


function ConditionMenu(props) {
  const [conditions, setConditions] = useState([])
  const [selectedCondition, setSelectedCondition] = useState()
  const renderConditions = () => {
    return conditions.map((condition, i) => {
      return ( <option value={i} key={'condition-option-' + i}>{condition}</option> )
    })
  }

  const onChange = (e) => {
    setSelectedCondition(props.conditions[Number(e.currentTarget.value)])
  }

  useEffect(() => {
    if(props.conditions !== undefined) {
      setConditions(props.conditions)
      setSelectedCondition(props.conditions[0])
    }
  }, [props.conditions])

  return (
    <>
      <select  className = "conditionList"
        onChange = {onChange}>
          {renderConditions()}
      </select>
      {selectedCondition}
      
    </>
  );
}

export default ConditionMenu;


{/* 
 function ConditionMenu () {
return(
<div className = "conditionMenu"> 
<div className = "submit-btn">Choose One</div>
<div className = "conditionMenu-content">
<div className="conditionMenu-item">
  Thunderstorm
  </div>

</div>
</div>
)}

ReactDOM.render(<App />), document.querySelector("#root") */}
