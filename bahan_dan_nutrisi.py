
import pandas as pd

# Ganti 'path_to_nutrition_file' dan 'path_to_recipe_file' dengan path file Anda
nutrition_df = pd.read_csv('nutrition.csv')
recipe_df = pd.read_csv('data_resep.csv', sep=';')  # Jika perlu delimiter spesifik
print(nutrition_df.head())
print(recipe_df.head())
import pandas as pd

# Memuat dataset
nutrition_df = pd.read_csv('nutrition.csv', sep=';')
recipe_df = pd.read_csv('data_resep.csv', sep=';')

# Bersihkan bahan pada resep
recipe_df['ingredient_clean'] = recipe_df['ingredient'].str.extract(r'([a-zA-Z\s]+)')
recipe_df['ingredient_clean'] = recipe_df['ingredient_clean'].str.strip().str.lower()

print(recipe_df[['ingredient', 'ingredient_clean']].head())

# Bersihkan nama bahan pada dataset nutrisi
nutrition_df['name_clean'] = nutrition_df['name'].str.strip().str.lower()

print(nutrition_df[['name', 'name_clean']].head())

# Gabungkan dataset berdasarkan bahan yang sudah dibersihkan
merged_df = pd.merge(recipe_df, nutrition_df, left_on='ingredient_clean', right_on='name_clean', how='left')

# Lihat hasil penggabungan
print(merged_df[['food_name', 'ingredient', 'calories', 'proteins', 'fat', 'carbohydrate']].head())

# Cek bahan-bahan yang sudah dinormalisasi
print(recipe_df['ingredient_clean'].unique())
print(nutrition_df['name_clean'].unique())

# Bersihkan lebih lanjut bahan dari satuan dan angka
recipe_df['ingredient_clean'] = recipe_df['ingredient_clean'].str.replace(r'\d+', '')  # Hapus angka
recipe_df['ingredient_clean'] = recipe_df['ingredient_clean'].str.replace(r'(kg|gram|sdm|sdt|butir|ekor)', '', regex=True)  # Hapus satuan ukuran
recipe_df['ingredient_clean'] = recipe_df['ingredient_clean'].str.strip()

print(recipe_df[['ingredient', 'ingredient_clean']].head())

# Isi nilai NaN dengan string kosong
recipe_df['ingredient_clean'] = recipe_df['ingredient_clean'].fillna('')

# Atau, Anda bisa mengabaikan baris yang memiliki nilai NaN
recipe_df = recipe_df.dropna(subset=['ingredient_clean'])

from fuzzywuzzy import process

# Fungsi untuk melakukan pencocokan fuzzy
def fuzzy_match(ingredient, choices):
    return process.extractOne(ingredient, choices)

# Terapkan pencocokan fuzzy ke semua bahan
recipe_df['matched_ingredient'] = recipe_df['ingredient_clean'].apply(lambda x: fuzzy_match(x, nutrition_df['name_clean'])[0] if x else '')

# Gabungkan hasil berdasarkan bahan yang cocok secara fuzzy
merged_df = pd.merge(recipe_df, nutrition_df, left_on='matched_ingredient', right_on='name_clean', how='left')

print(merged_df[['food_name', 'ingredient', 'matched_ingredient', 'calories', 'proteins', 'fat', 'carbohydrate']].head())

total_nutrisi = merged_df.groupby('food_name').agg({
    'calories': 'sum',
    'proteins': 'sum',
    'fat': 'sum',
    'carbohydrate': 'sum'
}).reset_index()

print(total_nutrisi)

print(merged_df.columns)

# Filter data untuk 'Kue ape'
kue_ape_data = merged_df[merged_df['food_name'].str.lower() == 'kue ape'.lower()]

# Periksa apakah data ditemukan
if not kue_ape_data.empty:
    # Kelompokkan berdasarkan bahan
    total_nutrisi = kue_ape_data.groupby('ingredient').agg({
        'calories': 'sum',
        'proteins': 'sum',
        'fat': 'sum',
        'carbohydrate': 'sum'
    }).reset_index()

    print(total_nutrisi)
else:
    print("Data untuk 'Kue ape' tidak ditemukan.")

# Minta input nama makanan dari pengguna
nama_makanan = input("Masukkan nama makanan: ").strip().lower()

# Filter data berdasarkan input nama makanan
kue_ape_data = merged_df[merged_df['food_name'].str.lower() == nama_makanan]

# Periksa apakah data ditemukan
if not kue_ape_data.empty:
    # Kelompokkan berdasarkan bahan
    total_nutrisi = kue_ape_data.groupby('ingredient').agg({
        'calories': 'sum',
        'proteins': 'sum',
        'fat': 'sum',
        'carbohydrate': 'sum'
    }).reset_index()

    print(total_nutrisi)
else:
    print(f"Data untuk '{nama_makanan}' tidak ditemukan.")

import pandas as pd

# Ganti 'path_to_nutrition_file' dan 'path_to_recipe_file' dengan path file Anda
nutrition_df = pd.read_csv('nutrition.csv')
recipe_df = pd.read_csv('data_resep.csv', sep=';')  # Jika perlu delimiter spesifik

print(nutrition_df.head())
print(recipe_df.head())

import pandas as pd

# Memuat dataset
nutrition_df = pd.read_csv('nutrition.csv', sep=';')
recipe_df = pd.read_csv('data_resep.csv', sep=';')

# Bersihkan bahan pada resep
recipe_df['ingredient_clean'] = recipe_df['ingredient'].str.extract(r'([a-zA-Z\s]+)')
recipe_df['ingredient_clean'] = recipe_df['ingredient_clean'].str.strip().str.lower()

print(recipe_df[['ingredient', 'ingredient_clean']].head())

# Bersihkan nama bahan pada dataset nutrisi
nutrition_df['name_clean'] = nutrition_df['name'].str.strip().str.lower()

print(nutrition_df[['name', 'name_clean']].head())

# Gabungkan dataset berdasarkan bahan yang sudah dibersihkan
merged_df = pd.merge(recipe_df, nutrition_df, left_on='ingredient_clean', right_on='name_clean', how='left')

# Lihat hasil penggabungan
print(merged_df[['food_name', 'ingredient', 'calories', 'proteins', 'fat', 'carbohydrate']].head())

# Cek bahan-bahan yang sudah dinormalisasi
print(recipe_df['ingredient_clean'].unique())
print(nutrition_df['name_clean'].unique())

# Bersihkan lebih lanjut bahan dari satuan dan angka
recipe_df['ingredient_clean'] = recipe_df['ingredient_clean'].str.replace(r'\d+', '')  # Hapus angka
recipe_df['ingredient_clean'] = recipe_df['ingredient_clean'].str.replace(r'(kg|gram|sdm|sdt|butir|ekor)', '', regex=True)  # Hapus satuan ukuran
recipe_df['ingredient_clean'] = recipe_df['ingredient_clean'].str.strip()

print(recipe_df[['ingredient', 'ingredient_clean']].head())



# Isi nilai NaN dengan string kosong
recipe_df['ingredient_clean'] = recipe_df['ingredient_clean'].fillna('')

# Atau, Anda bisa mengabaikan baris yang memiliki nilai NaN
recipe_df = recipe_df.dropna(subset=['ingredient_clean'])

from fuzzywuzzy import process

# Fungsi untuk melakukan pencocokan fuzzy
def fuzzy_match(ingredient, choices):
    return process.extractOne(ingredient, choices)

# Terapkan pencocokan fuzzy ke semua bahan
recipe_df['matched_ingredient'] = recipe_df['ingredient_clean'].apply(lambda x: fuzzy_match(x, nutrition_df['name_clean'])[0] if x else '')

# Gabungkan hasil berdasarkan bahan yang cocok secara fuzzy
merged_df = pd.merge(recipe_df, nutrition_df, left_on='matched_ingredient', right_on='name_clean', how='left')

print(merged_df[['food_name', 'ingredient', 'matched_ingredient', 'calories', 'proteins', 'fat', 'carbohydrate']].head())

total_nutrisi = merged_df.groupby('food_name').agg({
    'calories': 'sum',
    'proteins': 'sum',
    'fat': 'sum',
    'carbohydrate': 'sum'
}).reset_index()

print(total_nutrisi)

print(merged_df.columns)

# Filter data untuk 'Kue ape'
kue_ape_data = merged_df[merged_df['food_name'].str.lower() == 'kue ape'.lower()]

# Periksa apakah data ditemukan
if not kue_ape_data.empty:
    # Kelompokkan berdasarkan bahan
    total_nutrisi = kue_ape_data.groupby('ingredient').agg({
        'calories': 'sum',
        'proteins': 'sum',
        'fat': 'sum',
        'carbohydrate': 'sum'
    }).reset_index()

    print(total_nutrisi)
else:
    print("Data untuk 'Kue ape' tidak ditemukan.")

# Minta input nama makanan dari pengguna
nama_makanan = input("Masukkan nama makanan: ").strip().lower()

# Filter data berdasarkan input nama makanan
kue_ape_data = merged_df[merged_df['food_name'].str.lower() == nama_makanan]

# Periksa apakah data ditemukan
if not kue_ape_data.empty:
    # Kelompokkan berdasarkan bahan
    total_nutrisi = kue_ape_data.groupby('ingredient').agg({
        'calories': 'sum',
        'proteins': 'sum',
        'fat': 'sum',
        'carbohydrate': 'sum'
    }).reset_index()

    print(total_nutrisi)
else:
    print(f"Data untuk '{nama_makanan}' tidak ditemukan.")