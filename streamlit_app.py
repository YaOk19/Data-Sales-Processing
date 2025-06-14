import pandas as pd
import streamlit as st

# Fungsi untuk mengelompokkan customer
def kelompokan(customer_name):
    kelompok_a = [
        "KOKARMINA BOGOR", "PT. TERA LABORATORIUM INDONESIA", "PT. AAM JK2", "PT. MEDIKA LOKA MANAJEMEN - Hermina", "PT. Pembangun Pemilik Pengelola Menara Proteksi Indonesia (PT. P3MPI)", "RS HERMINA BOGOR", "RS HERMINA CIAWI", "RS HERMINA DAAN MOGOT", "RS HERMINA DEPOK", "RS HERMINA JATINEGARA", "RS HERMINA KEMAYORAN", "RS HERMINA PIK DUA", "RS HERMINA PODOMORO",
        
         "PT BERSIH AMAN CEMERLANG", "PT MEDIKALOKA PENDIDIKAN PELATIHAN - HERMINA", "PT. BERSIH AMAN CEMERLANG", "INSTITUT KESEHATAN HERMINA", "PERKUMPULAN HERMINA GROUP", 
        "PT CAHAYA BALLROOM KEMAYORAN", "PT INTEGRASI BISNIS DIGITAL", 
        "KOPERASI HERMINA PODOMORO", "KOKARMINA PUSAT", "CIPUTRA HOSPITAL CITRAGARDEN CITY",   "PT Tera Laboratorium Indonesia", "PT.Medikaloka Hermina Tbk", "RS HERMINA PUSAT", "YAYASAN PENDIDIKAN HERMINA", "KOKARMINA  CIAWI", "KOKARMINA  DEPOK", "KOKARMINA  JATINEGARA", "KOKARMINA  KEMAYORAN", "KOKARMINA PODOMORO", "KOKARMINA DAAN MOGOT", "PT. INTEGRASI BISNIS DIGITAL", "PT. CAHAYA BALLROOM KEMAYORAN"
    ]
    kelompok_b = [
        "PT.AAM BEKASI", "RS HERMINA BEKASI", "RS HERMINA CIBITUNG", "RS HERMINA GALAXY", "RS HERMINA GRANDWISATA", "RS HERMINA KARAWANG", "RS HERMINA MEKARSARI", "KOKARMINA  Bekasi", "KOKARMINA GRANDWISATA", "KOKARMINA KARAWANG", "KOKARMINA BEKASI", "KOKARMINA CIBITUNG", "KOKARMINA GALAXY", "TOKO VILA PLASTIK", "RS MASMITRA", "TOKO PLASTIK 3 BERLIAN", "TOKO OREN MANDIRI", "TOKO SEGAMAS PART,", "TOKO PLASTIK AZQIRRA,", "Toko CV. CAHAYA PELITA SURYA", "TOKO NAJWA NADZIF", "TOKO NADIN PLASTIK,", "", "", ""
    ]
    kelompok_c = [
        "PT AAM Jakarta Tangerang", "PT.  AAM TGR", "PT.  ANUGRAH ARGON MEDICA", "PT.  ANUGRAH ARGON MEDICA JK3", "PT AAMPT. ANUGRAH ARGON MEDICA JK3", "RS HERMINA CILEGON", "RS HERMINA BITUNG", "RS HERMINA CILEDUG", "RS HERMINA CIPUTAT", "RS HERMINA CIRUAS", "RS HERMINA PERIUK TANGERANG", "RS HERMINA SERPONG", "RS HERMINA TANGERANG", "KOKARMINA  CIRUAS", "KOKARMINA Bitung", "KOKARMINA  CIPUTAT", "KOKARMINA  TANGERANG", "KOKARMINA CILEGON", "KOKARMINA PERIUK TANGERANG", "KOKARMINA SERPONG", "Kokarmina Tangerang", "TOKO VILA PLASTIK,", "PT AAM,   PT. ANUGRAH ARGON MEDICA JK3", "TOKO MERIAM,", "TOKO AMINAH,", "RS SARI ASIH KARAWACI", "RS SARI ASIH CILEDUG", "TOKO PIJAR"
    ]
    # lena
    kelompok_d = [
        "RS HERMINA ACEH", "RS HERMINA LAMPUNG", "RS HERMINA MEDAN", "RS HERMINA OPI JAKABARING", "RS HERMINA PADANG", "RS HERMINA PALEMBANG", "RS HERMINA PEKANBARU", "PT Bersih Aman Cemerlang", "KOKARMINA ACEH"
    ]
    # gita
    kelompok_e = [
        "RS HERMINA ARCAMANIK", "RS HERMINA SOREANG", "RS HERMINA PASTEUR BANDUNG", "RS HERMINA SOREANG", "RS HERMINA SUKABUMI", "RS HERMINA TASIKMALAYA", "KOKARMINA  PASTEUR BANDUNG", "KOKARMINA SOREANG"
    ]
    # gita jateng
    kelompok_f = [
        "RS HERMINA BANYUMANIK", "RS HERMINA MADIUN", "RS HERMINA MALANG TANGKUBANPRAHU", "RS HERMINA MUTIARA BUNDA SALATIGA", "RS HERMINA PANDANARAN", "RS HERMINA PASURUAN", "RS HERMINA PEKALONGAN", "RS HERMINA PURWOKERTO", "RS HERMINA WONOGIRI", "RS HERMINA YOGYA", "RS HERMINA SOLO", "KOKARMINA  MADIUN", "KOKARMINA  PASURUAN"
    ]
    if customer_name in kelompok_a:
        return 'Lius'
    elif customer_name in kelompok_b:
        return 'Eva'
    elif customer_name in kelompok_c:
        return 'Rius'
    elif customer_name in kelompok_d:
        return 'Lena'
    elif customer_name in kelompok_e:
        return 'Gita'
    elif customer_name in kelompok_f:
        return 'Gita Jateng'
    else:
        return 'Lainnya'

# Membaca file CSV atau Excel yang diunggah
def upload_file():
    uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])
    if uploaded_file is not None:
        if uploaded_file.name.endswith('csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file, engine='openpyxl')

        # Menampilkan nama kolom untuk memeriksa apakah kolom yang diinginkan ada
        st.write("Nama kolom yang ditemukan dalam file:", df.columns)

        # Normalisasi kolom untuk menangani perbedaan kapitalisasi
        df.columns = df.columns.str.strip()  # Menghapus spasi yang tidak diinginkan
        df.columns = df.columns.str.title()  # Menjadikan nama kolom memiliki kapitalisasi yang benar

        # Periksa bahasa dan sesuaikan kolom
        if 'Jumlah Total' in df.columns:
            # File CSV Bahasa Indonesia
            total_amount_column = 'Jumlah Total'
            customer_name_column = 'Nama Pelanggan'
        elif 'Total Amount' in df.columns:
            # File CSV Bahasa Inggris
            total_amount_column = 'Total Amount'
            customer_name_column = 'Customer Name'
        else:
            st.error("Kolom 'Total Amount' atau 'Jumlah Total' dan 'Nama Pelanggan' atau 'Customer Name' tidak ditemukan.")
            return None

        # Pemrosesan data
        df[total_amount_column] = df[total_amount_column].replace({'Rp ': '', ',': ''}, regex=True)
        df[total_amount_column] = pd.to_numeric(df[total_amount_column], errors='coerce')  # Mengubah menjadi angka

        # Mengelompokkan berdasarkan nama pelanggan
        df['Kelompok'] = df[customer_name_column].apply(kelompokan)
        df_grouped = df.groupby(['Kelompok', customer_name_column])[total_amount_column].sum().reset_index()
        df_grouped = df_grouped.rename(columns={'Kelompok': 'Nama Sales'})

        return df_grouped
    return None

# Menampilkan hasil
def main():
    st.title("Data Sales Processing")

    df_grouped = upload_file()

    if df_grouped is not None:
        st.subheader("Processed Data")

        # Tampilkan tabel berdasarkan kelompok
        kelompok_list = df_grouped['Nama Sales'].unique()
        
        for kelompok in kelompok_list:
            st.subheader(f"Table for {kelompok}")
            df_kelompok = df_grouped[df_grouped['Nama Sales'] == kelompok]
            st.write(df_kelompok)

        # Menyediakan opsi untuk mendownload hasilnya
        st.download_button(
            label="Download Processed Data",
            data=df_grouped.to_csv(index=False),
            file_name="processed_sales_data.csv",
            mime="text/csv"
        )
        
if __name__ == "__main__":
    main()
