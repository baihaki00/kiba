from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
model_name = "gpt2"  # You can also use "gpt2-medium", "gpt2-large", or "gpt2-xl"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Encode the input text (prompt)
prompt = "write anything specific about the space?"
inputs = tokenizer.encode(prompt, return_tensors="pt")

# Generate an attention mask (indicating which tokens are actual words and which are padding)
attention_mask = inputs.new_ones(inputs.shape)  # Attention mask with all ones (no padding)

# Generate text
outputs = model.generate(
    inputs, 
    max_length=200, 
    num_return_sequences=1, 
    no_repeat_ngram_size=2,
    do_sample=True,  # Enable sampling for randomness
    temperature=0.7,  # Adjusting temperature for more sensible output
    attention_mask=attention_mask,
    pad_token_id=tokenizer.eos_token_id
)



# Decode the generated text
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(generated_text)
