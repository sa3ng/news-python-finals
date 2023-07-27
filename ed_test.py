from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import streamlit as st
import requests

API_KEY = 'b8da9753d86045fab4baa56f365cc09b'
NEWS_API_TOP_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines/'


def summarize_html(url: str, sentences_count: int, language: str = 'english') -> str:
    """
    Summarizes text from URL

    Inputs
    ----------
    url: URL for full text
    sentences_count: specifies max number of sentences for return value
    language: specifies language of text

    Return
    ----------
    summary of text from URL
    """
    parser = HtmlParser.from_url(url, Tokenizer(language))
    stemmer = Stemmer(language)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(language)

    summary = ''
    for sentence in summarizer(parser.document, sentences_count):
        if not summary:
            summary += str(sentence)
        else:
            summary += ' ' + str(sentence)

    return summary


def news_api_request(url: str, **kwargs) -> list:
    """
    Sends GET request to News API endpoint

    Inputs
    ----------
    url: full URL for endpoint
    kwargs: please refer to 
            News API documentations: 
            https://newsapi.org/docs/endpoints/
            (apiKey argument is required)

    Return
    ----------
    list containing data for each article in response
    """
    params = kwargs
    res = requests.get(url, params=params)
    articles = res.json().get('articles')
    return articles


def summarize_news_api(articles: list, sentences_count: int) -> list:
    """
    summarizes text at URL for each element of articles dict 
    (return value from news_api_request) and adds a new element 
    articles dict where the key is 'summary' and the value is 
    the summarized text

    Inputs
    ----------
    articles: list of dict returned from news_api_request()
    sentences_count: specifies max number of sentences for 
                     return value

    Return
    ----------
    articles list with summary element added to each dict
    """
    for article in articles:
        summary = summarize_html(article.get('url'), sentences_count)
        article.update({'summary': summary})

    return articles


def main() -> None:
    articles = news_api_request(
        NEWS_API_TOP_HEADLINES_URL, apiKey=API_KEY, sortBy='publishedAt', country='ph')
    summaries = summarize_news_api(articles, 10)
    print(summaries[0])
    st.title('News Summarizer')


if __name__ == "__main__":
    main()
