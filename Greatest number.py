import streamlit as st

st.header("Greatest among 3 numbers")

num_1 = st.number_input("ENTER FIRST NUMBER")
num_2 = st.number_input("ENTER SECOND NUMBER")
num_3 = st.number_input("ENTER THIRD NUMBER")

m = max(num_1,num_2,num_3)
s = "The greatest amongst the three numbers is "+str(m)+"."

st.write(s)
