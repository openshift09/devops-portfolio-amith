const express=require("express");
const mongoose=require("mongoose");

const app=express();
const PORT = 3000;

mongoose.connect(process.env.MONGO_URL)
    .then(() => console.log("Connected to MongoDB"))
    .catch((err) => console.log("Mongo Error:", err));

app.get("/",(req,res)=> {
    res.send("Node + MongoDB + Docker Compose Working!");

});

app.listen(PORT,() => {
    console.log('Server running on port ${PORT');
});
