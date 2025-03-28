import streamlit as st
import json
from ctransformers import AutoModelForCausalLM
import os
from pathlib import Path

# Configure the page
st.set_page_config(
    page_title="AI Friend",
    page_icon="🤖",
    layout="wide"
)

# Set up model directory
MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)  # Create directory if it doesn't exist, don't error if it does

# Get default cache directory
DEFAULT_CACHE = str(Path.home() / ".cache" / "ctransformers")

# Initialize session state for chat history and model
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add system prompt for friendly personality
    st.session_state.messages.append({
        "role": "system",
        "content": "You are a warm, friendly, and empathetic AI companion. You use a conversational and caring tone, show genuine interest in the user's thoughts and feelings, and provide supportive and encouraging responses. You use appropriate emojis occasionally to make the conversation more engaging and friendly. You maintain a positive and uplifting attitude while being authentic and understanding."
    })
if "model" not in st.session_state:
    st.session_state.model = None

# Custom CSS for better UI
st.markdown("""
    <style>
    .stTextInput>div>div>input {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #FF6B6B;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
    }
    .stButton>button:hover {
        background-color: #FF8B8B;
    }
    .welcome-message {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 1rem;
        margin: 1rem 0;
        border-left: 4px solid #FF6B6B;
        color: #000000;
    }
    </style>
    """, unsafe_allow_html=True)

# Header with friendly welcome
st.title("🤖 AI Friend")
st.markdown("""
    <div class="welcome-message">
    👋 Hi there! I'm your friendly AI companion, and I'm so excited to chat with you! 
    Whether you want to share your thoughts, get advice, or just have a friendly conversation, 
    I'm here to listen and chat. What's on your mind today? 😊
    </div>
    """, unsafe_allow_html=True)

# Display chat messages
for message in st.session_state.messages:
    if message["role"] != "system":  # Don't display system messages
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to talk about? 😊"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # Initialize model if not already done
        if st.session_state.model is None:
            with st.spinner("🤖 Getting ready to chat with you... This might take a minute..."):
                st.info(f"📥 The model will be downloaded to: {os.path.abspath(MODEL_DIR)}")
                st.session_state.model = AutoModelForCausalLM.from_pretrained(
                    "TheBloke/Llama-2-7B-Chat-GGUF",
                    model_file="llama-2-7b-chat.Q4_K_M.gguf",
                    model_type="llama",
                    max_new_tokens=512,
                    temperature=0.8,  # Slightly higher temperature for more personality
                    context_length=2048,
                    top_p=0.95,  # Add top_p for better response diversity
                    repetition_penalty=1.1  # Add repetition penalty to avoid repetitive responses
                )

        # Format the conversation for the model
        conversation = ""
        for msg in st.session_state.messages:
            if msg["role"] == "system":
                conversation += f"System: {msg['content']}\n"
            elif msg["role"] == "user":
                conversation += f"Human: {msg['content']}\n"
            else:
                conversation += f"Assistant: {msg['content']}\n"
        
        # Generate response
        with st.spinner("💭 Thinking about what you said..."):
            response = st.session_state.model(
                conversation + "Assistant:",
                max_new_tokens=512,
                temperature=0.8,
                top_p=0.95,
                repetition_penalty=1.1,
                stop=["Human:", "\n\n"]
            )
            
            assistant_message = response.strip()
            st.session_state.messages.append({"role": "assistant", "content": assistant_message})
            
            with st.chat_message("assistant"):
                st.markdown(assistant_message)
            
    except Exception as e:
        st.error(f"Oops! Something went wrong: {str(e)}")
        st.error(f"""
        If this is the first time running the app, it's downloading the model to:
        {os.path.abspath(MODEL_DIR)}
        Please wait a few minutes and try again. I'll be right here! 😊
        """)

# Sidebar with information and features
with st.sidebar:
    st.markdown("### 🌟 What We Can Do Together")
    st.markdown("""
    - 💭 Share thoughts and feelings
    - 🤗 Provide emotional support
    - 💡 Give friendly advice
    - 🎮 Suggest fun activities
    - 🌟 Share daily inspiration
    - 💪 Offer encouragement
    - 🎯 Help with goals
    - 😊 Be a friendly chat buddy
    """)
    
    # Model information
    st.markdown("### 📦 Model Information")
    st.markdown(f"""
    - Model: Llama-2-7B-Chat
    - Location: {os.path.abspath(MODEL_DIR)}
    - Size: ~4GB
    """)
    
    # Clear chat button
    if st.button("🗑️ Start Fresh Chat"):
        st.session_state.messages = [st.session_state.messages[0]]  # Keep system prompt
        st.rerun() 