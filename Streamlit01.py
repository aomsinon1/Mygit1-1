import streamlit as st
import pandas as st
st.title("การทดสอบสร้างเว็บด้วยPython")
st.image("data.jpeg")
st.header("การนำเสนอข้อมูลกราฟด้วย Python")


col1, col2, col3 = st.columns(3)

with col1
   st.header("Versicolor")
   st.image("./img/1.jpg")
with col2
   st.header("Verginica")
   st.image(".img/2.jpg")

with col3
   st.header("Setosa")
   st.image(".img/3.jpg")

#import panda as pd 
df=pd.read_csv("./data/iris.csv")
st.write(df.head(10)