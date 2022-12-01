import logo from './M_Logo.jpg';
import './App.css';
import ContentImage   from './contentImage';
import StyleImage from './styleImage'
//import { Response_ } from './contentImage';

function App() {
  ContentImage()
  StyleImage()
  //var Response_1 = Response_
  
  const handleSubmit = (e)=>{
    
  

    fetch("http://127.0.0.1:8000/startTraining", {
      
  })
  .then(response => response.blob())
  .then(blob => {
      var blobURL = URL.createObjectURL(blob);
      var image = document.getElementById("image.png");
      image.onload = function(){
          URL.revokeObjectURL(this.src); // release the blob URL once the image is loaded
      }
      image.src = blobURL;
  })
  .catch(error => {
      console.error(error);
  });  
  }
  
  
  
  return (
    <div className="App">
      <header className="App-header">
        <h1>Neural Dream</h1>
        <img src={logo} className="App-logo" alt="logo" />
        <ContentImage/>
        
        <StyleImage/>

        <button onClick = {handleSubmit}> Start</button>
        <img id="image.png" onClick={handleSubmit} ></img>
        
      </header>
      
    </div>
  );
}

export default App;
