# %%
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, KFold, cross_val_score, GridSearchCV
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# %%
df = pd.read_csv("phishing_clean_normalized_for_comprehend.csv")

#print(df.head())   #test to make sure the csv file is correct
print(df.columns) #prints the names of the columns
#print(df['Text']) #prints only values in Text column
print(len(df)) #counts how many rows
print(df['CLASS'].value_counts()) #counts number of times each unique value appears in a column

df["CLASS"] = df["CLASS"].map({
    "phishing" : 1,
    "not phishing" : 0
})

vectorizer = TfidfVectorizer(stop_words="english") #This means ignore any super common english words in the text ("the", "and", "of", etc)

X = vectorizer.fit_transform(df["Text"]) #X holds all the inputs (dataset emails)
Y = df.CLASS #Y is a series that holds all the answers (phisning/not phishing)

#THIS LINE SPLITS THE DATA INTO TRAINING ADN TESTING DATA
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

#I need to create a model. this cretes a model object. then I will train it.
model = MultinomialNB()

# Hyperparameter grid to search over
param_grid = {
    "alpha": [0.1, 0.5, 1.0, 2.0, 5.0],
    "fit_prior": [True, False]
}


# 5-fold cross-validation hyperparameter search
grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5,              # 5-fold CV
    scoring="accuracy",# or "f1_macro", etc.
    n_jobs=-1,         # use all cores (optional)
    refit=True         # refit on full X_train with best params
)

grid_search.fit(X_train, Y_train) #fit means learn patterns from the given examples (training data). this is training the model using each cobination of the hyper-parameters.

print("Best params:", grid_search.best_params_)
print("Best CV score:", grid_search.best_score_)

# %%
# Declare my best model
best_model = grid_search.best_estimator_

# Predict on the held-out test set
predictions = best_model.predict(X_test)
test_score = best_model.score(X_test, Y_test)

# now I'll compare predictions to real answers
accuracy = accuracy_score(Y_test, predictions)
print(accuracy)

# Intentionally commented - used only as a learning reference
# model.fit(X_train, Y_train) #fit means learn patterns from the given examples (training data). this is training the model.
# predictions = model.predict(X_test) #now I want to see if the model can make correct predictions on never-before-seen emails

# now I'll compare predictions to real answers
# accuracy = accuracy_score(Y_test, predictions)
# print(accuracy)

############################################################################
# %%
#now we will get into the actual prpose of this program. Predicting whether inputed emails are phishing or not

email = input("paste your email here: \n")
email_vector = vectorizer.transform([email])

#this will store 1 or 0 depending on whether the email is determined to be phsihing or non-phishing
prediction = best_model.predict(email_vector)
probabilities = best_model.predict_proba(email_vector)
if prediction[0] == 1:
    print("Phishing.")

else:
    print("Not phishing.")

# %%
