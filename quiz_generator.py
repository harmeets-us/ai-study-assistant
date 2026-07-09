def genrate_quiz(text):
   questions = []
   sentences = text.split('.')
   for i, sentence in enumerate(sentences[:5]):
      sentence = sentence.strip()
      if len(sentence) > 20:
            questions.append({"question": f"Q{i+1}: complete the statement: {sentence}", "answer": sentence})
   return questions