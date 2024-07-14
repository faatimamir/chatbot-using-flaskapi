
<h1 align="center">Gemini AI Web Chat 🌌</h1>

<p align="center">
  <a href="https://github.com/bisnuray/GeminiAiWeb/stargazers"><img src="https://img.shields.io/github/stars/bisnuray/GeminiAiWeb?color=blue&style=flat" alt="GitHub Repo stars"></a>
  <a href="https://github.com/bisnuray/GeminiAiWeb/issues"><img src="https://img.shields.io/github/issues/bisnuray/GeminiAiWeb" alt="GitHub issues"></a>
  <a href="https://github.com/bisnuray/GeminiAiWeb/pulls"><img src="https://img.shields.io/github/issues-pr/bisnuray/GeminiAiWeb" alt="GitHub pull requests"></a>
  <a href="https://github.com/bisnuray/GeminiAiWeb/graphs/contributors"><img src="https://img.shields.io/github/contributors/bisnuray/GeminiAiWeb?style=flat" alt="GitHub contributors"></a>
  <a href="https://github.com/bisnuray/GeminiAiWeb/network/members"><img src="https://img.shields.io/github/forks/bisnuray/GeminiAiWeb?style=flat" alt="GitHub forks"></a>
</p>

<p align="center">
  <em>Gemini is an advanced Artificial Intelligence (AI) system designed to intelligently respond to diverse prompts, including pictures. This repository contains the code for a web-based multimodal web chat application that integrates gemini AI, allowing users to interact using both text and images.</em>
</p>
<hr>

## Features

- **Text Interaction**: Users can type prompts to receive text-based responses from a generative AI model.
- **Multi-turn Conversations**: Users can chat with `gemini-pro` model that response to the chat history.
- **Image Uploads**: Users can upload images as part of their queries to the `gemini-pro-vision` AI model.
- **Real-Time AI Response**: Provides real-time responses to queries using Google's Generative AI API.
- **Syntax Highlighting and Markdown Support**: Responses that contain code are highlighted, and markdown is rendered into HTML.

### Prerequisites

- You need to have a web browser to run the the script
- An API key from Google's Generative AI service is required.
</br>
<h2 align="center">Getting Started 🚀</h2>

To utilize Gemini AI, configure your environment with the necessary API key and service account credentials. Follow these steps to get started:

1. Obtain a Google API key by following the link [here](https://makersuite.google.com/app/apikey). 

2. Set the Google API key to the script

   Replace `your_api_key` Replace with your gemini-api actual API key in this line `const API_KEY = 'your_api_key';`

## Usage

1. Install the requirements using `requirements.txt`:
   ```sh
   pip install -r requirements.txt
Start the chatbot script:

```sh
python chatbot.py
![chatbot](https://github.com/user-attachments/assets/c9cbe081-32a3-4e58-a0b5-bb84be716e2f)


Type your prompt in the input field to use gemini-pro model. This model supports multi-turn conversations (chat).

Upload an image with a prompt to use gemini-pro-vision model. This model does not support multi-turn conversations (chat).

Click the "Send" button to receive a response from the AI model.

The chat interface supports displaying messages as well as images returned from the AI model.

Rate Limits
Input Token Limit: Maximum of 12,288 tokens per request, where each token is approximately equivalent to 4 characters.
Output Token Limit: The model can generate up to 4,096 tokens in a single response.
Rate Limit: The rate limit for Gemini Pro models is 60 requests per minute (RPM).







