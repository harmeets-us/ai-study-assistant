def generate_quiz(text):
    questions = []
    sentences = text.split('.')

    for i, sentence in enumerate(sentences[:5]):
        sentence = sentence.strip()

        if len(sentence) > 20:
            questions.append({
                "question": f"What is the meaning of: {sentence[:50]}...?",
                "answer": sentence
            })

    return questions