from django.shortcuts import render
import os
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
# Create your views here.
from django.http import HttpResponse


def index(request):
    

    x = 0


    return render(request,'index.html')

def detail(request):
    y = 6 + 6
    return HttpResponse(y)

def predict_user(request,umur,sa,penyakit):
    csv = open(os.path.dirname(os.path.realpath(__file__)) + '//dataframe.csv', "r")
    dataset = pd.read_csv(csv)
    dataset.head

    X = dataset.iloc[:, -1].values 
    Y = dataset.iloc[:, 0:len(dataset.columns)-1].values 


    labelencoder_X = LabelEncoder()
    labelencoder_X.fit(Y[:,0])
    Y[:,0] = labelencoder_X.transform(Y[:,0])

    neigh = KNeighborsClassifier(n_neighbors=3)
    neigh.fit(Y, X) 

    umu = umur
    umu = umu * 1000000
    up = sa
    penyaki = penyakit * 100000000

    predict = neigh.predict([[umu,up,penyaki]])
    proba = neigh.predict_proba([[umu,up,penyaki]])

    return HttpResponse(predict)
    