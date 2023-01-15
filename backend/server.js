import express from 'express';
import connectDB from './config/db.js';
import PromiseProvider from 'mongoose';
import dotenv from "dotenv";

dotenv.config();

const app = express();
const PORT = process.env.PORT;


app.get('/', (req, res) => {
    res.send('API is running');
})

app.listen( PORT, () =>{
    console.log(`Server started on port ${PORT}`);
});

export default app;