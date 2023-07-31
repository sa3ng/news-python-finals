import os
from app_functions import get_top_headlines, search_articles
import streamlit as st
from streamlit_option_menu import option_menu
#-----declare imports here

#Preloading
with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

#News API key - Sa3ng
API_KEY = "4a579d60db244444b74cf8fc149f8d64"
st.title('HapoNS -  News Summarizer')


#navbar - option menu
def streamlit_menu():
    with st.sidebar:
        selected = option_menu(
            menu_title="Categories",  # required
            options=["General", "Entertainment", "Business", "Health", "Science", "Sports", "Technology"],  # required
            icons=["house", "emoji-sunglasses", "building", "capsule", "lightbulb-fill", "trophy", "cpu"],  # optional
            menu_icon="globe",  # optional
            default_index=0,  # optional
            styles = {
                "container": {
                    "font-family":"Century Gothic",
                    "font-weight":"bold"
                },
                "nav-link": {
                    "font-family":"Century Gothic"
                },
            }
        )
    return selected



selected = streamlit_menu()
# summaries = get_news_per_genre("General", API_KEY)

if selected == "General":
    summaries = get_top_headlines(5, API_KEY, 
                                                   sortBy='publishedAt', 
                                                   country='us', 
                                                   category= "General")
# if selected == "Entertainment":
#     summaries = get_news_per_genre("Entertainment", API_KEY)
# if selected == "Business":
#     summaries = get_news_per_genre("Business", API_KEY)    
# if selected == "Health":
#     summaries = get_news_per_genre("Health", API_KEY)    
# if selected == "Science":
#     summaries = get_news_per_genre("Science", API_KEY)    
# if selected == "Sports":
#     summaries = get_news_per_genre("Sports", API_KEY)    
# if selected == "Technology":
#     summaries = get_news_per_genre("Technology", API_KEY)    

#main body - main page\
try:
    for i in range(len(summaries)):
        st.title(summaries[i]['title'])
        st.write(f"published at: {summaries[i]['publishedAt']}")
        st.write(f"source: {summaries[i]['source']['name']}")
        st.write(summaries[i]['summary'])
except:
        st.write("========= END =========")