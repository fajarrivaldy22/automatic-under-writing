from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predicts/<int:umur>/<int:sa>/<int:penyakit>/',views.predict_user,name="predict"),
    path('predicts_urine/<str:a>/<str:b>/<str:c>/<str:d>/<str:e>/<str:f>/<str:g>/<str:h>/',views.predict_urine,name="predict_urine"),
    path('predicts_blood/<str:a>/<str:b>/<str:c>/<str:d>/<str:e>/<str:f>/',views.predict_blood,name="preict_blood"),
    path('predicts_mass/',views.predicts_mass,name="predicts_mass"),
    #<str:bili>/<str:uro>/<str:keton>/<str:protein>/<str:nitrit>/<str:lekosit>/<str:glu>/<str:ph>/
    #<str:a>/<str:b>/<str:c>/<str:d>/<str:e>/<str:f>/
    #<str:a>/<str:b>/<str:c>/<str:d>/<str:e>/<str:f>/<str:g>/<str:h>/
]