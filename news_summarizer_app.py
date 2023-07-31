import os
from app_functions import get_top_headlines, search_articles
import streamlit as st
from streamlit_option_menu import option_menu
#-----declare imports here

#News API key - Sa3ng
API_KEY = "4a579d60db244444b74cf8fc149f8d64"


st.title('HapoNS -  News Summarizer')

#navbar - option menu
def streamlit_menu():
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",  # required
            options=["Home", "Projects", "Contact"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
        )
    return selected



selected = streamlit_menu()

if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "Projects":
    st.title(f"You have selected {selected}")
if selected == "Contact":
    st.title(f"You have selected {selected}")



# #Sidebar
sentences_count = 5


category = st.sidebar.selectbox('Search By Category:', options=['business', 
                                                            'entertainment', 
                                                            'general', 
                                                            'health', 
                                                            'science', 
                                                            'sports', 
                                                            'technology'], index=2)
    
summaries = get_top_headlines(sentences_count, apiKey=API_KEY, 
                                                   sortBy='publishedAt', 
                                                   country='us', 
                                                   category=category)




#main body - main page\

for i in range(len(summaries)):
    st.title(summaries[i]['title'])
    st.write(f"published at: {summaries[i]['publishedAt']}")
    st.write(f"source: {summaries[i]['source']['name']}")
    st.write(summaries[i]['summary'])
