import './App.css';

function App() {
  
  const studentName = "Alice";
  const favColour = "blue";
  const age = 15; 
  
  const name = "Alex";
  const currentYear = new Date().getFullYear();
  return(
    <div>
        <h1>My React Journey Begins</h1>
        <br/>
        <p>Hello, {name}</p>
        <p>Welcome to {currentYear}</p>
        <br/><br/>
        <h1>My portfolio</h1>
        <p>My name is {studentName}</p>
        <p>My fav color is {favColour} & my age is {age}</p>

      </div>
  )
}

export default App;