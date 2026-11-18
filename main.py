
# AIXcelerate - Happy or Sad Mood Guesser

# DATASET
train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),
    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad")
]


# LEVEL 1: COUNT THE MOODS

def count_moods(data):
    happy_count = 0
    sad_count = 0

    for sentence, mood in data:
        if mood == "Happy":
            happy_count += 1
        elif mood == "Sad":
            sad_count += 1

    return happy_count, sad_count


print("LEVEL 1: MOOD COUNT")
print("Mood Count:", count_moods(train_data))


# LEVEL 2: GUESS THE MOOD

# Exactly 7 words in each list
happy_words = [
    "marks", "won", "surprise", "tasty",
    "excited", "selected", "favourite"
]

sad_words = [
    "lost", "failed", "moving", "cancelled",
    "upset", "stopped", "lonely"
]


def guess_mood(sentence):

    # Convert to lowercase and remove punctuation
    clean_sentence = ""

    for ch in sentence.lower():
        if ch.isalnum() or ch.isspace():
            clean_sentence += ch

    words = clean_sentence.split()

    happy_count = 0
    sad_count = 0

    for word in words:
        if word in happy_words:
            happy_count += 1

        if word in sad_words:
            sad_count += 1

    if happy_count > sad_count:
        return "Happy"

    elif sad_count > happy_count:
        return "Sad"

    else:
        # Tie: choose Happy as the default mood.
        return "Happy"


# LEVEL 3: TEST THE PROGRAM

practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train was late and I felt upset", "Sad"),
    ("Today was a great day", "Happy")
]


print("\nLEVEL 2: MOOD GUESSING")

for sentence, actual_mood in practice_data:
    predicted_mood = guess_mood(sentence)

    print("Sentence:", sentence)
    print("Predicted Mood:", predicted_mood)
    print()


print("LEVEL 3: ACCURACY")

correct = 0

for sentence, actual_mood in practice_data:
    predicted_mood = guess_mood(sentence)

    if predicted_mood == actual_mood:
        correct += 1

total = len(practice_data)

accuracy = (correct / total) * 100

print("Correct Predictions:", correct)
print("Total Sentences:", total)
print("Accuracy:", accuracy, "%")
