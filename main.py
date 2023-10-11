if __name__ == "__main__":
    from tfIDF import search as tfidf_search
    from dice import dice_similarity_search

    # Memilih algoritma yang akan digunakan
    print("Pencarian Informasi:\n1: TF-IDF\n2: Dice Similarity")
    algorithm_choice = int(input("Pilih algoritma: "))
    query = input("Masukkan kata kunci: ")

    with open('tokenized.txt', 'r', encoding='utf-8') as f:
        documents = [doc.strip() for doc in f.readlines()]

    if algorithm_choice == 1:
        # Gunakan pencarian TF-IDF
        tfidf_search(query, documents)
    elif algorithm_choice == 2:
        # Gunakan pencarian Dice Similarity
        dice_similarity_search(query, documents)
    else:
        print("Pilihan algoritma tidak valid.")
