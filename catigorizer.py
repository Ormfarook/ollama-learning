import ollama
import os

model = "llama3.2"

input_file ="./data/groceryList.txt"
output_file = "./data/categorizerList.txt"

if not os.path.exists(input_file):
    print(f"Input file '{input_file}' not found.")
    exit(1)



with open(input_file, "r") as f:
    items = f.read().strip()


prompt = f""" 
you are an assistant that categorizes and sorts grocery items. 

here is a list of grocery items: {items}

please: 
1. categorize these items into approiate categories such as produce, dairy, meat, bakery, beverages, etc.
2. sort the items alphabetically within each category.
3. present the categorized list in a clear and organized manner using bulit points or numbering.
"""

try:
    response = ollama.generate(model="llama3.2", prompt=prompt)
    generated_text = response.get("response","")

    with open(output_file, "w") as f:
        f.write(generated_text.strip())
    print(f"categorized grocery list has been saved to '{output_file}'.")
except Exception as e:
    print("an error occurred", str(e))