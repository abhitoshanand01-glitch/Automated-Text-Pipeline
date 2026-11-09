import streamlit as st
import os
from core_processor import parse_poetry_file, fetch_article_from_url
from image_generator import create_poetry_image 
from latex_generator import generate_latex_book_page

st.title("✨ Automated Text & Article Publisher")
st.write("Link paste karein YA raw text type karein aur jadoo dekhein!")

# URL Input aur Text Area dono options
url_input = st.text_input("🔗 Yahan kisi article ka Web URL paste karein:")
st.write("--- YA ---")

default_text = """TITLE: [Write Title Here]
AUTHOR: [Write Author Here]
---
[Write your text or poem here...]"""

user_input = st.text_area("📝 Input Text (Metadata + Text)", value=default_text, height=250)

if st.button("Generate Outputs"):
    # Agar user ne URL dala hai, toh text box ko ignore karke URL se data layenge
    if url_input:
        with st.spinner('Article fetch ho raha hai...'):
            final_input = fetch_article_from_url(url_input)
            st.success("Article successfully fetched!")
    else:
        final_input = user_input
        
    # 1. Input ko ek temporary file mein save karna
    temp_file = "temp_input.txt"
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(final_input)
    
    # 2. Processor se meta aur lines nikalna
    meta, poem = parse_poetry_file(temp_file)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📱 Social Media Post")
        create_poetry_image(meta, poem)
        image_path = os.path.join("output_social", "kavita_post.png")
        if os.path.exists(image_path):
            st.image(image_path, caption="Ready for Instagram/Facebook")
            
    with col2:
        st.subheader("📖 Print-Ready Book Page")
        generate_latex_book_page(meta, poem)
        latex_path = os.path.join("output_book", "kavita_book_page.tex")
        if os.path.exists(latex_path):
            with open(latex_path, "r", encoding="utf-8") as f:
                latex_code = f.read()
            st.code(latex_code, language="latex")
            st.success("Copy the code and paste to Overleaf!")