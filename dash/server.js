var mongoose = require('mongoose');
var express = require('express');
var app = express();

// Databse Querying
mongoose.connect('mongodb://localhost/test');

var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function() {
  console.log('Connected!');
});

//var collection : db.collection("result");
// Mongoose Schema definition
var Schema = mongoose.Schema;
var UserSchema = new Schema({
    // Server IP
    server_ip: String,
    // Onion ID
    onion: String,
    // Check Date
    date_check: String,
    // Server ip
    server_ip: String,
    // Shodan
    shodan_result: String,
    // Cymon
    cymon_result: String,
    // Lang
    lang: String,
    // Category
    category: String
});

// Mongoose Model definition
var User = mongoose.model('users', UserSchema);


app.use(express.static('public'));

app.get('/index.html', function (req, res) {
   res.sendFile( __dirname + "/view/index.html" );
})

app.get('/style.css', function (req, res) {
   res.sendFile( __dirname + "/view/style.css" );
})

app.get('/graph.js', function (req, res) {
   res.sendFile( __dirname + "/view/graph.js" );
})

// Send JSON files to clients
app.get('/style.raw', function (req, res) {
    res.sendFile(__dirname + "/view/style.raw")

})

app.get('/graph.json', function (req, res) {
   res.sendFile( __dirname + "/view/graph.json" );
})

var server = app.listen(8080, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("Server litenning on http://%s:%s", host, port)

})
