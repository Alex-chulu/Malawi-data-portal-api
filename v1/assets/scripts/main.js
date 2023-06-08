fetch('http://127.0.0.1:5000/v1/population')
  .then(response => response.json())
  .then(data => {
    // Do something with the data
    console.log(data);
  })
  .catch(error => {
    console.error(error);
  });
