import streamlit
import pandas 
import requests
import snowflake.connector

#streamlit.title("🍞 My Parent's Healthy Dinner") 
#streamlit.header('🥗 Breakfast Menu')
#streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
#streamlit.text('🐔 Kale, Spinach & Rocket Smoothie')
#streamlit.text('🥑 Hard-Boiled Free-Range Egg')
#streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#my_fruit_list = my_fruit_list.set_index('Fruit')
#selected_fruit=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Grapes', 'Lemon']) 
#to_show=my_fruit_list.loc[selected_fruit]
#streamlit.dataframe(to_show)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# write your own comment -what does the next line do? 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
#streamlit.dataframe(fruityvice_normalized)

#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#streamlit.write('The user entered ', fruit_choice)

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)

# streamlit_app.py
import streamlit as st

# Initialize connection.
my_cnx =  snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
def get_dataframe(table_name):
    query = f"SELECT * FROM {table_name}"
    my_cur.execute(query)
    data = my_cur.fetchall()
    df = pandas.DataFrame(data, columns=[i[0] for i in my_cur.description])
    return df
data=get_dataframe("MYTABLE") 
streamlit.dataframe(data) 
