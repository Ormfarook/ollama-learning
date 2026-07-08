import ollama

response = ollama.list()

# print(response)
res = ollama.chat(
    model="llama3.2",
    messages=[{"role":"user", "content":"why the sky is blue?"},],
)

# print(res["message"]["content"])

res2 = ollama.chat(
    model="llama3.2",
    stream=True,
    messages=[{"role":"user", "content": "how many types of anime and how are they classified?"},],
)

for chunk in res2:
    print(chunk["message"]["content"], end="", flush= True)

res3 = ollama.generate(
    model="llama3.2", 
    prompt=" what is your favorit anime?"
)

# we can show 
print(ollama.show("llama3.2"))
