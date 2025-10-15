# South Indian recipe advisor
This project is a RAG system that turns my mom's South Indian recipes—dishes like dosa, sambar, idli, rasam, and appam that I grew up eating—into an interactive Q&A bot. Ask questions like "How does Amma make crispy dosa?" or "Ingredients for lemon rasam without garlic?" and get accurate, grounded responses pulled directly from her recipes.

Fine-tuned embeddings on South Indian recipe language (e.g., terms like "urad dal" or "tempering with mustard seeds") for better accuracy. Runs locally on CPU.

See what it looks like ⬇️

![](test.gif)

## Installation 
### 1. Setup environment
```
python -m venv rag_env
source rag_env/bin/activate  # Windows: rag_env\Scripts\activate
pip install -r requirements.txt  # (Create this file with the libs above)
```
or if you prefer conda
```
conda create -n rag_recipes python=3.10
conda activate rag_recipes
conda install pytorch torchvision torchaudio -c pytorch  # If using torch for embeddings
conda install nltk sentencepiece
pip install langchain sentence-transformers chromadb ollama streamlit datasets torch nltk # inside activated conda env
```
### 2. Install Ollama and Pull Model
- Download Ollama from https://ollama.com/download
- Pull a fast model: ```ollama pull phi3:mini``` (or gemma2:2b for smarter responses).

### 3. Prepare Recipes
- Create a recipes/ folder.
- Add .txt files (one per recipe), e.g., ```paper_dosa.txt```:
  ```
  Paper Dosa
  Ingredients: Urad dal 1 cup, idli rice 3 cups, fenugreek seeds 1 tsp, salt.
  Steps: Soak 6 hours, grind to batter, ferment overnight. Heat tawa, spread thin, cook till golden.
  Note: A childhood favorite from Chennai, best served with coconut chutney!
  ```
 - Ensure you have about 10-20 recipes, the more the better!

## Usage

### 1. Index recipes
Run ```python rag_recipes.py``` which builds vectorstore from recipes.

### 2. Ask questions
- Console test: Edit and run the script with ```print(ask_mom("How to make sambar?"))```.
- Web UI: ```streamlit run app.py``` and type queries in the browser.

### 3. Fine-Tuning Embeddings (optional)
- Upload recipes/ to a Colab notebook (use the finetune.ipynb notebook).
- Run on T4 GPU: Generates ~50-200 sentence pairs, trains for 50 epochs (~5 min).
- Download fine_tuned_embeddings.zip, unzip to ./fine_tuned_embeddings.
- Loads automatically in code for tailored searches (e.g., better matches for "tamrind" vs. generic embeddings).
