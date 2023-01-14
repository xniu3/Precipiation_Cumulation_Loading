import app from "./server.js"

import mongodb from "mongodb"

import dotenv from "dotenv"

dotenv.config()

const MongoClient = mongodb.MongoClient;

const port = process.env.PORT || 8000

MongoClient.connect(
    process.env.WEATHER_DB_URI,
    {
        maxPoolSize: 50,
        connectTimeoutMS: 100 
        
    }
).catch(err =>{
    console.error(err);
    process.exit()
})
.then(async client => {
    app.listen(port, ()=>{
        console.log(`listening on port ${port}`);
    })
})
