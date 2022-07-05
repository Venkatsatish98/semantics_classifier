# semantics_classifier

There are times when a user writes Good, Nice App or any other positive text, in the review and gives 1-star rating. Your goal is to identify the reviews where the semantics of review text does not match rating. 

The goal is to identify such ratings where review text is good, but rating is negative- so that the support team can point this to users.

The dataset "chrome_reviews.csv" has been used in the project

The file "model_pickle" is the model which is selected by performing accuracy check on different machine learning classification algorithms.

## Deployment

This project has been deployed in heroku platform. please find the live link here https://semantics--analyser.herokuapp.com/


Install Git   https://git-scm.com/

Install heroku cli   https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli

1.Create heroku account

Run the following commands in the IDE terminal

2.git init (to initialize the git repository)

3.heroku login
-->enter the mail credentials

5.heroku create <app_name>  (give the app name without <,> )

6.git add .  (Adding all the files)

7.git commit -m "type any message"

8.git push heroku master


