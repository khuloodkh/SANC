# coding=utf8
# ---------------------------- Import libraries --------------------------------------#
# Preprossing function
from preprocessing import data_preprocessing
# pickle 
import pickle

# ----------------------------Classify function --------------------------------------#

def classify(user_input):
    # Define tfidf file path
    pickle_tfidf = "static/pickle_tfidf.pkl"
    # Define model file path
    pickle_model = "static/pickle_model.pkl"
    # Load the tfidf
    loaded_tfidf = pickle.load(open(pickle_tfidf, 'rb'))
    # Load the model
    loaded_model = pickle.load(open(pickle_model, 'rb'))
    # Preprocessing the user input
    pre_user_input = data_preprocessing(user_input)
    # Transform the preprocessed user input
    user_input_tfidf = loaded_tfidf.transform([pre_user_input])
    # Predict the topic
    predictions = loaded_model.predict(user_input_tfidf)
    # Return the prediction
    return predictions