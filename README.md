# Basic Q&A Generative AI Chatbot

This project is a **Streamlit-based AI chatbot** that allows users to ask **natural language questions** and receive intelligent responses using **OpenAI's GPT models**.

## Features

- **Generative AI-Powered Q&A**: Uses OpenAI's GPT models to answer user queries.
- **Customizable Model Selection**: Choose between `gpt-4o`, `gpt-4-turbo`, or `gpt-4`.
- **Temperature & Token Control**: Adjust response creativity and token limits.
- **Secure API Key Input**: Requires an OpenAI API key for authentication.
- **Interactive UI**: Simple and user-friendly interface powered by Streamlit.

## Tech Stack

- **Python**
- **Streamlit**
- **OpenAI GPT models**
- **LangChain**
- **dotenv (for environment variables management)**

## Installation

### Prerequisites

- Python 3.8+
- OpenAI API Key

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/PrinceGupta8/basic-qa-chatbot.git
   cd basic-qa-chatbot
   ```
2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application**
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Enter your OpenAI API Key** in the sidebar.
2. **Select the GPT model** (`gpt-4o`, `gpt-4-turbo`, or `gpt-4`).
3. **Adjust the temperature and token settings** for desired response behavior.
4. **Enter a question** in the text input box.
5. **Receive an AI-generated response** instantly!

## Example

**Input:**

```
What are the key differences between supervised and unsupervised learning?
```

**Output:**

```
Supervised learning requires labeled data and learns from input-output pairs, while unsupervised learning finds patterns in unlabeled data without explicit guidance...
```

## API Keys

- Get your **OpenAI API Key** from [OpenAI](https://openai.com/).
- Enter it in the Streamlit sidebar to enable AI-generated responses.

## Contributing

Pull requests are welcome! If you’d like to propose changes, open an issue first for discussion.

---

🚀 **Experience AI-powered Q&A with ease!**

