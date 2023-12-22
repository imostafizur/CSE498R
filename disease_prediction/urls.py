"""disease_prediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mdp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    # result page
    path("result1", views.showResultOfDiabetes, name="result1"),
    path("result2", views.showResultOfHeart, name="result2"),
    path("result3", views.showResultOfParkinson, name="result3"),
    path("result4", views.showResultOfBrainStroke, name="result4"),
    path("result5", views.showResultOfLungCancer, name="result5"),
    path("imaging", views.showResultOfImage, name="imaging"),
    # input page
    path("diabetes", views.diabetes_parameter, name="diabetes"),
    path("heart-disease/", views.heartDisease, name="heart-disease"),
    path("parkinson/", views.parkinson, name="parkinson"),
    path("brain-stroke/", views.brainStroke, name="brain-stroke"),
    path("lung-cancer/", views.lungCancer, name="lung-cancer"),
    path("tumor/", views.tumor, name="tumor"),
    path("malaria/", views.malaria, name="malaria"),
    path("pneumonia/", views.pneumonia, name="pneumonia"),
    path("oct/", views.oct, name="oct"),
    # Registration page
    path("login/", views.login_user, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.register_user, name="register"),
    # database page
    path("ui/", views.userInfo, name="ui"),
]
