import openai

# Paste your real API key here
openai.api_key = "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"

def ask_neonova(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are Neonova, an all-knowing helpful AI."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Ask a question
user_input = input("Ask Neonova anything: ")
answer = ask_neonova(user_input)
print("Neonova says:", answer)
