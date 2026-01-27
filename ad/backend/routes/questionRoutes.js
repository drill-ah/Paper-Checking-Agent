const router = require("express").Router()
const auth = require("../middleware/auth")
const Question = require("../models/Question")

router.post("/", auth, async(req,res)=>{
  if(req.user.role!=="teacher") return res.sendStatus(403)
  const q = await Question.create({...req.body, createdBy:req.user.id})
  res.json(q)
})

router.get("/", async(req,res)=> res.json(await Question.find()))

module.exports = router
