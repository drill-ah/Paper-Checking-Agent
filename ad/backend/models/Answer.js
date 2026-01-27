module.exports = mongoose.model("Answer", new mongoose.Schema({
  studentId:{type:mongoose.Schema.Types.ObjectId, ref:"User"},
  questionId:{type:mongoose.Schema.Types.ObjectId, ref:"Question"},
  answerText:String
}))
