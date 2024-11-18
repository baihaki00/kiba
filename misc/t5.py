from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load pre-trained T5 model and tokenizer
model_name = "t5-large"
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

# Input text
question = "who is the first president of united states?"

# Format the question for T5 in a more explicit way
input_text = f"answer the following question: {question}"

# Tokenize input
inputs = tokenizer(input_text, return_tensors="pt")

# Generate the answer
outputs = model.generate(inputs["input_ids"], max_length=50)

# Decode and print the generated answer
answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(answer)
