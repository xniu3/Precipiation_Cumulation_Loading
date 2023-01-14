import express from "express"

const router  = express.Router()

router.route("/").get((req, res) => 
    res.send("Hello, Router!")
);


export default router 