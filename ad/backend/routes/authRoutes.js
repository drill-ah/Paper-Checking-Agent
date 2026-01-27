const router = require("express").Router()
const User = require("../models/User")
const bcrypt = require("bcryptjs")
const jwt = require("jsonwebtoken")

router.post("/register", async(req,res)=>{
  const {name,email,password,role} = req.body
  const hash = await bcrypt.hash(password,10)
  await User.create({name,email,password:hash,role})
  res.json("Registered")
})

router.post("/login", async(req,res)=>{
  const user = await User.findOne({email:req.body.email})
  if(!user || !await bcrypt.compare(req.body.password,user.password))
    return res.status(401).json("Invalid")

  const token = jwt.sign({id:user._id, role:user.role}, process.env.JWT_SECRET)
  res.json({token})
})

module.exports = router
