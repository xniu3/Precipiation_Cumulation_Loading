//configure an expres file 
// .env file is used to save the environment variables. 

import express from "express";
import cors from "cors";
import weather from "./api/weather.route.js";


const app = express();


// configure middle ware
app.use(cors());
app.use(express.json);// our server can accept json in the body of the request. 
// any request could be re-jsoned. 
app.use("/api/v1/weather", weather);
app.use("*", (req, res) => res.status(404).json({error: "Not Found!"}));


export default app;





