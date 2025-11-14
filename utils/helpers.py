# utils/helpers.py
import pandas as pd
from langchain.schema import Document

def pick_column(df, candidates):
    for c in candidates:
        if c in df.columns:
            return c
    raise ValueError(f"None of {candidates} found in columns: {df.columns.tolist()}")

def build_documents(df):
    docs = []
    for i, row in df.iterrows():
        meta = {"title": row["title"], "categories": row.get("categories"), "row_id": int(i)}
        docs.append(Document(page_content=row["text"], metadata=meta))
    return docs