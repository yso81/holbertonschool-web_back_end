const express = require('express');

// Create express app
const app = express();
const port = 1245;

// Define route for the '/'
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

if (require.main === module) {
  app.listen(port, () => {
    console.log(`Server is listening on port ${port}`);
  });
}

module.exports = app;
