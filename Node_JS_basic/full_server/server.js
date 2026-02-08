const express = require('express');
const routes = require('./routes');

const app = express();
const port = 1245;

app.use('/', routes);

app.use((req, res, next) => {
  res.status(404).send('Cannot GET /');
});

if (require.main === module) {
  app.listen(port, () => {
    console.log(`Full server is listening on port ${port}`);
    console.log(`Using database: ${process.argv[2] || 'No database path provided'}`);
  });
}

module.exports = app;
