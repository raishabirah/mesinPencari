import numpy as np

def dice_similarity_search(query, documents):

    # Hitung skor dice untuk setiap dokumen
    dice_similarities = []
    for doc_index, doc in enumerate(documents):
        # Hitung jumlah term yang sama dalam query dan dokumen
        common_terms = len(set(query.split()) & set(doc.split()))
        # Hitung jumlah term dalam query dan dokumen
        total_terms = len(query.split()) + len(doc.split())
        dice_similarities.append(2 * common_terms / total_terms)

    # Cetak hasil pencarian
    found = False
    for doc_index, doc in enumerate(documents):
        if all(keyword in doc for keyword in query.split()):
            found = True
            break

    # Cetak hasil pencarian
    if found:
        for doc_index, doc in enumerate(documents):
            if all(keyword in doc for keyword in query.split()) and dice_similarities[doc_index] > 0:
                term_positions = {}
                for term in query.split():
                    positions = [i for i, token in enumerate(doc.split()) if token == term]
                    term_positions[term] = positions
                for term, positions in term_positions.items():
                    print(f'Dokumen {doc_index + 1}, index: {positions}')
                    print(f'Skor: {round(dice_similarities[doc_index], 4)}')
    else:
        print("Tidak ada dokumen yang ditemukan.")
