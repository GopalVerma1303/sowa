import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import re

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

stop_words = set(stopwords.words('english'))

class Node:
    def __init__(self, content, level):
        self.content = content
        self.level = level
        self.children = []

def create_hierarchical_index(text):
    # Split text into chapters (assuming chapters start with "Chapter" or a number)
    chapters = re.split(r'\n(?=Chapter|\d+\.)', text)
    
    root = Node("Textbook", 0)
    
    for chapter in chapters:
        chapter_node = Node(chapter[:100] + "...", 1)  # Store first 100 chars as preview
        root.children.append(chapter_node)
        
        # Split chapter into sections (assuming sections start with a number followed by a dot)
        sections = re.split(r'\n(?=\d+\.)', chapter)
        
        for section in sections[1:]:  # Skip the first one as it's the chapter title
            section_node = Node(section[:100] + "...", 2)
            chapter_node.children.append(section_node)
            
            # Split section into paragraphs
            paragraphs = section.split('\n\n')
            
            for paragraph in paragraphs:
                if len(paragraph.split()) > 20:  # Only consider paragraphs with more than 20 words
                    paragraph_node = Node(paragraph, 3)
                    section_node.children.append(paragraph_node)
    
    return root

def index_to_dict(node):
    return {
        'content': node.content,
        'level': node.level,
        'children': [index_to_dict(child) for child in node.children]
    }