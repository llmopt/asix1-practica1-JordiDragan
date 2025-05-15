from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="hf-inference",
    api_key="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",
)

# Leer el contenido de apache_logs.txt
with open("apache_logs.txt", "r", encoding="utf-8") as f:
    logs_content = f.read()

# Puedes ajustar el prompt según el análisis que desees
prompt = f"Analiza el siguiente log de Apache:\n\n{logs_content}"

completion = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.3",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
)

print(completion.choices[0].message)
