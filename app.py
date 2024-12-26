import streamlit as st
import json
from text_extraction import extract_text_from_pdf
from hierarchical_indexing import create_hierarchical_index, index_to_dict
from retrieval import create_faiss_index, retrieve_relevant_text
from question_answering import answer_question
from database import init_db, save_query, get_query_history, save_textbook_structure, get_textbook_structure

# Set page config
st.set_page_config(page_title="SOWA", page_icon="📚", layout="wide")

# Initialize database
init_db()

# Custom CSS
def local_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

# App title and description
#st.set_page_config(page_title="Advanced Textbook Q&A", page_icon="📚", layout="wide") #Removed as per instructions

# Sidebar
with st.sidebar:
    # st.image("https://your-logo-url.com/logo.png", width=200)
    st.title("SOWA")
    st.markdown("Unlock the knowledge within your textbooks! 🚀")
    
    # File upload
    uploaded_files = st.file_uploader("Choose up to 3 PDF textbooks", type="pdf", accept_multiple_files=True)

# Initialize session state
if 'textbooks' not in st.session_state:
    st.session_state.textbooks = {}

# Main content
st.title("📚 SOWA")

if uploaded_files:
    for file in uploaded_files[:3]:  # Limit to 3 textbooks
        if file.name not in st.session_state.textbooks:
            with st.spinner(f"Processing {file.name}..."):
                # Extract text
                text = extract_text_from_pdf(file)
                
                # Create hierarchical index
                index = create_hierarchical_index(text)
                
                # Create FAISS index for efficient retrieval
                faiss_index, indexed_texts = create_faiss_index([node.content for node in index.children])
                
                st.session_state.textbooks[file.name] = {
                    "text": text,
                    "index": index_to_dict(index),
                    "faiss_index": faiss_index,
                    "indexed_texts": indexed_texts
                }
                
                # Save textbook structure to database
                save_textbook_structure(file.name, json.dumps(index_to_dict(index)))
            
            st.success(f"{file.name} processed successfully!")

# Textbook selection and querying
if st.session_state.textbooks:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        selected_textbook = st.selectbox("Select a textbook:", list(st.session_state.textbooks.keys()))
    
    with col2:
        query = st.text_input("Enter your question:", placeholder="What would you like to know?")
    
    if query:
        with st.spinner("🔍 Searching for answers..."):
            # Retrieve relevant text
            relevant_texts = retrieve_relevant_text(
                query, 
                st.session_state.textbooks[selected_textbook]["faiss_index"],
                st.session_state.textbooks[selected_textbook]["indexed_texts"]
            )
            
            # Combine relevant texts
            context = " ".join(relevant_texts)
            
            # Answer question
            answer = answer_question(query, context)
            
            # Save query to database
            save_query(selected_textbook, query, answer)
            
            # Display answer
            st.markdown("## 💡 Answer")
            st.info(answer)
            
            # Display relevant context
            with st.expander("📖 Relevant Context", expanded=False):
                for i, text in enumerate(relevant_texts, 1):
                    st.markdown(f"**Excerpt {i}:**")
                    st.write(text[:300] + "...")  # Show first 300 characters of each relevant text
                    st.markdown("---")
    
    # Display textbook structure
    with st.expander("📑 Textbook Structure", expanded=False):
        structure = get_textbook_structure(selected_textbook)
        if structure:
            structure_dict = json.loads(structure)
            st.write(f"### Chapters in {selected_textbook}")
            for i, chapter in enumerate(structure_dict['children'], 1):
                st.write(f"{i}. {chapter['content']}")
                for j, section in enumerate(chapter['children'], 1):
                    st.write(f"   {i}.{j} {section['content']}")

    # Display query history
    with st.expander("📜 Query History", expanded=False):
        history = get_query_history()
        for entry in history:
            st.write(f"**Textbook:** {entry[0]}")
            st.write(f"**Query:** {entry[1]}")
            st.write(f"**Answer:** {entry[2]}")
            st.write(f"**Timestamp:** {entry[3]}")
            st.markdown("---")

else:
    st.info("👆 Please upload at least one textbook to start querying.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Mansi")
