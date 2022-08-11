import streamlit
import pandas #as pd -> Aliasing doesn't work for some reason!


streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado on Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Add the fruit list from snowflake's S3 bucket:
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#my_fruit_list = pd.read_csv(" https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Change the dataframe index to 'fruit' so the drop down list would behave in the app
my_fruit_list = my_fruit_list.set_index('Fruit')

# asking the streamlit library to display the above dataframe on the page:
streamlit.dataframe(my_fruit_list) 

# Let's put a pick list here so they can pick the fruit they want to include 
# pre-populate the list to set an example for the customer with 'Avocado', 'Strawberries']
# fruits_selected keeps the choices
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# asking the streamlit library to display the choices the customer made:
streamlit.dataframe(fruits_to_show)


# New section to display fruityvice fruit advice
import requests

streamlit.header('Fruityvice Fruit Advice')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")
# Improved this line below: streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
