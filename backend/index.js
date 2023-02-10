const express = require("express");
const bodyParser = require("body-parser");

const cors = require('cors');
const {Server} = require('socket.io');
const http = require("http");
let ip = require("ip");

const app = express();
const server = http.createServer(app);
console.dir (ip.address());
const port = 3000;

const io = new Server(server, {
    cors: {
        origin: '*'
    }
})

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(cors({
    origins: '*'
}))


app.get('/', (req, res) => {
    res.json({"hello": "world!"});
})

app.post('/post', (req, res) => {
    console.log(req.body);
    //io.emit('button-click', { timestamp: Date.now() });
    res.status(200).json({"msg": "Data sent"});
    
});


io.on("connection", (socket) => {
    console.log(`New connection: ${socket.id}`);
    socket.emit("hello", "world");
})

// ecoute du port

server.listen(port, () =>{
    console.log(`On écoute sur le port ${port}`)
})