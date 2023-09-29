import os
import string

def index_txt_files(input_folder, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename in os.listdir(input_folder):
            if filename.endswith('.txt'):
                file_path = os.path.join(input_folder, filename)
                with open(file_path, 'r', encoding='utf-8') as infile:
                    # Baca setiap baris dalam file, hilangkan spasi di awal dan akhir,
                    # dan hapus baris kosong
                    lines = [line.strip() for line in infile if line.strip() != '']
                    # Gabungkan semua baris menjadi satu teks tanpa baris kosong
                    text = ' '.join(lines)
                    # Hapus semua tanda baca
                    text = text.translate(str.maketrans('', '', string.punctuation))
                    outfile.write(text)

def main():
    input_folder = 'index'
    output_file = 'tokenized.txt'
    index_txt_files(input_folder, output_file)
    print('Indeks file teks selesai.')

if __name__ == "__main__":
    main()
