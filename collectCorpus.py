import requests
from bs4 import BeautifulSoup
import random
import os
import re

# URL halaman berita dari situs web yang diinginkan
url = 'https://news.detik.com/'

# Mengirim permintaan GET ke URL
response = requests.get(url)

# Memeriksa apakah permintaan berhasil
if response.status_code == 200:
    # Menggunakan BeautifulSoup untuk analisis HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Mencari semua tautan berita pada halaman web
    links = [a['href'] for a in soup.find_all('a', href=True)]

    # Mengambil jumlah tautan berita acak yang ingin dibuka dan disimpan
    num_links_to_open = 200

    # Mengacak urutan tautan
    random.shuffle(links)

    # Membuat direktori "korpus" jika belum ada
    if not os.path.exists('corpus'):
        os.makedirs('corpus')

    # Pola URL untuk artikel berita yang ingin disimpan
    article_pattern = r'https://news.detik.com/berita/d-\d+/.+'

    # Menghitung berapa banyak tautan berita yang berhasil diakses dan disimpan
    saved_count = 0

    # Membuka dan menyimpan hanya tautan berita acak dalam file HTML
    for idx, link in enumerate(links, start=1):
        try:
            # Memeriksa apakah link sesuai dengan pola artikel berita
            if re.match(article_pattern, link):
                # Mengirim permintaan GET ke tautan berita
                berita_response = requests.get(link)

                # Memeriksa apakah permintaan berhasil
                if berita_response.status_code == 200:
                    # Menyimpan halaman berita dalam file HTML dengan indeks yang sesuai
                    filename = f'corpus/berita_{saved_count + 1}.html'
                    with open(filename, 'w', encoding='utf-8') as file:
                        file.write(berita_response.text)
                        saved_count += 1
                        print(f"Berita_{saved_count} disimpan")
                else:
                    print(f"Gagal mengakses tautan berita {idx}")
        except Exception as e:
            print(f"Terjadi kesalahan saat mengakses tautan berita {idx}: {str(e)}")

        # Berhenti setelah menyimpan jumlah tautan yang diinginkan
        if saved_count >= num_links_to_open:
            break

    print(f"Total {saved_count} tautan berita berhasil diakses dan disimpan.")
else:
    print("Gagal mengambil halaman web.")
