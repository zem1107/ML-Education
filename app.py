"""足の本数を入力すると、人か猫かを自動で判定して表示するアプリケーションです。"""

import streamlit as st

st.title("Human or cat ?")

n_legs = st.number_input("足の本数", value=0)

if n_legs == 2:
    animal = "人間"
elif n_legs == 4:
    animal = "猫"
else:
    animal = "不明"

st.write('判定 ', animal)