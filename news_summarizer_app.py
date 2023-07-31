import os
from app_functions import get_top_headlines, search_articles
import streamlit as st
#-----declare imports here

#Preloading
with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

#News API key - Sa3ng
API_KEY = "4a579d60db244444b74cf8fc149f8d64"

st.title('News Summarizer')

#Sidebar
search_choice = st.sidebar.radio('', options=['Top Headlines', 'Search Term'])
sentences_count = 3

if search_choice == 'Top Headlines':
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


elif search_choice == 'Search Term':
    search_term = st.sidebar.text_input('Enter Search Term:')

    if not search_term:
        summaries = []
        st.write('Please enter a search term =)')
    else:
        summaries = search_articles(sentences_count, apiKey=API_KEY, 
                                                     sortBy='publishedAt', 
                                                     q=search_term)

#main body - main page
for i in range(len(summaries)):
    st.title(summaries[i]['title'])
    st.write(f"published at: {summaries[i]['publishedAt']}")
    st.write(f"source: {summaries[i]['source']['name']}")
    st.write(summaries[i]['summary'])