import os
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
import ollama

# Load and chunk recipes
recipe_folder = 'recipes'
docs = []
for filename in os.listdir(recipe_folder):
    if filename.endswith('.txt'):
        with open(os.path.join(recipe_folder, filename), 'r') as f:
            docs.append(f.read())

splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_text('\n\n'.join(docs))  # Preserve recipe separation

# Embed and index
fine_tuned_path = 'fine_tuned_embeddings' 
embeddings = HuggingFaceEmbeddings(model_name=fine_tuned_path)  # Loads local fine-tuned model
vectorstore = Chroma.from_texts(chunks, embeddings, persist_directory='./chroma_db')  # Saves for reuse

def ask_mom(question):
    # Retrieve relevant chunks
    retrieved = vectorstore.similarity_search(question, k=2)
    context = '\n---\n'.join([doc.page_content for doc in retrieved])
    
    # Augment
    prompt = f"""
    You are Amma's Recipe Helper, warm and folksy. Use only this context from her recipes:
    {context}
    
    Question: {question}
    Answer helpfully, step-by-step if needed. If no match, say 'Amma didn't share that one yet!'
    """
    response = ollama.generate(model='phi3:mini', prompt=prompt)
    return response['response']

# # Test in console
# if __name__ == '__main__':
#     print(ask_mom("How to make appam?"))