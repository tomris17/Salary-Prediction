import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Salary Prediction App", layout="centered")

st.title("Salary Prediction App")
st.write(
    "Bu uygulama, çalışanların deneyim yılı ve mesleki özelliklerine göre Gradient Boosting modeli ile maaş tahmini yapar."
)


@st.cache_resource
def load_model():
    return joblib.load("salary_prediction_model.pkl")


model = load_model()

st.subheader("Calisan Bilgilerini Giriniz:")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Yas (Age)", min_value=18, max_value=70, value=30)
    gender = st.selectbox("Cinsiyet (Gender)", ["Male", "Female"])
    education_level = st.selectbox(
        "Egitim Seviyesi (Education Level)",
        ["Bachelor's", "Master's", "PhD", "High School"],
    )

with col2:
    job_title = st.text_input("Unvan (Job Title)", "Software Engineer")
    years_of_experience = st.number_input(
        "Deneyim Yili (Years of Experience)", min_value=0.0, max_value=40.0, value=5.0
    )

if st.button("Maaşi Tahmin Et", type="primary"):
    # Model sadece Years of Experience ile egitildigi icin (veya uygun kolonlarla) tahmin adimi
    try:
        input_data = pd.DataFrame(
            {"Years of Experience": [years_of_experience]}
        )
        prediction = model.predict(input_data)
        st.success(f"Tahmin Edilen Yillik Maas: **${prediction[0]:,.2f}**")
    except Exception as e:
        st.error(f"Tahmin sirasinda bir hata olustu: {e}")