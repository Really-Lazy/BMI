import streamlit as st

st.set_page_config(layout="wide")

# ตั้งค่าภาพพื้นหลัง
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://i.ytimg.com/vi/rtrld-X-1Jc/maxresdefault.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("BMI Calculator")

# เลือกเพศ
gender = st.radio("Select Gender", ["Male", "Female"], horizontal=True)

# ป้อนน้ำหนักและส่วนสูง
weight = st.slider("Select your weight (kg)", min_value=1, max_value=200, step=1)
height = st.slider("Select your height (cm)", min_value=50, max_value=250, step=1)

# คำนวณ BMI
height_m = height / 100
bmi = weight / (height_m ** 2)

st.write(f"Your BMI is: **{bmi:.2f}**")

# สร้าง Dictionary สำหรับภาพตามเพศและช่วง BMI
image_dict = {
    "Male": {
        "Underweight": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3CG7imwrCJOBkOwirUxpnurFslmRA35Id-g&s.jpg",
        "Normal": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9xU86Z4LOEApQKFAZ6zq0VYx7DDZepoEKyA&s.jpg",
        "Overweight": "https://pbs.twimg.com/media/FpvY5StXEAAqYZH?format=jpg&name=4096x4096",
        "Obese": "https://static1.srcdn.com/wordpress/wp-content/uploads/2024/12/rin-getting-angry.jpg",
        "Extremely Obese": "https://static0.gamerantimages.com/wordpress/wp-content/uploads/2024/12/rin-mad-2.jpg"
    },
    "Female": {
        "Underweight": "https://thumbs.dreamstime.com/z/too-thin-woman-anorexia-model-2814892.jpg",
        "Normal": "https://static.vecteezy.com/system/resources/thumbnails/036/095/205/small/ai-generated-beautiful-anime-girl-photo.jpg",
        "Overweight": "https://i.pinimg.com/736x/99/c1/22/99c1224a119194497c9496b690843f98.jpg",
        "Obese": "https://pics.craiyon.com/2024-09-05/zv7qTm3WRhiPav2qRStvXA.webp",
        "Extremely Obese": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJFhTEUBEmhtZymPGaUd7CEPqwKisi6izjkg&s"
    }
}

# ประเมินค่า BMI และแสดงภาพตามเพศและช่วง BMI
if bmi < 18.5:
    category = "Underweight"
    st.warning(category)
    st.image(image_dict[gender]["Underweight"], use_column_width=False, width=150)  # กำหนดขนาดภาพที่เล็กลง
elif 18.5 <= bmi < 24.9:
    category = "Normal"
    st.success("Normal weight")
    st.image(image_dict[gender]["Normal"], use_column_width=False, width=150)  # กำหนดขนาดภาพที่เล็กลง
elif 25 <= bmi < 29.9:
    category = "Overweight"
    st.info(category)
    st.image(image_dict[gender]["Overweight"], use_column_width=False, width=150)  # กำหนดขนาดภาพที่เล็กลง
elif 30 <= bmi < 39.9:
    category = "Obese"
    st.error(category)
    st.image(image_dict[gender]["Obese"], use_column_width=False, width=150)  # กำหนดขนาดภาพที่เล็กลง
else:
    category = "Extremely Obese"
    st.error(category)
    st.image(image_dict[gender]["Extremely Obese"], use_column_width=False, width=150)  # กำหนดขนาดภาพที่เล็กลง
