# Task 1: Text Summarization using Transformers

from transformers import pipeline

# Load pre-trained summarizer
summarizer = pipeline("summarization")

# Input long article (you can replace this with your own)
article = """
Artificial Intelligence is transforming industries by enabling automation and insights.
From healthcare to finance, AI models are being trained on large datasets to identify patterns,
predict outcomes, and enhance decision-making. With tools like NLP and computer vision,
machines can now understand and interact with humans more naturally. The future of AI looks
promising as innovations continue to emerge, making it one of the most powerful technologies of our time.
"""

# Summarize the text
summary = summarizer(article, max_length=60, min_length=20, do_sample=False)

# Print summary
print("🔹 Original Text:\n", article)
print("\n🔸 Summarized Text:\n", summary[0]['summary_text'])
