import ollama

response = ollama.list()

# print(response)
res = ollama.chat(
    model="llama3.2",
    messages=[{"role":"user", "content":"why the sky is blue?"},],
)

print(res["message"]["content"])