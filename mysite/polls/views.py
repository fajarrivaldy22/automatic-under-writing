from django.shortcuts import render
import os
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
import math

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

csv = open(os.path.dirname(os.path.realpath(__file__))+'//dataframe_urine.csv','r')
data= pd.read_csv(csv)
    
label = data.iloc[:,-1].values
data.head
data.drop(['eritrosit'],inplace=True,axis=1)

categorical_encoder = []
for i in range(len(data.columns)-1):
    le = preprocessing.LabelEncoder()
    categorical_encoder.append(le)
    categorical_encoder[i].fit(data.iloc[:,i])
    data.iloc[:,i] = categorical_encoder[i].transform(data.iloc[:,i])
kelas = data.iloc[:,0:len(data.columns)-1].values
neigh = KNeighborsClassifier(n_neighbors=1)

neigh.fit(kelas,label)

def predict_urine(request,a,b,c,d,e,f,g,h):
    

    bilirubin = a
    urobilin = b
    keton = c
    protein = d
    nirit = e
    leukosit = f
    gluskosa = g
    ph = h

    bahan_uji = []
    bahan_uji.append([bilirubin])
    bahan_uji.append([urobilin])
    bahan_uji.append([keton])
    bahan_uji.append([protein])
    bahan_uji.append([nirit])
    bahan_uji.append([leukosit])
    bahan_uji.append([gluskosa])
    bahan_uji.append([ph])

    encoded_categorical = []
    for i in range(len(categorical_encoder)):
        j = categorical_encoder[i].transform(bahan_uji[i])
        encoded_categorical.append(j[0])
    data_result = np.array(encoded_categorical)
    data_result = data_result.reshape(1, -1)

    predict = neigh.predict(data_result)
    probability = neigh.predict_proba(data_result)

    return HttpResponse(predict)


def predict_blood(request,a,b,c,d,e,f):
    csv = open(os.path.dirname(os.path.realpath(__file__))+'//dataframe_darah.csv','r')
    data = pd.read_csv(csv)
    label = data.iloc[:,-1].values
    data.head

    categorical_encoder = []
    for i in range(len(data.columns)-1):
        le = preprocessing.LabelEncoder()
        categorical_encoder.append(le)
        categorical_encoder[i].fit(data.iloc[:,i])
        data.iloc[:,i] = categorical_encoder[i].transform(data.iloc[:,i])
    
    kelas = data.iloc[:,0:len(data.columns)-1].values
    
    neigh = KNeighborsClassifier(n_neighbors=1)
    neigh.fit(kelas,label)

    hemogoblin = a
    hemaktorit = b
    leukosit = c
    trombosit = d
    led = e
    eritorsit = f

    bahan_uji = []
    bahan_uji.append([hemogoblin])
    bahan_uji.append([hemaktorit])
    bahan_uji.append([leukosit])
    bahan_uji.append([trombosit])
    bahan_uji.append([led])
    bahan_uji.append([eritorsit])

    encoded_categorical = []
    for i in range(len(categorical_encoder)):
        j = categorical_encoder[i].transform(bahan_uji[i])
        encoded_categorical.append(j[0])
    data_result = np.array(encoded_categorical)
    data_result = data_result.reshape(1, -1)
    
    predict = neigh.predict(data_result)

    return HttpResponse(predict)

def predicts_mass(request):
    if request.method == "POST":
        file = request.POST.get('fname','')
        return HttpResponse("heloo")
    