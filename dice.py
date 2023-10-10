from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import math

def search(query, index_file='indexWords.txt', corpus_file='tokenized.txt'):
    # Baca file korpus dan simpan dalam list
    with open(corpus_file, 'r', encoding='utf-8') as f:
        documents = [doc.strip() for doc in f.readlines()]

    # Inisialisasi vectorizer
    vectorizer = TfidfVectorizer()

    # Hitung skor TF-IDF untuk setiap dokumen dalam korpus
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Hitung skor TF-IDF untuk query
    query_vector = vectorizer.transform([query])

    # Hitung skor dice untuk setiap dokumen
    dice_similarities = []
    for doc_index, doc in enumerate(documents):
        # Hitung jumlah term yang sama dalam query dan dokumen
        common_terms = len(set(query.split()) & set(doc.split()))
        # Hitung jumlah term dalam query dan dokumen
        total_terms = len(query.split()) + len(doc.split())
        dice_similarities.append(2 * common_terms / total_terms)

    # Temukan semua dokumen yang mengandung kata kunci
    found = False
    for doc_index, doc in enumerate(documents):
        if all(keyword in doc for keyword in keyword):
            found = True
            break

    # Cetak hasil pencarian
    if found:
        for doc_index, doc in enumerate(documents):
            if all(keyword in doc for keyword in keyword) and dice_similarities[doc_index] > 0:
                print(f'Dokumen {doc_index + 1}, ', end='')
                print(f'Kemiripan: {round(dice_similarities[doc_index], 4)}')
    else:
        print("Tidak ada dokumen yang ditemukan.")

if __name__ == "__main__":
    query = input("Masukkan kata kunci: ")
    keyword = query.split()
    search(query, keyword)
