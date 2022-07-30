
// import dotenv from 'dotenv'
// dotenv.config()
// import { app } from './app.js'

// const HOSTNAME = process.env.HOSTNAME
// const PORT = process.env.PORT || 80

// app.listen(PORT, HOSTNAME, () => {
//     console.log(`Server has been started on port ${PORT}`)
// })
import dotenv from 'dotenv'
dotenv.config()
import { app } from './app.js'
import fs from 'fs'
import http from 'http'
import https from 'https'

// const HOSTNAME = process.env.HOSTNAME
const PORT = process.env.PORT || 80

var options = {
    key: fs.readFileSync('./key.pem'),
    cert: fs.readFileSync('./cert.pem')
}

http.createServer(app).listen(PORT);
https.createServer(options, app).listen(443);