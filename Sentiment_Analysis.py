
import re

# Positive sentiment words
positive_words = {
    "good", "great", "excellent", "happy", "love",
    "awesome", "amazing", "wonderful", "best",
    "beautiful", "nice", "fantastic", "perfect",
    "brilliant", "enjoy", "enjoyed", "success"
}

# Negative sentiment words
negative_words = {
    "bad", "worst", "poor", "sad", "hate",
    "terrible", "awful", "boring", "angry",
    "disappointing", "dislike", "failed",
    "horrible", "ugly", "problem"
}

# Negation words
negations = {
    "not", "no", "never", "isn't",
    "wasn't", "don't", "doesn't", "didn't"
}

# Sentiment analysis function
def analyze_sentiment(sentence):

    words = re.findall(r"[a-z]+(?:'[a-z]+)?", sentence.lower())

    positive_score = 0
    negative_score = 0

    for i, word in enumerate(words):

        negated = i > 0 and words[i - 1] in negations

        if word in positive_words:

            if negated:
                negative_score += 1
            else:
                positive_score += 1

        elif word in negative_words:

            if negated:
                positive_score += 1
            else:
                negative_score += 1

    if positive_score > negative_score:
        sentiment = "Positive"

    elif negative_score > positive_score:
        sentiment = "Negative"

    else:
        sentiment = "Neutral"

    return positive_score, negative_score, sentiment


# Main program
def main():

    print("=" * 50)
    print("       NLP SENTIMENT ANALYSIS PROJECT")
    print("=" * 50)

    print("Analyze movie reviews, product reviews, or sentences.")
    print("Type exit to stop the program.")

    while True:

        sentence = input("\nEnter a sentence: ")

        if sentence.lower() == "exit":
            print("Thank you!")
            break

        positive, negative, result = analyze_sentiment(sentence)

        print("\n---------- RESULT ----------")
        print("Input Sentence :", sentence)
        print("Positive Score:", positive)
        print("Negative Score:", negative)
        print("Sentiment     :", result)
        print("---------------------------")


# Run program
if __name__ == "__main__":
    main()
