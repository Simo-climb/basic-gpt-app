import streamlit as st
import openai
import time

# Set up the OpenAI API key
openai.api_key = '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'

TOKEN_LIMIT = 500  # Set a token limit for each request

def get_gpt_response(prompt, max_tokens=TOKEN_LIMIT):
    """Get response from GPT-3 based on the given prompt."""
    retries = 3  # Number of retries
    wait_time = 10  # Wait time in seconds before retrying
    
    for _ in range(retries):
        try:
            response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=max_tokens)
            return response.choices[0].text.strip()
        except openai.error.RateLimitError:
            st.warning("Rate limit exceeded. Waiting for a few seconds before retrying...")
            time.sleep(wait_time)
    return "Error: Unable to get a response after multiple retries."

# Streamlit UI
st.title("ChatGPT Streamlit App with Token Rate Limiting")

user_input = st.text_input("Enter your prompt for ChatGPT:")

if user_input:
    response = get_gpt_response(user_input)
    st.write(response)
