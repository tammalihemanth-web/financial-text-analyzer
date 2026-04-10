from textblob import TextBlob

choice = input("Type '1' to enter text OR '2' to use file: ")

if choice == "1":
    text = input("Enter financial text: ")
else:
    with open("data.txt", "r", encoding="utf-8") as file:
        text = file.read()

blob = TextBlob(text)

polarity = round(blob.sentiment.polarity, 3)
subjectivity = round(blob.sentiment.subjectivity, 3)

if polarity > 0:
    trend = "Positive 📈"
elif polarity < 0:
    trend = "Negative 📉"
else:
    trend = "Neutral ➖"

# sentiment label
if polarity > 0.2:
    result = "Strong Positive"
elif polarity > 0:
    result = "Mild Positive"
elif polarity < -0.2:
    result = "Strong Negative"
elif polarity < 0:
    result = "Mild Negative"
else:
    result = "Neutral"

# word count
word_count = len(text.split())
keywords = ["growth", "risk", "profit", "loss", "market"]

found_keywords = []

text_lower = text.lower()
for word in keywords:
    if word in text_lower or word + "s" in text_lower:
        found_keywords.append(word)

print("\n========== ANALYSIS RESULT ==========")
print("----------------------")
print("Polarity Score :", polarity)
print("Subjectivity   :", subjectivity)
print("Word Count     :", word_count)
print("Sentiment      :", result)
print("Trend         :", trend)

if found_keywords:
    print("Keywords      :", ", ".join(found_keywords))
else:
    print("Keywords      : None found")

print("Keyword Count  :", len(found_keywords))

if polarity < 0:
    print("⚠️ Warning: Negative financial outlook detected")
print("----------------------")