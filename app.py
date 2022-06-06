import pandas as pd
import streamlit as st
import re
import nltk


nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pickle

with open('model_pickle', 'rb') as f:
    model = pickle.load(f)  # loading the model_pickle file
data = pd.read_csv('sample_data.csv')
porterstemmer = PorterStemmer()


def clean_data(dataset):
    final_text = []
    for i in range(len(dataset)):
        text = re.sub('[^a-zA-Z]', ' ', str(dataset['Text'][i]))  # Negation of all the characters other than alphabets
        text = text.lower()  # converting the text into lower case
        text = text.split()  # splitting the words as a list
        text = [porterstemmer.stem(word) for word in text if word not in stopwords.words('english')]  # Applying stemmation
        text = ' '.join(text)  # joining the stemmed words to form a sentence
        final_text.append(text)

    for i in range(len(final_text)):
        dataset['Text'][i] = final_text[i]  # Replacing the text with the cleaned text

    return dataset


def main():
    html_temp = """
        <div style="background-color:aqua;padding:10px;">
        <h2 style="color:black;text-align:center;">Semantics Classifier</h2>
        </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.header('Classifying the semantics for reviews using Natural Language Processing')
    st.write('This app will identify the reviews where the semantics of review text does not match its rating.')
    st.write('Please upload a "csv" file with the below format and click on "View Result" button.')
    st.write(data.head())

    st.subheader("Please select a 'csv' file")
    filename = st.file_uploader("Upload", type="csv")
    if filename is not None:
        try:
            if st.button('View Result'):
                test_data = pd.read_csv(filename)
                copy_data = test_data.copy(deep=True)
                df_final = clean_data(dataset=test_data)
                X = df_final['Text'].values
                y_pred = model.predict(X)
                review_ID = []
                for i in range(len(y_pred)):
                    if ((y_pred[i] == 1) and (copy_data['Star'][i] == 1)):
                        review_ID.append(copy_data['ID'][i])
                result = copy_data[copy_data['ID'].isin(review_ID)]
                result.reset_index(inplace=True)
                result = result.iloc[:, 1:]
                st.subheader('Classified Reviews')
                st.write(result)
        except Exception as e:
            return st.write(e)


if __name__ == '__main__':
    main()
