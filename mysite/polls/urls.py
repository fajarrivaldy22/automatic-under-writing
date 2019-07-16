from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predicts/<int:umur>/<int:sa>/<int:penyakit>/',views.predict_user,name="predict"),
    path('predicts_urine/',views.predict_urine,name="predict_urine"),
    path('predicts_blood/',views.predict_blood,name="preict_blood")
    #<str:bili>/<str:uro>/<str:keton>/<str:protein>/<str:nitrit>/<str:lekosit>/<str:glu>/<str:ph>/
]