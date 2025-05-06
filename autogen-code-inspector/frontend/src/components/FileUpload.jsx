import React, { useState } from 'react';

console.log('API URL:', process.env.REACT_APP_API_URL);

function FileUpload() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    setFile(selectedFile);
    console.log('File selected:', selectedFile);
  };

  const handleFileUpload = async () => {
    if (!file) {
      setMessage('No file selected');
      console.log('Error: No file selected');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);
    console.log('FormData prepared:', formData);

    try {
      console.log('Sending file to the server...');
      const response = await fetch(`${process.env.REACT_APP_API_URL}/upload`, {
        method: 'POST',
        body: formData,
      });

      console.log('Response received:', response);

      const data = await response.json();
      console.log('Response data:', data);

      if (response.ok) {
        setMessage(`Success: ${data.message}`);
        console.log('File uploaded successfully');
      } else {
        setMessage(`Error: ${data.error}`);
        console.log('Error in file upload:', data.error);
      }
    } catch (error) {
      setMessage('Error uploading file');
      console.log('Error during upload:', error);
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleFileUpload}>Upload</button>
      <p>{message}</p>
    </div>
  );
}

export default FileUpload;
