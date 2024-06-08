import streamlit as st
import pandas as pd
from tabulate import tabulate

df = pd.read_csv('output_dataset.csv')  


def main():
    st.title('Subtheme Sentiment Finder')

    review_texts = df['review_text'].unique().tolist()

    review_texts.insert(0, "")

    selected_review_text = st.selectbox('List of text present in the dataset:', review_texts, format_func=lambda x: 'Select Any Text' if x == '' else x)

    if st.button('Find') and selected_review_text != "":
    
        subtheme_sentiments_pred = df.loc[df['review_text'] == selected_review_text, 'subtheme_sentiments_pred'].iloc[0]
        

        st.write(f'Subtheme Sentiments Prediction: {subtheme_sentiments_pred}')

if __name__ == '__main__':
    main()
