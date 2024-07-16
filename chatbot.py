from flask import Flask, request, render_template, session
import google.generativeai as genai
from PIL import Image
import io

genai.configure(api_key='AIzaSyDvWSxEts3K3bE_pOFvhXX2vTnZxOetQO8')

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'chat_history' not in session:
        session['chat_history'] = []

    if request.method == 'POST':
        text_prompt = request.form.get('text_prompt')
        image = request.files.get('image')

        if text_prompt:
            session['chat_history'].append({'role': 'user', 'content': text_prompt})

        if image and image.filename:
            img = Image.open(image)

            try:
                response = chat.send_message(text_prompt, img)
                result = response.text
                session['chat_history'].append({'role': 'bot', 'content': result})
            except Exception as e:
                result = f"Error: {str(e)}"
                session['chat_history'].append({'role': 'bot', 'content': result})

        elif text_prompt:
            try:
                response = chat.send_message(text_prompt)
                result = response.text
                session['chat_history'].append({'role': 'bot', 'content': result})
            except Exception as e:
                result = f"Error: {str(e)}"
                session['chat_history'].append({'role': 'bot', 'content': result})

    return render_template('index.html', chat_history=session['chat_history'])

if __name__ == '__main__':
    app.run(debug=True, port=8000)
