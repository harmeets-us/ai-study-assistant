def generate_flashcards(text):
    cards = []
    sentences = text.split('.')
    for sentence in sentences[:5]:
        sentence = sentence.strip()
        if len(sentence) > 20:
            cards.append({"front": "Explain","back": sentence})
    return cards
        