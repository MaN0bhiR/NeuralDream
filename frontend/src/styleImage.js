import React, { useState } from "react";

const StyleImage = () => {
  const [selectedImage, setSelectedImage] = useState(null);

  const fileChangeHandler = (e) =>{
    setSelectedImage(e.target.files[0]);
    console.log(e.target.files[0]);
  }

  const handleSubmit = (e)=>{
    const form_data = new FormData();
    form_data.append("file" , selectedImage , selectedImage.name);

  

  const requestOptions = {
    method : 'POST', body : form_data
  };

  fetch("http://127.0.0.1:8000/uploadStyle" , requestOptions).
  then(Response => Response.json())
  .then(function(Response){
    console.log(Response)
  })
}
  return (
    <div>
      
      {selectedImage && (
        <div>
        <img alt="not fount" width={"300px"} src={URL.createObjectURL(selectedImage)} />
        <br />
        <button onClick={()=>setSelectedImage(null)}>Remove</button>
        <button onClick ={handleSubmit}>Upload</button>
        </div>
      )}
      <br />
     
      <br /> 
      <input
        type="file"
        name="myImage"
        accept=".jpeg , .jpg , .git , .png , ."
        onChange={(fileChangeHandler) 
        }
        
      />
    </div>
  );
};

export default StyleImage;