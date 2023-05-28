import streamlit as st
import openai

# Set up your OpenAI API key
openai.api_key = "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"

# Streamlit app
def spmain():
    st.title("Text Summarization App")

    # Text input
    text = st.text_area("Enter text to summarize", height=200)

    # Button to generate summary
    if st.button("Generate Summary"):
            # Generate summary using OpenAI API
            summary = generate_summary(text)
            st.markdown("## Summary")
            st.write(summary)
            # st.warning("Please enter text to summarize.")

def generate_summary(text):
    # Use the OpenAI API to generate a summary
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        max_tokens=100,
        temperature=0.3,
        top_p=1.0,
        n=1,
        stop=None,
        echo=False
    )
    summary = response.choices[0].text.strip()
    return summary
if __name__ == "__main__":
    spmain()
