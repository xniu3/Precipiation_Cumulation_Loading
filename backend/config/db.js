import mongoose from "mongoose";
import data from "./default.json" assert { type: "json" };
// console.log(`db is ${data.mongoURI}`);
const db = data.mongoURI
const connectDB = async () => {
    try{
        await mongoose.connect(db, {
            useNewUrlParser: true
        });
        console.log("MongoDB connected ... ");
    } catch (err) {
        console.error(err.message);
        // Exit process with failure
        process.exit(1);
    }
}

//mongoose.connect(data.mongoURI);

export default connectDB;
// module.exports = connectDB;

