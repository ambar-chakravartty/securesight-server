from ollama import chat

context = "You are helping train corporate employees from falling victims to phishing scams,use randome company and link names do not use placeholders "
PROMPTS = {
    "beginner": "Generate a simple phishing email aimed at tricking users with obvious grammar mistakes and generic text. Keep it simple and blatant.",
    "intermediate": "Generate a moderately realistic phishing email about account verification. Include a suspicious link and a fake sender name.",
    "advanced": "Generate a highly realistic phishing email about unusual login activity. Include polished grammar, a legitimate tone, and obfuscated links."
}


messages = [
  {
    'role': 'user',
    'content': context + PROMPTS["intermediate"],
  },
]

response = chat('mistral',messages=messages)

print(response['message']['content'])