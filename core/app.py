from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Initialize DialoGPT model and tokenizer
model_name = "microsoft/DialoGPT-medium"  # You can use "medium" or "large" based on your preference
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Ensure the tokenizer uses the EOS token properly
tokenizer.pad_token = tokenizer.eos_token

@app.route('/api/message', methods=['POST'])
def respond():
    user_message = request.json.get("message", "").lower()

    # Ensure there's a message from the user
    if not user_message:
        return jsonify({"reply": "Please provide a valid question."}), 400

    # Encode the user message and add the special tokens needed for dialogue generation
    input_ids = tokenizer.encode(user_message + tokenizer.eos_token, return_tensors="pt")

    # Generate a response from DialoGPT
    outputs = model.generate(
        input_ids,
        max_length=150,
        num_beams=5,
        temperature=0.7,
        top_p=0.9,
        early_stopping=True
    )

    # Decode the output and remove the special tokens
    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Extract only the bot's reply (split by user message to avoid concatenation)
    if user_message in reply:
        reply = reply.split(user_message, 1)[-1].strip()

    # Return the generated reply
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
