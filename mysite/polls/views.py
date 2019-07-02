from django.shortcuts import render
import os
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
# Create your views here.
from django.http import HttpResponse


def index(request):
    csv = open(os.path.dirname(os.path.realpath(__file__)) + '//dataframe.csv', "r")
    dataset = pd.read_csv(csv)

    dataset.head

    X = dataset.iloc[:, -1].values 
    Y = dataset.iloc[:, 0:len(dataset.columns)-1].values 

    labelencoder_X = LabelEncoder()
    labelencoder_X.fit(Y[:,0])
    Y[:,0] = labelencoder_X.transform(Y[:,0])

    neigh = KNeighborsClassifier(n_neighbors=101)
    neigh.fit(Y, X) 

    umur = 1600
    up = 200000000 #umur

    predict = neigh.predict([[umur,up]])
    proba = neigh.predict_proba([[umur,up]])


    return render(request,'index.html',{
        'prediction':predict[0],
        'proba':proba,
    })

def detail(request,id):
    y = 6 + 6
    return HttpResponse(f"detail {id,y}")