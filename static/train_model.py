
# ------------------------------ Import libraries --------------------------------------#

#import Pandas
import pandas as pd
# Vectorizers
from sklearn.feature_extraction.text import TfidfVectorizer
# model
from sklearn.model_selection import  train_test_split
from sklearn import svm
# Evaluation metric
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
# import preprossing function
from preprocessing import data_preprocessing
# import the pickle to Save the models 
import pickle

# -------------------------- prepare data for modeling --------------------#

# Read the data set from csv file
df=pd.read_csv('../datasets/dataset.csv')

# Cleand the articles column
df['article'] = df['article'].apply(lambda article: data_preprocessing(article))

# Determen the target and the predictor
y = df.cat_topic
X = df.article

# Convert them into data frame
X = pd.DataFrame(X)
y = pd.DataFrame(y)

# Split X and y to train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, shuffle=True, stratify=y, random_state=42)

# Initialize the TfidfVectorizer
vectorizer = TfidfVectorizer()
# Fit and transform the TfidfVectorizer for train data
data_train_tfidf = vectorizer.fit_transform(X_train.article)
# Transform the TfidfVectorizer for test data
data_test_tfidf = vectorizer.transform(X_test.article)
# Check the shape of train and test data 
print(f"Train TF-IDF shape: {data_train_tfidf.shape}")
print(f"Test TF-IDF shape: {data_test_tfidf.shape}")


#--------------------------- SVM MODEL ----------------------------------#
# Initialize the support Vector Machine
svm_model = svm.SVC()
# Fit SVM for train data
svm_model.fit(data_train_tfidf, y_train)
# Make predictions for train and test data
y_pred_train_svm = svm_model.predict(data_train_tfidf)
y_pred_test_svm = svm_model.predict(data_test_tfidf)
# Print the model accuracy score
print(f"Train Accuracy : {accuracy_score(y_train, y_pred_train_svm)}")
print(f"Test Accuracy  : {accuracy_score(y_test, y_pred_test_svm)}")


# Define tfidf path
filename_tfidf = "pickle_tfidf.pkl"
# Define svm model path
filename_model = "pickle_model.pkl" 

# save the tfidf vectorizer as a pickle file
pickle.dump(vectorizer, open(filename_tfidf, 'wb'))
# save the svm model as a pickle file
pickle.dump(svm_model, open(filename_model, 'wb'))
