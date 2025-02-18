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
    st.button("ไม่แสดงกราฟแท่ง")
else:
    st.button("ไม่แสดงกราฟแท่ง")

    import matplotlib.pyplot as plt

# Pie 
labels = 'sepal.width', 'sepal.length', 'petal.width', 'petal.length'
x1=df['sepal.width'].mean()
x2=df['sepal.length'].mean()
x3=df['petal.width'].mean()
x4=df['petal.length'].mean()
sizes = [x1, x2, x3, x4]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
#ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)

if(st.button("แสดงกราฟวงกลม")):
    st.pyplot(fig1)
    st.button("ไม่แสดงกราฟวงกลม")

else:
    st.button("ไม่แสดงกราฟวงกลม")
