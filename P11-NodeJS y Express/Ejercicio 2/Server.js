const express = require('express')
const app = express()
const port = 3001
const userRouters = require('./app/routes/user')

app.use(userRouters)

app.listen(port, () => {
    console.log('La aplicación está en línea!');
})