import openai
api_key ="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"
openai.api_key = api_key

from flask import Flask, render_template, request, jsonify
import datetime
from flask_cors import CORS
medibo = Flask(__name__)
CORS(medibo)
def get_greeting():
    now = datetime.datetime.now()
    if 6 <= now.hour < 12:
            return "Goodmorning! I am your medical assistant. How can I help you?"
    elif 12 <= now.hour < 18:
        return "Good afternoon! The day seems fine. May I ask what issues you are facing?"
    else:
        return "Hello! How can I assist you this evening? Please tell me your symptoms"
@medibo.route('/get_greeting')
def greeting():
    greeting_text = get_greeting()
    return jsonify({'greeting': greeting_text})

@medibo.route('/')
def index():
    greeting = get_greeting()
    return render_template('index.html', greeting=greeting)

@medibo.route('/get_response', methods=['POST'])
def get_response():
    user_query = request.form['user_query']
    if user_query.strip() == '':
        return jsonify({'response': 'I apologize as I did not understand your question. I am a Medical assistant so anything other than symptoms and medical conditon is out of my knowledge sphere. I cannot help you with that query.'})

   
    try:
        response = openai.Completion.create(
            engine="davinci:ft-no-2023-07-20-20-56-10", 
            prompt=user_query,
            max_tokens=10
        )
        chatbot_response = response.choices[0].text.strip()
        return jsonify({'response': chatbot_response})
    except Exception as e:
        return jsonify({'response': "I apologize as I did not understand your question. I am a Medical assistant so anything other than symptoms and medical conditon is out of my knowledge sphere. I cannot help you with that query."})

if __name__ == '__main__':
    medibo.run(debug=True)