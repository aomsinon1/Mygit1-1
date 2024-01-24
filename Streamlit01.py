import streamlit as st
import pandas as pd
st.title("การทดสอบสร้างเว็บด้วยPython")
st.image("./img/rrr.jpg")
st.header("การนำเสนอข้อมูลกราฟด้วย Python")


col1, col2, col3 = st.columns(3)

with col1:
   st.header("Versicolor")
   st.image("./img/1.jpg")
with col2:
   st.header("Verginica")
   st.image("./img/2.jpg")

with col3:
   st.header("Setosa")
   st.image("./img/3.jpg")

#import panda as pd 
df=pd.read_csv("./data/iris.csv")
st.write(df.head(10))

if(st.button("แสดงข้อมูลตัวอย่าง")):
   st.write(df.head(10))
   st.button("ไม่แสดงตัวอย่าง")
else:
    st.button("ไม่แสดงข้อมูลตัวอย่าง")


if(st.button("แสดงกราฟแท่ง")):
    chart_data = pd.DataFrame(
    {
        "ประเภทดอกไม้": df['variety'],
        "ความกว้าง": df['sepal.width'],
        "ความยาว": df['sepal.length']    
        }
    )
    st.bar_chart(chart_data, x="ประเภทดอกไม้", y=["ความกว้าง","ความยาว"], color=["#FF0000", "#0000FF"])
    st.button("ไม่แสดงข้อมูลสถิติ")
else:
    st.button("ไม่แสดงข้อมูลสถิติ")
