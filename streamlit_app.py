import streamlit
import pandas 
streamlit.title("🍞 My Parent's Healthy Dinner") 
streamlit.header('🥗 Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑 Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
selected_fruit=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Grapes', 'Lemon']) 
to_show=my_fruit_list.loc[selected_fruit]
streamlit.dataframe(to_show)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
