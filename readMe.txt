Analysis of Obesity Data Set by Vincent DEBANDE and Ludovic CHEVALLIER, Engineer Students (M1) in Data Analysis and Artificial Intelligence at ESILV. 

In the Jupyter Notebook, you can find all our analysis of the data set and applied Machine Learning to predict if an individual from South America is suffering from some form of Weight disorder.
We used Random Forest and got an accuracy of 82%. 

Our model might not perform well on individual from other countries than South America because the habits of people and the culture are unique in every country !

In the API folder, you'll find an API designed with Flask : 

Open obesity.csv (please, do not remove any line but the first one) and add some lines to it. You'll find the structure of the data set in our Notebook or .pdf
You can also add lines from the original .csv (you can find it in DB)

Run the app.py in a terminal
Run API_client in another terminal. 

It'll save the result in obesity_predictions.csv and print the accuracy (it can be way higher than 82% because obesity.csv might have rows used to train the model !).

Please read the Notebook to understand our work. 

Feel free to leave a comment !
