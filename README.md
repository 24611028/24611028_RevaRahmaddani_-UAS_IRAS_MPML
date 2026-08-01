# 📊 Analisis & Prediksi Indeks Kerawanan Akses Sanitasi (IRAS) Jawa Tengah 2024
> **Tugas Akhir Semester (UAS) Manajemen Proyek & Machine Learning (MPML)**  
> **NIM:** 24611028 | **Nama:** REVA RAHMADDANI  

---

## 📌 Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis, mengelompokkan (clustering), dan memprediksi **Indeks Kerawanan Akses Sanitasi (IRAS)** di 35 Kabupaten/Kota Provinsi Jawa Tengah Tahun 2024 menggunakan pendekatan Machine Learning.

---

## 🔗 Tautan Penting (Quick Links)

| Kategori | Deskripsi / Sumber | Tautan |
| :--- | :--- | :--- |
| 🚀 **Web App Live** | Dashboard Interaktif Streamlit | [Buka Aplikasi Streamlit](https://nama-app-anda.streamlit.app/) *(Ganti dengan link aplikasi live)* |
| 📓 **Google Colab Notebook** | Notebook Eksperimen & Model | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/11SdrDzTrjXnrDaDye4gSKlucX8DPZWpH) |
| 📄 **Laporan LENGKAP** | Dokumen Laporan Akhir (PDF/Word) | [Lihat Laporan Dokumen](./docs/24611028_REVA%20RAHMADDANI_UAS%20MPML.docx) |
| 💻 **Kode Aplikasi** | Script Aplikasi Streamlit | [`app_iras_jateng_2024.py`](./app_iras_jateng_2024.py) |

---

## 📂 Struktur Repositori

```text
.
├── Dataset/                                # Folder dataset analisis
├── docs/                                   # Folder dokumen laporan & lampiran
│   ├── 24611028_REVA RAHMADDANI_UAS MPML.docx
│   └── Laporan_Komprehensif_UAS_MPML_24611028.md
├── app_iras_jateng_2024.py                 # Kode utama aplikasi Streamlit
├── 24611028_UAS_fixed_4.ipynb              # Notebook analisis Python / Google Colab
├── best_model_iras_jateng.pkl              # Model ANN (Artificial Neural Network) terbaik
├── scaler_iras_jateng.pkl                  # Model Scaler data
├── features_iras_jateng.pkl                # Fitur terpilih model
├── requirements.txt                        # Depedensi pustaka Python
└── README.md                               # Dokumentasi utama repositori
```

---

## 💻 Cara Menjalankan Aplikasi Lokal

1. **Clone Repositori ini:**
   ```bash
   git clone https://github.com/24611028/24611028_RevaRahmaddani_-UAS_IRAS_MPML.git
   cd 24611028_RevaRahmaddani_-UAS_IRAS_MPML
   ```

2. **Install Dependensi:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan Aplikasi Streamlit:**
   ```bash
   streamlit run app_iras_jateng_2024.py
   ```

---

## ⚙️ Fitur Utama Aplikasi

1. **Dashboard Overview & Peta Interaktif Spasial Jawa Tengah**
2. **Simulasi Prediksi IRAS Real-time (Single & Batch)**
3. **Analisis Clustering (K-Means & Hierarchical Clustering)**
4. **Perbandingan Evaluasi & Feature Importance Model ML**
