# ReRanker Example
# 23 Apr 2024 _ 6.30PM
# Tester: Mr.Jack _ www.BICweb.vn

# https://huggingface.co/jinaai/jina-reranker-v1-tiny-en
# Model: 33M params
# Layers: 4
# Hidden size: 384

# !pip install transformers

from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained('jinaai/jina-reranker-v1-tiny-en', num_labels=1, trust_remote_code=True)

# Example query and documents
query = "Organic skincare products for sensitive skin"
print("Query:",query)

documents = [
    "Eco-friendly kitchenware for modern homes",
    "Biodegradable cleaning supplies for eco-conscious consumers",
    "Organic cotton baby clothes for sensitive skin",
    "Natural organic skincare range for sensitive skin",
    "Tech gadgets for smart homes: 2024 edition",
    "Sustainable gardening tools and compost solutions",
    "Sensitive skin-friendly facial cleansers and toners",
    "Organic food wraps and storage solutions",
    "All-natural pet food for dogs with allergies",
    "Yoga mats made from recycled materials"
]

# construct sentence pairs
sentence_pairs = [[query, doc] for doc in documents]

scores = model.compute_score(sentence_pairs)

print("Scores:",scores)

max_score = max(scores)

print("\nHighest score:",max_score)

max_index = scores.index(max_score)

print("Highest rank document:",documents[max_index])


"""
Query: Organic skincare products for sensitive skin
Scores: [0.18346597254276276, 0.2202903777360916, 0.8185698390007019, 0.954780638217926, 0.16224431991577148, 0.19299764931201935, 0.5848755836486816, 0.25678175687789917, 0.18836291134357452, 0.20082193613052368]

Highest score: 0.954780638217926
Highest rank document: Natural organic skincare range for sensitive skin

"""

