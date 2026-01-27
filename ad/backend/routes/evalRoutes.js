const router = require("express").Router()
const axios = require("axios")
const Result = require("../models/Result")

router.post("/:answerId", async(req,res)=>{
  const ai = await axios.post("http://localhost:8000/evaluate", req.body)
  const result = await Result.create(ai.data)
  res.json(result)
})

module.exports = router
