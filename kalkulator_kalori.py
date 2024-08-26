# -*- coding: utf-8 -*-
"""Kalkulator Kalori.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Pbdm1YFpt-ynkcschoRLPlwxvWA3TOzN
"""

# Fungsi untuk menghitung total kalori berdasarkan makanan yang dipilih
def hitung_kalori(makanan, kalori_per_gram):
    berat = float(input(f"Berapa gram {makanan} yang Anda konsumsi? "))
    total_kalori = berat * kalori_per_gram
    return total_kalori

print("Selamat Datang di kalkulator penghitung kalori Nasi dan Ayam")

# Nilai kalori per gram untuk beberapa makanan (contoh)
kalori_per_gram_dict = {
    "nasi": 4.0,
    "ayam": 2.5,
    "sayuran": 1.0
}

# Input makanan yang ingin dihitung kalorinya
makanan_input = input("Masukkan nama makanan: ").lower()

if makanan_input in kalori_per_gram_dict:
    kalori_per_gram = kalori_per_gram_dict[makanan_input]
    total_kalori = hitung_kalori(makanan_input, kalori_per_gram)
    print(f"Total kalori dari {makanan_input.capitalize()}: {total_kalori:.2f} kalori")
else:
    print("Makanan tidak ditemukan dalam daftar.")