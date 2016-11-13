var mongoose = require('mongoose');
var express = require('express');

var app = express();

var graph_ok = false;

//create graph
var graph = {};
graph["elements"] = {};
var elements = graph["elements"];
elements["nodes"] = [];
elements["edges"] = [];

// Databse Querying
mongoose.connect('mongodb://localhost/TORUser');

var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function () {
    console.log('Connected!');

    var collection = db.collection("result");
    var records = collection.find({});
    records.stream()
        .on ("error", function (error){
            cb (error, 500);
        })
        .on ("data", function (record){
            cat = "";
            if(record.category && record.category.length > 0){
              cat = record.category[0];
            }
            var data = {
                "data": {
                    "id": record.onion, 
                    "name": record.onion,
                    "category": cat,
                    "lang": record.lang,
                    "date_check": record.date_check,
                    "shodan_ip": record.shodan_ip_result,
                    "shodan_keyssh": record.shodan_keyssh_result,
                }, "selected": false };
    
            elements["nodes"].push(data);
    
            var edges = []
            for( link in record.onion_link){
                edges.push( { "data":
                    { 
                        "source": record.onion, "target": link
                    }, 
                    "selected": false } );
            }
            elements["edges"].concat(edges);
        })
        .on ("end", function (){
            console.log("finish read db");
            graph_ok = true;
        })
});

//pages
app.use(express.static('public'));


app.get('/index.html', function (req, res) {
   res.sendFile( __dirname + "/view/index.html" );
})

app.get('/', function (req, res) {
   res.sendFile( __dirname + "/view/index.html" );
})

app.get('/style.css', function (req, res) {
   res.sendFile( __dirname + "/view/style.css" );
})

app.get('/graph.js', function (req, res) {
   res.sendFile( __dirname + "/view/graph.js" );
})

app.get('/style.raw', function (req, res) {
    res.sendFile(__dirname + "/view/style.raw")

})

// send graph
app.get('/graph.json', function (req, res) {
   while(graph_ok==false)
   {}
   res.send(JSON.stringify(graph));
})

// create server
var server = app.listen(8080, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("Server litenning on http://%s:%s", host, port)

})
