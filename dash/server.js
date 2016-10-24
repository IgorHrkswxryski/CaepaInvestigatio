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

// Send JSON files to clients
app.use(express.static('public'));

app.get('/index.html', function (req, res) {
   res.sendFile( __dirname + "/" + "index.html" );
})

app.get('/server.js', function (req, res) {
    User.find({ email: req.params.email }, function (err, docs) {
                docs=(true)
                res.json(docs);
            });
})

var server = app.listen(8080, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("Server litenning on http://%s:%s", host, port)

})
