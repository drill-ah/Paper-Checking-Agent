module.exports = mongoose.model("Result", new mongoose.Schema({
  studentId:mongoose.Schema.Types.ObjectId,
  questionId:mongoose.Schema.Types.ObjectId,
  score:Number,
  feedback:String
}))
