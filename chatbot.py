import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

class FAQChatbot:
    def __init__(self, kb_path="knowledge_base.csv"):
        self.kb_path = kb_path
        self.kb = None
        self.model = None
        self.q_embeddings = None
        self.load_kb()

    def load_kb(self):
        if not os.path.exists(self.kb_path):
            raise FileNotFoundError(f"Knowledge base file not found: {self.kb_path}")
        self.kb = pd.read_csv(self.kb_path)
        #Fill blanks just in case
        self.kb = self.kb.fillna("")
        #Only use Q&A pairs with both fields
        self.kb = self.kb[(self.kb["question"].str.strip() != "") & (self.kb["answer"].str.strip() != "")]
        #Load small, fast model
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        #Compute question embeddings
        self.q_embeddings = self.model.encode(self.kb["question"].tolist())

    def get_answer(self, user_question, threshold=0.65, top_k=1):
        if not user_question or not user_question.strip():
            return "Please enter a question so I can help you out."

        #Embed the input question
        question_vec = self.model.encode([user_question])
        sims = cosine_similarity(question_vec, self.q_embeddings)[0]

        #Get top matches
        best_idx = np.argmax(sims)
        best_score = sims[best_idx]
        if best_score < threshold:
            return "Sorry, I’m not sure about that one. Want to talk to a real person?"
        #If you want to show top_k results, you could do:
        #top_indices = np.argsort(sims)[-top_k:][::-1]
        #return self.kb.iloc[top_indices[0]]["answer"]
        return self.kb.iloc[best_idx]["answer"]

    def reload_kb(self, new_kb_path):
        self.kb_path = new_kb_path
        self.load_kb()
