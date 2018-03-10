

const express = require('express');

const app = express();

const port = 8080;

app.get('/', function(req, res){

  console.log('request received');

  res.status(200).send('nodejs running inside docker!')
})

app.listen(8080, function() {
  console.log('Express listening on port ' + 8080 + '!');
});

