import express from 'express';
import connectDB from './config/db.js';
import PromiseProvider from 'mongoose';
import dotenv from "dotenv";
import userRouter from './routes/api/users.js'
import authRouter from './routes/api/auth.js'
import profileRouter from './routes/api/profile.js'
import postRouter from './routes/api/post.js'
dotenv.config();

const app = express();
const PORT = process.env.PORT;


app.get('/', (req, res) => {
    res.send('API is running');
})

// Define routers
app.use("/api/users", userRouter);
app.use("/api/auth", authRouter);
app.use("/api/profile", profileRouter);
app.use("/api/post", postRouter);


app.listen( PORT, () =>{
    console.log(`Server started on port ${PORT}`);
});

export default app;