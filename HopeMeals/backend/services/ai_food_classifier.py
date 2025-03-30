import os
import json
from transformers import pipeline
from PIL import Image
from groq import Groq

# Initialize Groq API client
client = Groq(api_key="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")

# Load a better food classification model (ViT)
food_classifier = pipeline("image-classification", model="google/vit-base-patch16-224", framework="pt")

# List of known non-food labels to filter out
NON_FOOD_LABELS = ["plate", "dish", "bowl", "table", "utensils", "background", "cutlery"]

# Freshness filtering (Only extreme cases like expired/rotten are rejected)
EXTREME_FRESHNESS_LABELS = ["expired", "rotten", "inedible"]

def classify_food(image_path: str):
    """Classify food using Google's ViT model and verify freshness with LLAMA-3 via Groq."""

    # Step 1: Use ViT model for initial classification
    result = food_classifier(image_path)
    
    # Extract the top classification label and confidence score
    top_label = result[0]["label"].lower()
    confidence_score = result[0]["score"]

    # DEBUG: Print classification results for debugging
    print(f"Food Classification: {top_label}, Confidence: {confidence_score}")

    # Step 2: Handle misclassification cases
    if top_label in NON_FOOD_LABELS and confidence_score < 0.6:
        print("⚠️ Possible misclassification! Forcing LLAMA-3 validation...")

    # Step 3: Send to LLAMA-3 for verification
    prompt = (
        f"The image contains {top_label} with a confidence of {confidence_score:.2f}. "
        f"Is this a food item? If yes, assume it is fresh. "
        f"Classify whether it is vegetarian or non-vegetarian. "
        f"Provide a structured JSON response."
    )

    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile"
    )

    # Step 4: Parse the response from LLAMA-3
    groq_response = chat_completion.choices[0].message.content

    try:
        response_data = json.loads(groq_response)
        is_food = response_data.get("is_food", confidence_score > 0.3)
        freshness_status = response_data.get("freshness", "fresh").lower()

        # **Reject only if freshness is "expired" or "rotten"**
        if freshness_status in EXTREME_FRESHNESS_LABELS:
            return {
                "is_food": is_food,
                "freshness": freshness_status,
                "vegetarian": response_data.get("vegetarian", "unknown"),
                "message": "Food is too spoiled to donate."
            }

        # Otherwise, accept fresh/slightly stale food
        return {
            "is_food": is_food,
            "freshness": "fresh",  # Assume fresh by default
            "vegetarian": response_data.get("vegetarian", "unknown"),
            "message": "Food is recognized and accepted."
        }

    except json.JSONDecodeError:
        return {
            "is_food": confidence_score > 0.3,  # Lowered threshold to avoid false negatives
            "freshness": "fresh",
            "vegetarian": "unknown",
            "message": "LLAMA-3 response was not properly formatted, fallback to confidence threshold."
        }
