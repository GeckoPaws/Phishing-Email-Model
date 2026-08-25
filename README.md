# Phishing-Email-Model
Phishing classification model 

# Purpose
This is a classification model I am building to identify potential phishing emails vs non-phishing emails. This program uses Pandas and SciKit Learn. Pandas for reading and formatting the training data and SciKit Learn to create and train the classification model. 

# Regarding Data Set Training
I have rotated between a couple of data sets to train the model, but for now I think I will settle with the dataset I found on Hugging Face. I have included some data sets I found from Kaggle, but they are not exclusively phishing emails. Some are just spam or suspicious emails. The CSVs included in this repo have been formatted for use in this program.

# Goals
The goal is to have a website where this program will run in the background. The user can paste an email they thing is phishing and the program will return whether it thinks it is phishing or not phishing. 

Im still trying to figure out how to get the model to identify emails better. The predictions are not always correct, and even if they are correct, the confidence level may not be that high. The next goal I have is to make the detector print what it thought was an indicator of phishing in the email. This will help users to understand why their email may be suspicious. I also hope this feature can point out words that may be causing the model to give false positive or false negatives.

# Regarding Use Of Code
Feel free to download and edit parts of this if you like. You can use it how you like as well. This is just a project I thought would be cool to make to gain some practical experience.
