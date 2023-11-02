import openai
api_key ="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"
openai.api_key = api_key

from flask import Flask, render_template, request, jsonify
import datetime
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
fine_tune_model= "davinci:ft-personal-2023-07-27-20-31-10"
def get_greeting():
    now = datetime.datetime.now()
    if 6 <= now.hour < 12:
            return "Goodmorning! I am a fraudulent mail detector. How can I help you?"
    elif 12 <= now.hour < 18:
        return "Good afternoon! The day seems fine. May I ask what issues you are facing?"
    else:
        return "Have you received a mail? You can send it to me and confirm whether it is fraud or not"

@app.route('/get_greeting')
def greeting():
    greeting_text = get_greeting()
    return jsonify({'greeting': greeting_text})

@app.route('/get_response', methods=['POST'])
def get_response():
    user_query = request.form['user_query']
    if user_query.strip() == '':
        return jsonify({'response': 'I cannot help with your querry. I am a fraud mail detector'})


    try:
        response = openai.Completion.create(
            engine="davinci:ft-personal-2023-07-27-20-31-10",  
            prompt=user_query,
            max_tokens=20
        )
        chatbot_response = response.choices[0].text.strip()
        return jsonify({'response': chatbot_response})
    except Exception as e:
        response = openai.Completion.create(
            engine="text-davinci-003",  
            prompt=user_query,
            max_tokens=20
        )
        chatbot_response = response.choices[0].text.strip()
        return jsonify({'response': "I am a fraudbot and cannot help you except for detecting fraud mail"})
                

if __name__ == '__main__':
    app.run(debug=True)