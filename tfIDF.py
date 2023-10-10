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

    # Temukan semua dokumen yang mengandung kata kunci
    found = False
    for doc_index, doc in enumerate(documents):
        if all(keyword in doc for keyword in keyword):
            found = True
            break

    # Cetak hasil pencarian
    if found:
        for doc_index, doc in enumerate(documents):
            if all(keyword in doc for keyword in keyword) and tfidf_matrix[doc_index, query_vector.indices[0]] > 0:
                print(f'Dokumen {doc_index + 1}, ', end='')
                print(f'Kemiripan: {round(tfidf_matrix[doc_index, query_vector.indices[0]], 4)}')
    else:
        print("Tidak ada dokumen yang ditemukan.")

if __name__ == "__main__":
    query = input("Masukkan kata kunci: ")
    keyword = query.split()
    search(query, keyword)
