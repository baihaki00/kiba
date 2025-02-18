from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import openai
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Load environment variables from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

print('OPEN AI KEY ',openai.api_key)

@app.route('/api/message', methods=['POST'])
def respond():
    user_message = request.json.get("message", "").strip()

    if not user_message:
        return jsonify({"reply": "Please provide a valid question."}), 400

    try:
        # Log the received message for debugging
        print(f"Received message: {user_message}")

        # Call OpenAI's API to generate a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "system", "content": "You are an AI assistant."},
                      {"role": "user", "content": user_message}],
            temperature=0.7,
            max_tokens=150,
            top_p=0.9
        )

        # Log the entire OpenAI API response
        print(f"OpenAI response: {response}")

        # Extract the assistant's reply
        reply = response["choices"][0]["message"]["content"].strip()

        return jsonify({"reply": reply})

    except Exception as e:
        # Log the error for debugging
        print(f"Error occurred: {str(e)}")
        return jsonify({"reply": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
