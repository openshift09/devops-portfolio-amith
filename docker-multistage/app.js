const http = require("http");

const server = http.createServer((req, res) => {
    res.end ("Docker Multi-Stage Build Example Running!");
});

server.listen(8080, () => {
    console.log("Server running on port 8080");
});