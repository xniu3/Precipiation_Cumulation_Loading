import express from 'express';

const router = express.Router();

// @route   GET api/auth/
// @desc    Test route
// @access  Public 
router.get('/', (req, res) =>{
    res.send("Authentication Route");
})



export default router;