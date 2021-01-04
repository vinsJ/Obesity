import pandas as pd
import requests

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# We need to get load our dataset with the rows we want to predict 

data = pd.read_csv('obesity.csv', encoding='UTF-8')

y = data.pop('NObeyesdad')

# Then, we'll put the data in the good form

def transfNumber(liste):
    listetransf=[]
    for i in range(len(liste)):
        if(liste[i]<=1.0):
            listetransf.append("1")
        elif((liste[i]>1) & (liste[i]<=2.0)):
            listetransf.append("2")
        elif((liste[i]>2) & (liste[i]<=3.0)):
            listetransf.append("3")
        else:
            listetransf.append("4")
    return listetransf

def tranFrequency(liste):
    listetransf=[]
    for i in range(len(liste)):
        if(liste[i]=="no"):
            listetransf.append("0")
        elif((liste[i]=="Sometimes")):
            listetransf.append("1")
        elif((liste[i]=="Frequently")):
            listetransf.append("2")
        else:
            listetransf.append("3")
    return listetransf

def dataPrep(obesity):
    obesity["FCVC"]=transfNumber(obesity["FCVC"])
    obesity["NCP"]=transfNumber(obesity["NCP"])
    obesity["CH2O"]=transfNumber(obesity["CH2O"])
    obesity["FAF"]=transfNumber(obesity["FAF"])
    obesity["TUE"]=transfNumber(obesity["TUE"])
    obesity['Age'] = round(obesity['Age']).astype(int)

    obesity = obesity.drop(['Height','Weight'],1)

    obesityP = obesity
    labelEncoder = LabelEncoder()

    obesityP['CAEC'] = labelEncoder.fit_transform(obesityP['CAEC'])
    obesityP['CALC'] = labelEncoder.fit_transform(obesityP['CALC'])

    data = pd.get_dummies(obesityP, columns=["Gender", "FAVC", "family_history_with_overweight", "SMOKE", "SCC", "MTRANS"], prefix=["Gender", "FAVC", "family", "SMOKE", "SCC", "MTRANS"] )

    return data

X = dataPrep(data)
# We can now send request to our API

host = 'localhost'
port= 42

try:
    res = requests.post('http://localhost:42/api/predict', json = X.to_json())
    result = res.json()

    print('Accuracy : ' + str(accuracy_score(y, result)))

    data['original'] = y
    data['predictions'] = result
    data.to_csv('obesity_predictions.csv', encoding = 'utf-8')

except Exception:
    print("An error has occured")