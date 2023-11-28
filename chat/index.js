var app = require('express')();
var http = require('http');
var server = http.Server(app)
var io = require('socket.io')(server);
var port = process.env.PORT || 3000;

const urlRobot = "http://127.0.0.1:5000/replies/";

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});

getReply = (message) => {
  let robotMessage = "";

  http.get(urlRobot + message, (replies) => {
    replies.on("data", (slice) => {
      robotMessage += slice;
    })

    replies.on("end", () => {
      const obj = JSON.parse(robotMessage)
      io.emit("chat message", "IronBot >> " + obj.replies);
    });
  });
}


io.on('connection', function (socket) {
  socket.on("chat message", function (msg) {
    io.emit("chat message", msg);
    getReply(msg);
  });
});

server.listen(port, function () {
  console.log('listening on *:' + port);
});