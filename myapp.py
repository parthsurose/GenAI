import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


st.title("My first Streamlit App")
#st.write("Parth Surose")
st.write(":streamlit: Hello Parth,")    #:streamlit: for print emoji
st.text("Let Start")

name=st.text_input("Enter Name: ")
if st.button("Greet"):
    st.success(f"Hello, {name}")
    
    

#Creating charts using pandas and numpy

df = pd.DataFrame(np.random.randn(10,2),columns=['A','B'])

st.line_chart(df)
st.bar_chart(df)


# Sidebar, image, &video

st.sidebar.title("Navigation")
img="https://imgs.search.brave.com/7Z-C7t1vIykRcgUiIO-YSBREQUCYAtdQSE7MgjbDkr0/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzLzc3L2I3/L2IzLzc3YjdiMzg5/NTJjMTE5NjNlNjI1/NTg5NzY5NTdlYzUz/LmpwZw"
st.sidebar.image(img,caption="Image from web",use_container_width=True)
#this will display video in sidebar

vid="https://www.youtube.com/watch?v=-xlKTqivNlA&pp=ygUVaW5kIHZzIHBhayBoaWdobGlnaHRz"
st.video(vid)
st.caption("IND VS PAK")


#upload csv file
upload_csv= st.file_uploader("Upload a csv file",type="csv")
if upload_csv:
    df=pd.read_csv(upload_csv)
    st.dataframe(df) 
    

# Text and markdown formatting
st.header("This is a Header")
st.subheader("This is a Subheader")
st.markdown("*Bold*,* Italic*,* Code* [Link][http://streamlit.io]")
st.code("for i in range(5) print(i)", language="python")

#Input components
st.text_input("What is your name?")
st.text_area("Write something.....")
st.number_input("pick a number ",min_value=0,max_value=100)
st.slider("Choose a range ",0,100)
st.selectbox("Select a fruit",["Apple","Banana","Mango"])
st.multiselect("Choose toppings",["Cheese","Tomato","Olives"])
st.radio("Pick one",["Option A","Option B","Option C"])
st.checkbox("I agree to the items.")



#Matplotlib
df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\GenAI\gen_streamlit\UserData.csv")

# Clean column names
df.columns = df.columns.str.strip()

st.write("Columns:", df.columns)

fig, ax = plt.subplots()
ax.plot(df["Name"], df["Age"], 'o')

st.pyplot(fig)


