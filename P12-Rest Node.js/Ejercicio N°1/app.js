const express = require('express');
const app = express();
const cors = require('cors');
app.use(cors());


app.listen('3000',() => {
    console.log("Servidor en ejecucion");
})

const GRouter=require('./routes/score');
app.use('/api',GRouter);