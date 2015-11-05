var express = require('express');
var PtBible = require("bible-portuguese");
var app = express();

app.get('/api', function(req,res) {
  res.send('Welcome to bible_helper api');
});

app.get('/api/:theme', function(req, res) {
  var theme = req.params.theme;
  res.json({ name: theme, verses:{}});
});

app.use('/', express.static(__dirname + '/static'));

app.listen(3000);
