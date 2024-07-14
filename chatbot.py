
# from flask import Flask, request, render_template
# import google.generativeai as genai
# from PIL import Image
# import io
# import PIL.Image

# genai.configure(api_key='AIzaSyDvWSxEts3K3bE_pOFvhXX2vTnZxOetQO8')

# # Load the models
# model = genai.GenerativeModel('gemini-1.5-flash')

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     result = ''
#     if request.method == 'POST':
#         # Debugging: Print all form data
#         print("Form Data:", request.form)
#         print("Files Data:", request.files)

#         text_prompt = request.form.get('text_prompt')
#         image = request.files.get('image')

#         if image and image.filename:
#             print(f"Received image file: {image.filename}")
#             img = PIL.Image.open(image)

#             # Convert image to bytes
#             img_bytes = io.BytesIO()
#             img.save(img_bytes, format='PNG')  # Change format to match your image type
#             img_bytes.seek(0)

#             # Assume model.generate_content() can handle image bytes and text prompt
#             try:
#                 response = model.generate_content([text_prompt, img])
#                 result = response.text
#             except Exception as e:
#                 result = f"Error: {str(e)}"
#         elif text_prompt:
#             print(f"Received text_prompt: '{text_prompt}'")
#             try:
#                 response = model.generate_content(text_prompt)
#                 result = response.text
#             except Exception as e:
#                 result = f"Error: {str(e)}"
#         else:
#             result = "Error: Text prompt cannot be empty and image must be provided."

#     return render_template('index.html', result=result)

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, render_template, session
import google.generativeai as genai
from PIL import Image
import io
import PIL.Image

genai.configure(api_key='AIzaSyDvWSxEts3K3bE_pOFvhXX2vTnZxOetQO8')

# Load the models
model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for session management

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'chat_history' not in session:
        session['chat_history'] = []

    if request.method == 'POST':
        text_prompt = request.form.get('text_prompt')
        image = request.files.get('image')

        # Add user's text prompt to chat history
        if text_prompt:
            session['chat_history'].append({'role': 'user', 'content': text_prompt})

        if image and image.filename:
            img = PIL.Image.open(image)

            # Convert image to bytes
           

            # Process image and text together
            try:
                response = model.generate_content([text_prompt, img])
                result = response.text
                session['chat_history'].append({'role': 'bot', 'content': result})
            except Exception as e:
                result = f"Error: {str(e)}"
                session['chat_history'].append({'role': 'bot', 'content': result})

        elif text_prompt:
            # Process text only
            try:
                response = model.generate_content(text_prompt)
                result = response.text
                session['chat_history'].append({'role': 'bot', 'content': result})
            except Exception as e:
                result = f"Error: {str(e)}"
                session['chat_history'].append({'role': 'bot', 'content': result})

    return render_template('index.html', chat_history=session['chat_history'])

if __name__ == '__main__':
    app.run(debug=True)
