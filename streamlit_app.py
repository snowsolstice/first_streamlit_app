import streamlit
import pandas as pd


my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


streamlit.title("my parents healthy diner 🥣 🥗 🐔 🥑🍞")

streamlit.header("I resent you for this")

streamlit.text("this is just html")

streamlit.dataframe(my_fruit_list)
