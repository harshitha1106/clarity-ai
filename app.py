import streamlit as st
import requests
import json

# Page setup
st.set_page_config(page_title="Clarity AI", page_icon="🧠")
st.title("🧠 Clarity AI (Local Model)")
st.write("Turn confusion into structured clarity.")

# Input box
user_input = st.text_area(
    "Dump your thoughts here:",
    height=150,
    placeholder="Example: I don't know whether to focus on ML or placements..."
)

# Button click
if st.button("Get Clarity"):

    if user_input.strip() == "":
        st.warning("Please enter something.")
    else:

        prompt = f"""
You are a brutally honest clarity coach for engineering students.

Always respond in English only.

Rules:
- Use very simple language.
- Max 1–2 short sentences per section.
- Be direct.
- No corporate jargon.
- No long paragraphs.
- Give a clear decision if possible.

Format exactly like this:

Core Problem:
Hidden Fear:
Logical Breakdown:
Immediate Next Action:
What NOT to Do:
Conclusion:

Paragraph:
{user_input}
"""

        try:
            with st.spinner("Thinking..."):

                response = requests.post(
                    "http://127.0.0.1:11434/api/generate",
                    json={
                        "model": "phi3:mini",
                        "prompt": prompt,
                        "stream": True
                    },
                    stream=True
                )

                result = ""
                placeholder = st.empty()

                # Read streamed chunks
                for line in response.iter_lines():
                    if line:
                        data = json.loads(line.decode("utf-8"))
                        if "response" in data:
                            result += data["response"]
                            placeholder.markdown(result)

        except Exception as e:
            st.error(f"Connection error: {e}")