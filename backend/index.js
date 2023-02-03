const express = require("express");
const bodyParser = require("body-parser");
const http = require("http");
const app = express();
// const server = http.createServer(app);
// const path = require("path");
const cors = require('cors');
let ip = require("ip");

const httpServer = http.createServer(app);
const {Server} = require('socket.io');
console.dir (ip.address());

let i = 0
let color = [0,0,0]

app.use(cors())
app.use(bodyParser.urlencoded({extended: true}));
const port = 4000


const io = new Server(httpServer, {
    cors: {
        origin : "*",
    }
})

app.use(express.json())

// app.get("/", (req,res) => {
//     console.log(req.body);
//     res.status(200).send('Button click event received');    //res.json({msg : "vous êtes sur la route GET"});
// })

// Socket (requètes des messages)
io.on('connection', (socket) =>{
    socket.on('state', (data) =>{
        io.emit('sendFront', data)
        console.log(data)
    })
})

app.get('/', (req, res) => {
    console.log('slay');
    //io.emit('button-click', { timestamp: Date.now() });
    res.status(200).send('Button click event received oui');
    
});


// ecoute du port

httpServer.listen(port, () =>{
    console.log(`On écoute sur le port ${port}`)
})



// app.post("/post", (req,res) => {
//     console.log(req.body);
//     console.log("vous êtes sur la route post");
//     const sensorData= req.body.data;
//     console.log(`la data : ${sensorData}`);
//     res.send('data received sucessfully')
//     //res.json({msg : "vous êtes sur la route post"});
// })
// server.listen( port, () => {
//     console.log(`The server is actually listened http://localhost:${port}`)
// })
// app.post('/api/data', (req, res) => {
//     console.log(req.body);
//     res.status(200).send('Data received');
// });

// app.listen(port, () => {
//     console.log(`Server running at http://localhost:${port}`);
// });