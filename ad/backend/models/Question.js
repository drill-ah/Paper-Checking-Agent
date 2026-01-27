module.exports = mongoose.model("Question", new mongoose.Schema({
  title:String,
  questionText:String,
  maxMarks:Number,
  subject:String,
  createdBy:{type:mongoose.Schema.Types.ObjectId, ref:"User"}
}))
