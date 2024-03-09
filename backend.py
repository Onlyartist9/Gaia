import os
from flask import Flask, render_template, request, jsonify
import anthropic

app = Flask(__name__)

API_KEY = os.environ.get('ANTHROPIC_API_KEY')
API_URL = 'https://api.anthropic.com/v1/messages'

@app.route("/")
def home():
    return render_template('htmx.html')

@app.route('/query/', methods=['POST'])
def query():
    if request.method == 'POST':
        user_input = request.form['userInput']
        if user_input:
            client = anthropic.Anthropic(api_key=API_KEY)

            response = client.messages.create(
                model="claude-3-sonnet-20240229", 
                messages=[
                    {"role": "user", "content": user_input}
                ],
                max_tokens=150,  
            )
            
            return_text = response.content if response else 'No response from API'

            return f"<h1>{return_text[0].text}</h1>"
        else:
            return "<h1>You didn't ask anything. Go ahead and ask.</h1>"

if __name__ == '__main__':
    app.run(debug=True)
