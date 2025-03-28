# 🤖 AI Friend

A friendly AI companion built with Streamlit and local LLM inference. This chatbot provides a warm, empathetic, and engaging conversation experience using the Llama-2-7B-Chat model.

## Features

- 💭 Natural and friendly conversations
- 🤗 Emotional support and encouragement
- 💡 Personal advice and guidance
- 🎮 Fun activity suggestions
- 🌟 Daily inspiration
- 💪 Goal setting support
- 😊 Friendly chat companion

## Requirements

- Python 3.8 or higher
- Streamlit
- ctransformers
- At least 4GB of free disk space for the model

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd ai-friend
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
streamlit run app.py
```

2. Open your browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Start chatting with your AI friend! The first time you run the app, it will download the model (about 4GB) to the default cache directory.

## Model Information

- Model: Llama-2-7B-Chat
- Size: ~4GB
- Default Cache Location: `~/.cache/ctransformers`
- Project Models Location: `./models`

## Technical Details

The application uses:
- Streamlit for the web interface
- ctransformers for local model inference
- Llama-2-7B-Chat model for natural language processing
- Custom CSS for a friendly and engaging UI

## Customization

You can customize the AI's personality by modifying the system prompt in `app.py`. The current prompt is designed to create a warm, friendly, and empathetic companion.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- TheBloke for providing the quantized Llama-2 model
- Meta for the original Llama-2 model
- The Streamlit team for the amazing web framework 