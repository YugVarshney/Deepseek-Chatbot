# 🤖 DeepSeek Chatbot

This is a simple chatbot built using **DeepSeek AI** and **Streamlit** for an interactive chat experience.

## ✨ Features
- ⚡ Uses **DeepSeek** AI model for generating intelligent responses.
- 🎨 Built with **Streamlit** for a user-friendly web UI.
- 🔄 Maintains chat history in session storage.
- 🔒 Securely loads API key using **dotenv**.

## 📦 Requirements
Make sure you have Python installed (>=3.7) and install the necessary dependencies:

```bash
pip install streamlit python-dotenv deepseek
```

## 🔑 Setup
1. **Get a DeepSeek API Key**:
   - Sign up on **DeepSeek AI** and generate an API key.
   - Copy the API key for later use.

2. **Create a `.env` file** in the project directory and add your API key:
   ```env
   DEEPSEEK_API_KEY=your_api_key_here
   ```

## 🚀 Run the Chatbot
Execute the following command in your terminal:

```bash
streamlit run main.py
```

This will start a **local web server** where you can chat with DeepSeek AI.

## 📂 Project Structure
```
📂 deepseek_chatbot
│-- main.py  # Main Streamlit app
│-- .env  # API key (not shared)
│-- requirements.txt  # Dependencies
│-- README.md  # Project documentation
```

## ☁️ Deployment
To deploy on platforms like **Streamlit Cloud, Hugging Face Spaces, or Render**:
1. Push your code to GitHub.
2. Use the platform’s **deployment guide** to connect your repository.
3. Ensure your `.env` variables are set in the hosting environment.

## 🔮 Future Enhancements
- 🎙️ Add voice-to-text input.
- 📝 Improve response formatting with Markdown.
- 💾 Store chat history in a database for analysis.

Enjoy chatting with **DeepSeek AI**! 🚀

