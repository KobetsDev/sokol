
import express from 'express'
import nunjucks from 'nunjucks'
import dotenv from 'dotenv'
dotenv.config()
import path, { dirname } from 'path'
import mongoose from 'mongoose'
import router from './routes/index.js'
import { fileURLToPath } from 'url';
const app = express()
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
// console.log(express.static(__dirname + '/assets'))
mongoose.connect(process.env.DB_URL)
    .then(() => console.log('MongoDB Connected'))
    .catch(error => console.log(error))


// шаблонизатор
app.set('view engine', 'html')
nunjucks.configure('templates', {
    autoescape: true,
    express: app
})
app.use(express.static(__dirname + '/static'));
// app.use('/static', express.static((path.resolve('static'))))//__dirname, 'static')))
app.disable('etag')

app.use('/', router)

export { app };

