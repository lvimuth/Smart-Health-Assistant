# api/services.py
from transformers import pipeline

# Load a pre-trained model for health recommendations (customize as needed)
recommendation_model = pipeline('text-generation', model='gpt-3')

def get_health_recommendation(user_data):
    prompt = f"User data: {user_data}. Provide a health recommendation."
    result = recommendation_model(prompt, max_length=50)
    return result[0]['generated_text']
