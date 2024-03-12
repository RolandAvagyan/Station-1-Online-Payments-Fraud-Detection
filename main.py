import pandas as pd
import plotly.express as px
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv("PS_20174392719_1491204439457_log.csv", nrows=10000)
fig = px.pie(data, names='type', title='Transaction Types')
fig.show()

X = pd.get_dummies(data.drop(columns=['isFraud']))
Y = data['isFraud']

model = DecisionTreeClassifier()

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, train_size=0.2, random_state=42)

model.fit(X_train, Y_train)
predictions = model.predict(X_test)
score = accuracy_score(Y_test, predictions)

print(score)
