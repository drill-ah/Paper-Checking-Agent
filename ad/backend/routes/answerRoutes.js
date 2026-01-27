const router = require("express").Router()
const Answer = require("../models/Answer")
const auth = require("../middleware/auth")

router.post("/", auth, async(req,res)=>{
  const a = await Answer.create({...req.body, studentId:req.user.id})
  res.json(a)
})

module.exports = router
