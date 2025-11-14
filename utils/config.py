# utils/config.py
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATA_PATH_RAW = "data/arxiv_papers.csv"
DATA_PATH_CLEAN = "data/clean_papers.csv"
FAISS_INDEX_PATH = "data/faiss_index"
EMBEDDING_MODEL = "text-embedding-3-small"
MAX_PAPERS = None