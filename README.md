# TC55043.10 — Natural Language Processing

Course repository for TC55043.10 NLP. Organized by class session with notebooks, datasets, and source code.

## Repository Structure

```
TC55043.10_NLP/
├── notebooks/
│   ├── Clase1/          # Regular expressions
│   ├── Clase2/          # Text processing & NLP fundamentals
│   ├── Clase3/          # Sentiment analysis & LLM prompting
│   └── Clase4/          # Week 4 exercises
├── data/
│   ├── Clase1/          # IMDB Dataset (Spanish)
│   ├── Clase2/          # Week 2 activity data
│   └── Clase3/          # Labelled sentiment datasets (IMDB, Amazon, Yelp)
├── src/                 # Source code
├── tests/               # Test suite
└── requirements.txt
```

## Notebooks

| Class | Notebook | Topic |
|-------|----------|-------|
| Clase 1 | `MNA_NLP_semana_02_active_class_regex.ipynb` | Regular expressions |
| Clase 2 | `MNA_NLP_semana_02_Actividad.ipynb` | Week 2 activity |
| Clase 2 | `MNA_NLP_semana_02_ejercicios_complementarios.ipynb` | Complementary exercises |
| Clase 3 | `MNA21_NLP_Actividad2_Analisis_de_Sentimiento.ipynb` | Sentiment analysis (Actividad 2) |
| Clase 3 | `MNA21_NLP_Actividad2_Analisis_de_Sentimiento_v2.ipynb` | Sentiment analysis v2 |
| Clase 3 | `MNA_NLP_prompts_HuggingFace_Llama.ipynb` | Prompting with HuggingFace / Llama |
| Clase 3 | `MNA_NLP_prompts_OpenAI_clase.ipynb` | Prompting with OpenAI |
| Clase 3 | `MNA_NLP_semana_03_Parte_1_ejercicios_complementarios.ipynb` | Week 3 exercises (Part 1) |
| Clase 3 | `MNA_NLP_semana_03_Parte_2_ejercicios_complementarios.ipynb` | Week 3 exercises (Part 2) |
| Clase 4 | `MNA_NLP_semana_04_ejercicios_complementarios.ipynb` | Week 4 exercises |
| Clase 4 | `MNA_NLP_Embeddings_Word2Vec_Glove_FastText-clase.ipynb` | Word2Vec, GloVe & FastText |
| Clase 4 | `MNA_NLP_semanas_4y5_Actividad_Embeddings_2026_HF.ipynb` | Embeddings activity with HuggingFace (weeks 4–5) |
| Clase 4 | `MNA_NLP_HuggingFace_y_Embeddings.ipynb` | HuggingFace & embeddings |

## Activity PDFs

| Class | File | Description |
|-------|------|-------------|
| Clase 4 | `MNA_NLP_semanas_4y5_Actividad_Embebidos_2026_HF (1).pdf` | Embeddings activity instructions (weeks 4–5) |

## Datasets

| Class | File | Description |
|-------|------|-------------|
| Clase 1 | `IMDB_Dataset_Spanish.csv` | IMDB movie reviews in Spanish |
| Clase 2 | `MNA_NLP_semana_02_Actividad_datos.txt` | Week 2 activity text data |
| Clase 3 | `imdb_labelled.txt` | 1000 IMDB sentences with positive/negative labels |
| Clase 3 | `amazon_cells_labelled.txt` | 1000 Amazon product reviews with labels |
| Clase 3 | `yelp_labelled.txt` | 1000 Yelp restaurant reviews with labels |
| Clase 4 | `imdb_labelled.txt` | 1000 IMDB sentences with positive/negative labels |
| Clase 4 | `amazon_cells_labelled.txt` | 1000 Amazon product reviews with labels |
| Clase 4 | `yelp_labelled.txt` | 1000 Yelp restaurant reviews with labels |

> Clase 3 labelled datasets from Kotzias et al., *"From Group to Individual Labels using Deep Features"*, KDD 2015.

## Setup

```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

## Dependencies

Key libraries: `scikit-learn`, `nltk`, `spacy`, `transformers`, `torch`, `datasets`, `pandas`, `matplotlib`.

See `requirements.txt` for pinned versions.
