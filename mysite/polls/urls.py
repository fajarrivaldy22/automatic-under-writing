from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predicts/<int:umur>/<int:sa>/<int:penyakit>/',views.predict_user,name="predict")
]