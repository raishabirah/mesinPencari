from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def search(query, documents):
    # Inisialisasi vectorizer
    vectorizer = TfidfVectorizer()

    # Hitung skor TF-IDF untuk setiap dokumen dalam korpus
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Hitung skor TF-IDF untuk query
    query_vector = vectorizer.transform([query])

    # Temukan semua dokumen yang mengandung kata kunci
    found = False
    for doc_index, doc in enumerate(documents):
        if all(keyword in doc for keyword in query.split()):
            found = True
            break

    # Cetak hasil pencarian
    if found:
        for doc_index, doc in enumerate(documents):
            if all(keyword in doc for keyword in query.split()) and tfidf_matrix[doc_index, query_vector.indices[0]] > 0:
                print(f'Dokumen {doc_index + 1}, ', end='')
                print(f'Skor: {round(tfidf_matrix[doc_index, query_vector.indices[0]], 4)}')
    else:
        print("Tidak ada dokumen yang ditemukan.")
