const express = require("express");
const bodyParser = require("body-parser");
const http = require("http");
const app = express();
const server = http.createServer(app);
const path = require("path");
let ip = require("ip");
console.dir (ip.address());
let i = 0
let color = [0,0,0]

app.use(bodyParser.urlencoded({extended: true}));
const port = 4000

app.get("/", (req,res) => {
    console.log(req.body);
    res.send({"data":"vous êtes sur la route get"});
    //res.json({msg : "vous êtes sur la route GET"});
})

app.post("/post", (req,res) => {
    console.log(req.body);
    res.send({"data":"vous êtes sur la route post"});
    const sensorData= req.body.data;
    console.log(`la data : ${sensorData}`);
    res.send('data received sucessfully')
    //res.json({msg : "vous êtes sur la route post"});
})
server.listen( port, () => {
    console.log(`The server is actually listened`)
})
// app.post('/api/data', (req, res) => {
//     console.log(req.body);
//     res.status(200).send('Data received');
// });

// app.listen(port, () => {
//     console.log(`Server running at http://localhost:${port}`);
// });