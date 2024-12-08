import streamlit as st
import pandas as pd

# Judul Aplikasi
st.title("Klasemen Liga Sepak Bola")

# Input Data Tim
st.subheader("Masukkan Data Tim Liga")

# Input jumlah tim
jumlah_tim = st.number_input("Jumlah Tim", min_value=2, value=2)

# Input nama tim
tim_list = []
for i in range(jumlah_tim):
    tim_name = st.text_input(f"Nama Tim {i+1}:")
    if tim_name:
        tim_list.append(tim_name)

# Simpan data pertandingan
pertandingan_list = []

# Input hasil pertandingan
st.subheader("Masukkan Hasil Pertandingan")
for i in range(len(tim_list)):
    for j in range(i+1, len(tim_list)):
        tim_1 = tim_list[i]
        tim_2 = tim_list[j]
        st.write(f"Pertandingan: {tim_1} vs {tim_2}")
        
        gol_tim_1 = st.number_input(f"Gol yang dicetak {tim_1}", min_value=0, value=0, key=f"gol_{i}_{j}_1")
        gol_tim_2 = st.number_input(f"Gol yang dicetak {tim_2}", min_value=0, value=0, key=f"gol_{i}_{j}_2")
        
        if gol_tim_1 is not None and gol_tim_2 is not None:
            pertandingan_list.append({
                'Tim 1': tim_1,
                'Tim 2': tim_2,
                'Gol Tim 1': gol_tim_1,
                'Gol Tim 2': gol_tim_2
            })

# Tombol untuk menghitung klasemen
if st.button("Hitung Klasemen"):
    # Data untuk klasemen
    klasemen_data = {
        'Tim': [],
        'Poin': [],
        'Menang': [],
        'Seri': [],
        'Kalah': [],
        'Gol': [],
        'Gol Kebobolan': [],
        'Selisih Gol': [],
        'Pertandingan': []
    }

    # Inisialisasi semua tim dalam klasemen
    for tim in tim_list:
        klasemen_data['Tim'].append(tim)
        klasemen_data['Poin'].append(0)
        klasemen_data['Menang'].append(0)
        klasemen_data['Seri'].append(0)
        klasemen_data['Kalah'].append(0)
        klasemen_data['Gol'].append(0)
        klasemen_data['Gol Kebobolan'].append(0)
        klasemen_data['Selisih Gol'].append(0)
        klasemen_data['Pertandingan'].append(0)

    # Menghitung poin dan statistik setiap pertandingan
    for pertandingan in pertandingan_list:
        tim_1 = pertandingan['Tim 1']
        tim_2 = pertandingan['Tim 2']
        gol_tim_1 = pertandingan['Gol Tim 1']
        gol_tim_2 = pertandingan['Gol Tim 2']
        
        idx_tim_1 = klasemen_data['Tim'].index(tim_1)
        idx_tim_2 = klasemen_data['Tim'].index(tim_2)
        
        # Update statistik untuk tim 1
        klasemen_data['Gol'][idx_tim_1] += gol_tim_1
        klasemen_data['Gol Kebobolan'][idx_tim_1] += gol_tim_2
        klasemen_data['Pertandingan'][idx_tim_1] += 1
        
        # Update statistik untuk tim 2
        klasemen_data['Gol'][idx_tim_2] += gol_tim_2
        klasemen_data['Gol Kebobolan'][idx_tim_2] += gol_tim_1
        klasemen_data['Pertandingan'][idx_tim_2] += 1
        
        # Tentukan hasil pertandingan
        if gol_tim_1 > gol_tim_2:
            klasemen_data['Poin'][idx_tim_1] += 3
            klasemen_data['Menang'][idx_tim_1] += 1
            klasemen_data['Kalah'][idx_tim_2] += 1
        elif gol_tim_1 < gol_tim_2:
            klasemen_data['Poin'][idx_tim_2] += 3
            klasemen_data['Menang'][idx_tim_2] += 1
            klasemen_data['Kalah'][idx_tim_1] += 1
        else:
            klasemen_data['Poin'][idx_tim_1] += 1
            klasemen_data['Poin'][idx_tim_2] += 1
            klasemen_data['Seri'][idx_tim_1] += 1
            klasemen_data['Seri'][idx_tim_2] += 1

    # Hitung selisih gol untuk setiap tim
    for i in range(len(klasemen_data['Tim'])):
        klasemen_data['Selisih Gol'][i] = klasemen_data['Gol'][i] - klasemen_data['Gol Kebobolan'][i]

    # Buat DataFrame dari data klasemen
    df_klasemen = pd.DataFrame(klasemen_data)

    # Menampilkan klasemen
    st.write("### Klasemen Liga Sepak Bola:")
    df_sorted = df_klasemen.sort_values(by=["Poin", "Selisih Gol", "Gol"], ascending=False).reset_index(drop=True)
    st.dataframe(df_sorted)
