# Import necessary libraries
import nltk
from nltk import ngrams
import gradio as gr

# Download NLTK data
nltk.download('punkt')

# Function to generate n-grams from text
def generate_ngrams(text, n):
    tokens = nltk.word_tokenize(text)
    n_grams = list(ngrams(tokens, n))
    return [' '.join(gram) for gram in n_grams]

# Gradio Interface
iface = gr.Interface(
    fn=generate_ngrams,
    inputs=gr.Textbox(),
    outputs=gr.Textbox(),
    live=True,
    title="N-gram Extractor",
    description="Enter a text passage, and the application will output the n-grams.",
)

# Launch the Gradio interface
iface.launch()
