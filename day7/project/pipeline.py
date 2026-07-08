import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# 1. Saved CSV Data-va load pandrom
df = pd.read_csv('spam.csv')

# 2. Data-va Train (80%) matrum Test (20%) nu pirikurom
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.2, random_state=42)

# 3. CountVectorizer vachu Text-a Numbers-a maathuroam
vectorizer = CountVectorizer()
X_train_vectors = vectorizer.fit_transform(X_train)
X_test_vectors = vectorizer.transform(X_test)

# 4. MultinomialNB Model-a train pandrom
model = MultinomialNB()
model.fit(X_train_vectors, y_train)

# 5. Model Performance-a measure pandrom (Testing)
predictions = model.predict(X_test_vectors)
accuracy = accuracy_score(y_test, predictions)

print("=== SPAM DETECTION PIPELINE REPORT ===")
print(f"Total Training Data: {len(X_train)} messages")
print(f"Total Testing Data: {len(X_test)} messages")
print(f"Model Accuracy: {accuracy * 100:.2f}%\n")

# Detailed Report (Precision, Recall details)
print("Detailed Classification Report:")
print(classification_report(y_test, predictions))

# 6. Namma custom message-a test pandrom
pudhu_msg = ["Daily 500rs bonus! login now to claim your reward! and enjoy money on your account."]

# Mukkiyam: Inga 'transform' mattum dhaan podanum, 'fit' panna koodadhu
msg_vector = vectorizer.transform(pudhu_msg)

# AI kitta mudivu kekkurom
mudivu = model.predict(msg_vector)

print("\n--- LIVE TEST ---")
print(f"Message: {pudhu_msg[0]}")
print(f"AI Prediction: {mudivu[0].upper()}")