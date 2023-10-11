from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def dice_similarity_search(query, documents):
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
        if all(keyword in doc for keyword in query.split()):
            found = True
            break

    # Cetak hasil pencarian
    if found:
        for doc_index, doc in enumerate(documents):
            if all(keyword in doc for keyword in query.split()) and dice_similarities[doc_index] > 0:
                print(f'Dokumen {doc_index + 1}, ', end='')
                print(f'Skor: {round(dice_similarities[doc_index], 4)}')
    else:
        print("Tidak ada dokumen yang ditemukan.")
