
import streamlit as st
import requests

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌐"
)

st.title("🌐 Language Translation Tool")

# Supported languages
languages = {
    "English": "en",
    "Urdu": "ur",
    "Arabic": "ar",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Chinese": "zh-CN"
}

# User input
text = st.text_area(
    "Enter text:",
    placeholder="Write something to translate..."
)

# Language selection
source_language = st.selectbox(
    "Source Language",
    list(languages.keys())
)

target_language = st.selectbox(
    "Target Language",
    list(languages.keys())
)

# Translate button
if st.button("Translate"):

    if not text.strip():
        st.warning("Please enter some text.")

    elif source_language == target_language:
        st.info("Source and target languages are the same.")

    else:
        source = languages[source_language]
        target = languages[target_language]

        url = "https://api.mymemory.translated.net/get"

        params = {
            "q": text,
            "langpair": f"{source}|{target}"
        }

        try:
            response = requests.get(url, params=params)

            if response.status_code == 200:

                result = response.json()

                translated_text = result["responseData"]["translatedText"]

                st.subheader("Translated Text")

                st.success(translated_text)

            else:
                st.error("Translation failed. Please try again.")

        except requests.exceptions.RequestException:
            st.error("Could not connect to the translation service.")
