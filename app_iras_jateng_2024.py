# ==============================================================================
# INTELLIGENT REGIONAL ANALYTICS SYSTEM (IRAS) PROVINSI JAWA TENGAH 2024
# STREAMLIT DASHBOARD UNTUK DUKUNGAN KEPUTUSAN PEMERINTAH DAERAH (FORMAL & CARD-BASED)
# NIM: 24611028 | REVA RAHMADDANI
# ==============================================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import base64
import folium
from streamlit_folium import st_folium

# 1. Page Configuration
st.set_page_config(
    page_title="IRAS Pemprov Jawa Tengah 2024 - Decision Support System",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Base64 Logo Loader for 100% Reliable HTML Rendering
def get_base64_logo():
    logo_path = "logo_jawa_tengah.png"
    if not os.path.exists(logo_path):
        logo_path = "Dataset/logo_jawa_tengah.png"
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

logo_b64 = get_base64_logo()

# 3. Advanced Custom CSS Styling (Card-Based Sidebar & High-Contrast Visuals)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background-color: #F8FAFC;
    }
    
    /* Header Banner */
    .gov-header {
        background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 100%);
        padding: 24px 30px;
        border-radius: 14px;
        color: white;
        box-shadow: 0 10px 20px -5px rgba(15, 23, 42, 0.25);
        margin-bottom: 25px;
        border-bottom: 5px solid #D97706;
    }
    .gov-title {
        font-size: 2.1rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin: 0;
        color: #FFFFFF !important;
    }
    .gov-subtitle {
        font-size: 1.02rem;
        color: #E2E8F0 !important;
        font-weight: 500;
        margin-top: 6px;
    }
    .gov-badge {
        background-color: #D97706;
        color: #FFFFFF !important;
        font-size: 0.78rem;
        font-weight: 700;
        padding: 4px 14px;
        border-radius: 20px;
        display: inline-block;
        margin-bottom: 8px;
        text-transform: uppercase;
        letter-spacing: 0.6px;
    }
    
    /* -------------------------------------------------------------------------
       SIDEBAR CARD-BASED DESIGN & CRISP CONTRAST
       ------------------------------------------------------------------------- */
    section[data-testid="stSidebar"] {
        background-color: #F1F5F9 !important;
        border-right: 1px solid #CBD5E1;
        padding-top: 15px;
    }
    
    /* Force crisp dark navy text for sidebar */
    section[data-testid="stSidebar"] *, 
    section[data-testid="stSidebar"] p, 
    section[data-testid="stSidebar"] span, 
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #0F172A !important;
    }
    
    /* Custom Sidebar Card Container */
    .sb-card {
        background-color: #FFFFFF !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 14px !important;
        padding: 18px 16px !important;
        margin-bottom: 18px !important;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.05) !important;
    }
    
    .sb-brand-card {
        text-align: center;
        border-top: 5px solid #1E3A8A !important;
    }
    .sb-logo-img {
        display: block;
        margin: 0 auto 12px auto;
        height: 100px;
        object-fit: contain;
    }
    .sb-brand-title {
        font-size: 1.08rem;
        font-weight: 800;
        color: #0F172A !important;
        line-height: 1.3;
        margin-top: 6px;
        letter-spacing: -0.3px;
    }
    .sb-brand-sub {
        font-size: 0.78rem;
        color: #475569 !important;
        font-weight: 600;
        margin-top: 4px;
    }
    
    .sb-card-header {
        font-size: 0.88rem;
        font-weight: 800;
        color: #1E3A8A !important;
        text-transform: uppercase;
        letter-spacing: 0.6px;
        margin-bottom: 14px;
        display: flex;
        align-items: center;
        gap: 8px;
        border-bottom: 2px solid #F1F5F9;
        padding-bottom: 8px;
    }

    /* Individual Radio Choice Card Box Buttons */
    div[data-testid="stSidebar"] div[role="radiogroup"] {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }
    
    div[data-testid="stSidebar"] div[role="radiogroup"] label {
        background-color: #F8FAFC !important;
        border: 1.5px solid #E2E8F0 !important;
        border-radius: 10px !important;
        padding: 12px 14px !important;
        margin: 0 !important;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02) !important;
        transition: all 0.2s ease-in-out !important;
        cursor: pointer !important;
    }
    
    div[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
        background-color: #EFF6FF !important;
        border-color: #1E3A8A !important;
        box-shadow: 0 4px 8px rgba(30, 58, 138, 0.1) !important;
        transform: translateY(-1px) !important;
    }
    
    div[data-testid="stSidebar"] div[role="radiogroup"] label p {
        font-weight: 700 !important;
        font-size: 0.88rem !important;
        color: #0F172A !important;
    }
    
    /* Main Content Metric Cards */
    .metric-box {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.03);
        border-top: 4px solid #1E3A8A;
        transition: transform 0.2s ease;
    }
    .metric-box:hover {
        transform: translateY(-3px);
    }
    .metric-label {
        font-size: 0.82rem;
        font-weight: 700;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .metric-value {
        font-size: 1.85rem;
        font-weight: 800;
        color: #0F172A;
        margin: 6px 0;
    }
    .metric-delta {
        font-size: 0.82rem;
        font-weight: 600;
    }
    .delta-good { color: #059669; }

    /* Explicit Dark Contrast Caption */
    .map-legend-caption {
        color: #0F172A !important;
        font-size: 0.92rem !important;
        font-weight: 600 !important;
        margin-top: 14px !important;
        background-color: #FFFFFF !important;
        padding: 10px 16px !important;
        border-radius: 8px !important;
        border: 1px solid #E2E8F0 !important;
        display: inline-block !important;
    }

    /* Footer */
    .gov-footer {
        text-align: center;
        padding: 22px;
        color: #475569 !important;
        font-size: 0.85rem;
        border-top: 1px solid #E2E8F0;
        margin-top: 40px;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# 4. Load Data & Model Assets
@st.cache_data
def load_dataset():
    paths = [
        "Dataset/Dataset_Kemiskinan_Stunting_JawaTengah_2024.xlsx",
        "Dataset_Kemiskinan_Stunting_JawaTengah_2024.xlsx"
    ]
    target_path = None
    for p in paths:
        if os.path.exists(p):
            target_path = p
            break
    if target_path is None:
        raise FileNotFoundError("File Dataset_Kemiskinan_Stunting_JawaTengah_2024.xlsx tidak ditemukan di folder repositori.")
    
    try:
        df = pd.read_excel(target_path, sheet_name='Data_Jateng_2024')
    except Exception:
        df = pd.read_excel(target_path)

    df.columns = [
        "kode_wilayah", "kabupaten_kota", "persentase_penduduk_miskin",
        "prevalensi_stunting", "ipm", "pengeluaran_per_kapita",
        "akses_sanitasi_layak", "akses_air_minum_layak",
        "jumlah_puskesmas", "curah_hujan_tahunan"
    ]
    return df

@st.cache_resource
def load_ml_assets():
    model = joblib.load("best_model_iras_jateng.pkl")
    scaler = joblib.load("scaler_iras_jateng.pkl")
    features = joblib.load("features_iras_jateng.pkl")
    return model, scaler, features

try:
    df = load_dataset()
    model, scaler, features = load_ml_assets()
    data_loaded = True
except Exception as e:
    st.error(f"Gagal memuat aset ML atau Dataset: {e}")
    data_loaded = False

if data_loaded:
    # --------------------------------------------------------------------------
    # SIDEBAR CARD-BASED DESIGN (FORMAL & INDIVIDUAL CHOICE BOXES)
    # --------------------------------------------------------------------------
    with st.sidebar:
        # BRAND CARD WITH BASE64 LOGO
        if logo_b64:
            img_html = f'<img src="data:image/png;base64,{logo_b64}" class="sb-logo-img" alt="Logo Pemprov Jateng" />'
        else:
            img_html = '<div style="font-size: 3rem; margin-bottom: 10px;">🏛️</div>'

        st.markdown(f"""
        <div class="sb-card sb-brand-card">
            {img_html}
            <div class="sb-brand-title">PEMERINTAH PROVINSI<br>JAWA TENGAH</div>
            <div class="sb-brand-sub">Badan Perencanaan & Analytical Center (IRAS)</div>
        </div>
        """, unsafe_allow_html=True)

        # NAVIGATION CARD CONTAINER
        st.markdown("""
        <div class="sb-card">
            <div class="sb-card-header">📌 Navigasi Sistem Analytics</div>
        """, unsafe_allow_html=True)
        
        menu = st.radio(
            "Pilih Modul Dashboard:",
            [
                "🏛️ 1. Dashboard Ringkasan Eksekutif", 
                "🗺️ 2. Peta Spasial & Clustering Wilayah", 
                "💡 3. Simulasi Prediksi & Intervensi Kebijakan"
            ],
            label_visibility="collapsed"
        )
        
        st.markdown("</div>", unsafe_allow_html=True)

        # SYSTEM INFO CARD CONTAINER
        st.markdown(f"""
        <div class="sb-card">
            <div class="sb-card-header">ℹ️ Informasi Sistem</div>
            <div style="font-size: 0.83rem; line-height: 1.6; color: #0F172A;">
                <b>Sistem Analytics:</b> IRAS v2.4 (Revisi 4)<br>
                <b>Tahun Pengamatan:</b> 2024<br>
                <b>Model Utama:</b> ANN (Artificial Neural Network)<br>
                <b>Prediktor Optimal:</b> {len(features)} Variabel<br>
                <b>CV Mean Accuracy:</b> <span style="color:#059669; font-weight:700;">82.9%</span><br>
                <b>Unit Analisis:</b> 35 Kab/Kota
            </div>
        </div>
        """, unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # MAIN HEADER BANNER
    # --------------------------------------------------------------------------
    st.markdown("""
    <div class="gov-header">
        <div class="gov-badge">Intelligent Regional Analytics System (IRAS)</div>
        <h1 class="gov-title">Sistem Pendukung Keputusan Pengentasan Kemiskinan & Stunting</h1>
        <div class="gov-subtitle">Integrasi Data BPS, Kementerian Kesehatan RI, dan BMKG | Provinsi Jawa Tengah Tahun 2024</div>
    </div>
    """, unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # MODUL 1: DASHBOARD RINGKASAN EKSEKUTIF
    # --------------------------------------------------------------------------
    if menu == "🏛️ 1. Dashboard Ringkasan Eksekutif":
        st.subheader("📊 Ringkasan Indikator Utama Pembangunan Jawa Tengah 2024")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-label">Rata-rata Kemiskinan</div>
                <div class="metric-value">{df['persentase_penduduk_miskin'].mean():.2f}%</div>
                <div class="metric-delta delta-good">📉 Median: {df['persentase_penduduk_miskin'].median():.2f}%</div>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown(f"""
            <div class="metric-box" style="border-top-color: #059669;">
                <div class="metric-label">Prevalensi Stunting</div>
                <div class="metric-value">{df['prevalensi_stunting'].mean():.2f}%</div>
                <div class="metric-delta delta-good">👶 Target Nasional: <14%</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="metric-box" style="border-top-color: #D97706;">
                <div class="metric-label">Rata-rata IPM</div>
                <div class="metric-value">{df['ipm'].mean():.2f}</div>
                <div class="metric-delta delta-good">🎓 Kategori Tinggi</div>
            </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
            <div class="metric-box" style="border-top-color: #7C3AED;">
                <div class="metric-label">Total Puskesmas</div>
                <div class="metric-value">{int(df['jumlah_puskesmas'].sum())} Unit</div>
                <div class="metric-delta delta-good">🏥 Rawat Inap & Non-Inap</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("📋 Matriks Profil Indikator 35 Kabupaten/Kota Jawa Tengah 2024")
        
        col_search, col_filter = st.columns([2, 1])
        with col_search:
            search_txt = st.text_input("🔍 Cari Nama Kabupaten/Kota:", "")
        with col_filter:
            selected_type = st.selectbox("Filter Tipe Wilayah:", ["Seluruh Wilayah", "Kabupaten", "Kota"])

        df_filtered = df.copy()
        if selected_type == "Kabupaten":
            df_filtered = df_filtered[~df_filtered["kabupaten_kota"].str.startswith("Kota")]
        elif selected_type == "Kota":
            df_filtered = df_filtered[df_filtered["kabupaten_kota"].str.startswith("Kota")]

        if search_txt:
            df_filtered = df_filtered[df_filtered["kabupaten_kota"].str.contains(search_txt, case=False)]

        st.dataframe(
            df_filtered.style.highlight_max(axis=0, color="#DCFCE7", subset=["ipm", "akses_sanitasi_layak", "akses_air_minum_layak", "jumlah_puskesmas"])
                             .highlight_min(axis=0, color="#FEE2E2", subset=["persentase_penduduk_miskin", "prevalensi_stunting"]),
            use_container_width=True,
            height=450
        )

    # --------------------------------------------------------------------------
    # MODUL 2: PETA SPASIAL & CLUSTERING
    # --------------------------------------------------------------------------
    elif menu == "🗺️ 2. Peta Spasial & Clustering Wilayah":
        st.subheader("🗺️ Pemetaan Tipologi Spasial Risiko Kemiskinan & Stunting (35 Wilayah)")
        st.write("Peta di bawah ini menampilkan distribusi spasial 35 Kabupaten/Kota berdasarkan klasifikasi status kemiskinan dan indikator kesehatan.")

        coords_jateng = {
            3301: (-7.7279, 109.0060), 3302: (-7.4646, 109.1764), 3303: (-7.3879, 109.3639),
            3304: (-7.3797, 109.6974), 3305: (-7.6706, 109.6600), 3306: (-7.7161, 109.9990),
            3307: (-7.3633, 109.9009), 3308: (-7.4313, 110.2175), 3309: (-7.5360, 110.5959),
            3310: (-7.7058, 110.6019), 3311: (-7.6811, 110.8340), 3312: (-7.8136, 110.9255),
            3313: (-7.6256, 111.0505), 3314: (-7.4277, 110.9351), 3315: (-7.0877, 110.9161),
            3316: (-7.0706, 111.4173), 3317: (-6.7093, 111.3414), 3318: (-6.7548, 111.0381),
            3319: (-6.8048, 110.8405), 3320: (-6.5891, 110.6685), 3321: (-6.8943, 110.6386),
            3322: (-7.2008, 110.4395), 3323: (-7.3168, 110.1691), 3324: (-7.0253, 110.2057),
            3325: (-7.0149, 109.8492), 3326: (-7.0250, 109.6053), 3327: (-7.0425, 109.4319),
            3328: (-7.0287, 109.1415), 3329: (-7.0016, 108.9702), 3371: (-7.4706, 110.2178),
            3372: (-7.5755, 110.8243), 3373: (-7.3305, 110.5084), 3374: (-6.9667, 110.4167),
            3375: (-6.8886, 109.6753), 3376: (-6.8671, 109.1378)
        }

        def get_lat_lon(kw):
            try:
                code_int = int(round(float(kw) * 100))
            except:
                code_int = 0
            return coords_jateng.get(code_int, (-7.1501, 110.1403))

        df['lat'] = df['kode_wilayah'].map(lambda k: get_lat_lon(k)[0])
        df['lon'] = df['kode_wilayah'].map(lambda k: get_lat_lon(k)[1])

        median_p = df['persentase_penduduk_miskin'].median()
        df['Status_Kemiskinan'] = df['persentase_penduduk_miskin'].apply(lambda x: 'Kemiskinan Tinggi' if x >= median_p else 'Kemiskinan Rendah')

        m = folium.Map(location=[-7.1501, 110.1403], zoom_start=8, tiles='OpenStreetMap')
        
        for _, row in df.iterrows():
            color = '#DC2626' if row['Status_Kemiskinan'] == 'Kemiskinan Tinggi' else '#059669'
            popup_txt = f"""
            <div style="font-family: Arial; font-size: 12px; width: 220px;">
                <b style="color: #0F172A; font-size: 14px;">{row['kabupaten_kota']}</b><br>
                <hr style="margin: 4px 0;">
                <b>Status:</b> <span style="color: {color}; font-weight: bold;">{row['Status_Kemiskinan']}</span><br>
                <b>Kemiskinan:</b> {row['persentase_penduduk_miskin']}%<br>
                <b>Stunting:</b> {row['prevalensi_stunting']}%<br>
                <b>IPM:</b> {row['ipm']}<br>
                <b>Puskesmas:</b> {row['jumlah_puskesmas']} Unit
            </div>
            """
            folium.CircleMarker(
                location=[row['lat'], row['lon']],
                radius=10, color=color, fill=True, fill_opacity=0.85,
                popup=folium.Popup(popup_txt, max_width=280)
            ).add_to(m)

        st_folium(m, width=1150, height=530)
        
        # High contrast map legend caption
        st.markdown("""
        <div class="map-legend-caption">
            🔴 <b style="color: #DC2626;">Merah</b>: Wilayah Kemiskinan Tinggi (≥ Median 9.63%) &nbsp;|&nbsp; 
            🟢 <b style="color: #059669;">Hijau</b>: Wilayah Kemiskinan Rendah (&lt; Median 9.63%)
        </div>
        """, unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # MODUL 3: SIMULASI PREDIKSI & INTERVENSI KEBIJAKAN
    # --------------------------------------------------------------------------
    elif menu == "💡 3. Simulasi Prediksi & Intervensi Kebijakan":
        st.subheader("💡 Simulator Intervensi Kebijakan Berbasis Machine Learning")
        st.write("Gunakan pengontrol di bawah ini untuk mensimulasikan perubahan indikator daerah secara real-time.")

        col_left, col_right = st.columns([1, 1])

        with col_left:
            st.markdown("### 🎛️ Input Parameter Indikator Daerah")
            stunting_in = st.slider("Prevalensi Stunting Balita (%)", 0.0, 30.0, 10.0, 0.1)
            ipm_in = st.slider("Indeks Pembangunan Manusia (IPM)", 60.0, 90.0, 74.5, 0.1)
            pengeluaran_in = st.number_input("Rata-rata Pengeluaran per Kapita (Rp/bulan)", 500000, 3000000, 1250000, step=10000)
            sanitasi_in = st.slider("Akses Sanitasi Layak (%)", 40.0, 100.0, 85.0, 0.5)
            air_in = st.slider("Akses Air Minum Layak (%)", 50.0, 100.0, 95.0, 0.5)
            puskesmas_in = st.number_input("Jumlah Puskesmas (Unit Data Mentah)", 1, 50, 18)
            hujan_in = st.number_input("Curah Hujan Tahunan (mm)", 1000, 5000, 2500, step=50)

        with col_right:
            st.markdown("### 🎯 Hasil Prediksi Model ML (IRAS)")
            
            # Safe input dictionary containing ALL possible predictor keys
            log_ipm = np.log1p(ipm_in)
            log_pengeluaran = np.log1p(pengeluaran_in)
            log_sanitasi = np.log1p(sanitasi_in)
            log_air = np.log1p(air_in)

            input_dict = {
                "prevalensi_stunting": stunting_in,
                "log_ipm": log_ipm,
                "log_pengeluaran_per_kapita": log_pengeluaran,
                "log_akses_sanitasi_layak": log_sanitasi,
                "log_akses_air_minum_layak": log_air,
                "jumlah_puskesmas": puskesmas_in,
                "curah_hujan_tahunan": hujan_in
            }
            
            # Filter dynamically to match exact feature list of loaded model
            input_data = pd.DataFrame([input_dict])[features]

            input_scaled = scaler.transform(input_data)
            pred_class = model.predict(input_scaled)[0]
            pred_proba = model.predict_proba(input_scaled)[0][1] if hasattr(model, "predict_proba") else 0.5

            if pred_class == 1:
                st.error(f"⚠️ **STATUS RISIKO: WILAYAH KEMISKINAN TINGGI** (Probabilitas: {pred_proba*100:.1f}%)")
                st.warning("""
                **📌 Rekomendasi Prioritas Intervensi Pemprov Jateng:**
                1. **Perluasan Jaringan Air Minum Layak**: Tingkatkan akses air bersih di permukiman padat & perdesaan (Variabel Determinan #1).
                2. **Program Akselerasi Penanganan Stunting**: Alokasikan bantuan gizi spesifik & sensitif di wilayah prioritas.
                3. **Peningkatan Kapasitas Puskesmas**: Tambah ketersediaan tenaga kesehatan dan peralatan medis dasar di unit Puskesmas.
                """)
            else:
                st.success(f"✅ **STATUS RISIKO: WILAYAH KEMISKINAN RENDAH** (Probabilitas Risiko: {pred_proba*100:.1f}%)")
                st.info("""
                **📌 Rekomendasi Pemeliharaan & Penguatan:**
                1. Pertahankan cakupan air minum & sanitasi layak di atas 95%.
                2. Tingkatkan pemerataan layanan kesehatan Puskesmas di wilayah rural.
                """)

    # Footer
    st.markdown("""
    <div class="gov-footer">
        © 2024 Pemerintah Provinsi Jawa Tengah | Intelligent Regional Analytics System (IRAS)<br>
        Dikembangkan untuk Ujian Akhir Semester (UAS) MPML - Statistika UII (NIM: 24611028)
    </div>
    """, unsafe_allow_html=True)
