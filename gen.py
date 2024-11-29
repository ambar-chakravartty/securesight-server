# from ollama import chat

# # Define prompts for varying difficulties


# # Function to generate phishing emails using OpenAI GPT
# def generate_phishing_email(difficulty, max_tokens=150):
#     if difficulty not in PROMPTS:
#         raise ValueError("Invalid difficulty level. Choose from 'beginner', 'intermediate', or 'advanced'.")
    
#     prompt = PROMPTS[difficulty]
    
#     response = ollama.chat(
#         model="mistral",  # You can use other models like gpt-4 if available
#         messages=[{"role":"system","content":context + prompt}]
#     )
    
#     return response



# print(chat('mistral',messages=[{"role":"system","content":context + PROMPTS["intermediate"]}]))

# # Generate phishing emails for each difficulty level
# # for level in ["beginner", "intermediate", "advanced"]:
# #     print(f"--- {level.capitalize()} Phishing Email ---")
# #     print(generate_phishing_email(level))
# #     print("\n")

from flask import Flask, request, jsonify
from flask_cors import CORS
from ollama import chat
import random

app = Flask(__name__)
CORS(app)

context = "You are helping train corporate employees from falling victims to phishing scams "
PROMPTS = [
    "Generate a simple phishing email aimed at tricking users with obvious grammar mistakes and generic text. Keep it simple and blatant.",
     "Generate a moderately realistic phishing email about account verification. Include a suspicious link and a fake sender name.",
     "Generate a highly realistic phishing email about unusual login activity. Include polished grammar, a legitimate tone, and obfuscated links."
]

prompt = random.choice(PROMPTS)
is_scam = random.choice([True,False])
messages = []

if is_scam:
    messages = [
    {
      'role': 'user',
      'content': context + prompt,
    },
    ]
else:
    messages = [{
        'role':'user',
        'content':'generate a genuine email from a company to a custom'
    },
    ]
    



@app.route('/generate-email')
def email():
    try:
        response = chat('mistral', messages=messages)

        return jsonify({"email":response['message']['content'],"scam":is_scam})
    except Exception as e:
        print("Error: ",e)
        return jsonify({'error': str(e)}), 500

         
        


if __name__ == '__main__':
    app.run(debug=True)