from unicodedata import name
from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from mdp.models import SaveDiabetesEnquiry,SaveHeartEnquiry,SavePerkinsonEnquiry,SaveStrokeEnquiry,SaveLungCancerEnquiry
from django.contrib.auth import  authenticate, login, logout
import joblib
import pickle
import numpy as np
import pandas as pd
#from dennisivy
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def home(request): 
    return render(request,"index.html")

def diabetes_parameter(request):
    
    d1 = request.POST.get("Pregnancies")
    d2 = request.POST.get("Glucose")
    d3 = request.POST.get("bp")
    d4 = request.POST.get("st")
    d5 = request.POST.get("Insulin")
    d6 = request.POST.get("bmi")
    d7 = request.POST.get("dpf")
    d8 = request.POST.get("age")
    
    return render(request,"diabetes.html",{'d1':d1,'d2':d2,'d3':d3,'d4':d4,'d5':d5,'d6': d6,'d7': d7,'d8': d8})
def heartDisease(request):
    return render(request,"heart disease.html")
def perkinson(request):
    return render(request,"parkinson.html")
def brainStroke(request):
    return render(request,"br_stroke.html")
def lungCancer(request):
    return render(request,"lung_cancer.html")

def showResultOfDiabetes(request):
    #deployment of sav model
    cls = joblib.load('sav model/diabetes_model.sav')
    list=[]
    list.append(request.POST.get('Pregnancies'))
    list.append(request.POST.get('Glucose'))
    list.append(request.POST.get('bp'))
    list.append(request.POST.get('st'))
    list.append(request.POST.get('Insulin'))
    list.append(request.POST.get('bmi'))
    list.append(request.POST.get('dpf'))
    list.append(request.POST.get('age'))
    print(list)
    ans = cls.predict([list])

    #save data into model
    pregnancies = (request.POST.get('Pregnancies'))
    glucose = (request.POST.get('Glucose'))
    bp = (request.POST.get('bp'))
    st = (request.POST.get('st'))
    insulin = (request.POST.get('Insulin'))
    bmi = (request.POST.get('bmi'))
    dpf = (request.POST.get('dpf'))
    age = (request.POST.get('age'))
    en = SaveDiabetesEnquiry(pregnancies = pregnancies, glucose = glucose,bp=bp,st = st, insulin= insulin,bmi = bmi,dpf =dpf, age= age)
    en.save()
    return render(request,'diabetes_result.html',{'ans':ans})

def showResultOfHeart(request):
    #deployment of sav model or dataset
    cls = joblib.load('sav model/heart_disease_model.sav')
    list=[]
    list.append(request.POST.get('age'))
    list.append(request.POST.get('gender'))
    list.append(request.POST.get('cp'))
    list.append(request.POST.get('trestbps'))
    list.append(request.POST.get('chol'))
    list.append(request.POST.get('fbs'))
    list.append(request.POST.get('restecg'))
    list.append(request.POST.get('thalach'))
    list.append(request.POST.get('exang'))
    list.append(request.POST.get('oldpeak'))
    list.append(request.POST.get('slope'))
    list.append(request.POST.get('ca'))
    list.append(request.POST.get('thal'))
    # print(list)
    # b = np.array(list, dtype=float)
    # c = [float(i) for i in list] 
    # print(c)
    # print(ans)
    ans = cls.predict([list])

    #save data into model
    age=(request.POST.get('age'))
    gender=(request.POST.get('gender'))
    cp=(request.POST.get('cp'))
    trestbps=(request.POST.get('trestbps'))
    chol=(request.POST.get('chol'))
    fbs=(request.POST.get('fbs'))
    restecg=(request.POST.get('restecg'))
    thalach=(request.POST.get('thalach'))
    exang=(request.POST.get('exang'))
    oldpeak=(request.POST.get('oldpeak'))
    slope=(request.POST.get('slope'))
    ca=(request.POST.get('ca'))
    thal=(request.POST.get('thal'))
    en = SaveHeartEnquiry(age=age, gender=gender, cp=cp, trestbps=trestbps, chol=chol, fbs=fbs,restecg=restecg,thalach=thalach,exang=exang,oldpeak=oldpeak,slope=slope,ca= ca,thal=thal)
    en.save()

    return render(request,'heart_result.html',{'ans':ans})

def showResultOfPerkinson(request):
    #deployment of sav model
    cls = joblib.load('sav model/parkinson_model.sav')
    list=[]
    list.append(request.POST.get('fo'))
    list.append(request.POST.get('fi'))
    list.append(request.POST.get('Flo'))
    list.append(request.POST.get('Jitter_p'))
    list.append(request.POST.get('Jitter_a'))
    list.append(request.POST.get('RAP'))
    list.append(request.POST.get('PPQ'))
    list.append(request.POST.get('DDP'))
    list.append(request.POST.get('Shimmer'))
    list.append(request.POST.get('Shimmer_db'))
    list.append(request.POST.get('APQ3'))
    list.append(request.POST.get('APQ5'))
    list.append(request.POST.get('APQ'))
    list.append(request.POST.get('DDA'))
    list.append(request.POST.get('HNR'))
    list.append(request.POST.get('RPDE'))
    list.append(request.POST.get('DFA'))
    list.append(request.POST.get('spread1'))
    list.append(request.POST.get('spread2'))
    list.append(request.POST.get('D2'))
    list.append(request.POST.get('PPE'))
    ans = cls.predict([list])


    #save data into model
    fo=(request.POST.get('fo'))
    fi=(request.POST.get('fi'))
    Flo=(request.POST.get('Flo'))
    Jitter_p=(request.POST.get('Jitter_p'))
    Jitter_a=(request.POST.get('Jitter_a'))
    RAP=(request.POST.get('RAP'))
    PPQ=(request.POST.get('PPQ'))
    DDP=(request.POST.get('DDP'))
    Shimmer=(request.POST.get('Shimmer'))
    Shimmer_db=(request.POST.get('Shimmer_db'))
    APQ3=(request.POST.get('APQ3'))
    APQ5=(request.POST.get('APQ5'))
    APQ=(request.POST.get('APQ'))
    DDA=(request.POST.get('DDA'))
    HNR=(request.POST.get('HNR'))
    RPDE=(request.POST.get('RPDE'))
    DFA=(request.POST.get('DFA'))
    spread1=(request.POST.get('spread1'))
    spread2=(request.POST.get('spread2'))
    D2=(request.POST.get('D2'))
    PPE=(request.POST.get('PPE'))
    en = SavePerkinsonEnquiry(fo=fo, fi=fi, Flo=Flo, Jitter_p=Jitter_p, Jitter_a=Jitter_a, RAP=RAP,PPQ=PPQ,DDP=DDP,Shimmer=Shimmer,Shimmer_db=Shimmer_db,
                                APQ3=APQ3,APQ5=APQ5,APQ=APQ,DDA=DDA,HNR=HNR,RPDE=RPDE,DFA=DFA,spread1=spread1,spread2=spread2,D2=D2,PPE=PPE)
    en.save()

    return render(request,'parkinson.html',{'ans':ans}) 


def showResultOfBrainStroke(request):
    #deployment of sav model
    # cls = joblib.load('sav model/br_stroke_rf_model.pickle')
    # cls = pickle.load(open('sav model/br_stroke_rf_model.pickle', 'rb'))
    cls = joblib.load('sav model/BrainStroke_prediction_rf.sav')

    # list=[]
    # list.append(request.POST.get('age'))
    # list.append(request.POST.get('hypertension'))
    # list.append(request.POST.get('heart_disease'))
    # list.append(request.POST.get('avg_glucose_level'))
    # list.append(request.POST.get('bmi'))
    # list.append(request.POST.get('gender'))
    # list.append(request.POST.get('ever_married'))
    # list.append(request.POST.get('work_type'))
    # list.append(request.POST.get('Residence_type'))
    # list.append(request.POST.get('smoking_status'))
    # print(list)
    # X = np.array([[list]])

    age = (request.POST.get('age'))
    hypertension = (request.POST.get('hypertension'))
    heart_disease = (request.POST.get('heart_disease'))
    avg_glucose_level = (request.POST.get('avg_glucose_level'))
    bmi = (request.POST.get('bmi'))
    gender = (request.POST.get('gender'))
    married = (request.POST.get('married'))
    work_type = (request.POST.get('work_type'))
    residence_type = (request.POST.get('residence_type'))
    smoking_status = (request.POST.get('smoking_status'))
    # input_features = np.array([age, hypertension,heart_disease,avg_glucose_level,bmi,gender,married,work_type,residence_type,smoking_status])

    pred = cls.predict([[age, hypertension,heart_disease,avg_glucose_level,bmi,gender,married,work_type,residence_type,smoking_status]])
    ans = {
        'ans': pred[0]
    }

    #save data into model
    age = (request.POST.get('age'))
    hypertension = (request.POST.get('hypertension'))
    heart_disease = (request.POST.get('heart_disease'))
    avg_glucose_level = (request.POST.get('avg_glucose_level'))
    bmi = (request.POST.get('bmi'))
    gender = (request.POST.get('gender'))
    married = (request.POST.get('married'))
    work_type = (request.POST.get('work_type'))
    residence_type = (request.POST.get('residence_type'))
    smoking_status = (request.POST.get('smoking_status'))
    
    en = SaveStrokeEnquiry(age= age, hypertension =hypertension , heart_disease = heart_disease, avg_glucose_level = avg_glucose_level, 
                            bmi = bmi, gender = gender, married = married, work_type = work_type, residence_type = residence_type, 
                            smoking_status = smoking_status)
    en.save()
    return render(request,'br_stroke_result.html', ans)




def showResultOfLungCancer(request):
    #deployment of sav model
    cls = joblib.load('sav model/lung_ada_model.sav')
    list=[]
    list.append(request.POST.get('age'))
    list.append(request.POST.get('smoking'))
    list.append(request.POST.get('yellow_finger'))
    list.append(request.POST.get('anxiety'))
    list.append(request.POST.get('pressure'))
    list.append(request.POST.get('chronic_disease'))
    list.append(request.POST.get('fatigue'))
    list.append(request.POST.get('allergy'))
    list.append(request.POST.get('wheezing'))
    list.append(request.POST.get('alcohol_consuming'))
    list.append(request.POST.get('coughing'))
    list.append(request.POST.get('sob'))
    list.append(request.POST.get('swalling_difficulty'))
    list.append(request.POST.get('chest_pain'))
    ans = cls.predict([list])

    #save data into model
    age=(request.POST.get('age'))
    smoking=(request.POST.get('smoking'))
    yellow_fingers=(request.POST.get('yellow_finger'))
    anxiety=(request.POST.get('anxiety'))
    peer_pressure=(request.POST.get('pressure'))
    chronic_disease=(request.POST.get('chronic_disease'))
    fatigue=(request.POST.get('fatigue'))
    allergy=(request.POST.get('allergy'))
    wheezing=(request.POST.get('wheezing'))
    alcohol_consuming=(request.POST.get('alcohol_consuming'))
    coughing=(request.POST.get('coughing'))
    sob=(request.POST.get('sob'))
    swalling_difficulty=(request.POST.get('swalling_difficulty'))
    chest_pain=(request.POST.get('chest_pain'))
    en = SaveLungCancerEnquiry(age=age, smoking=smoking,yellow_fingers= yellow_fingers, anxiety= anxiety, peer_pressure= peer_pressure,
                         chronic_disease= chronic_disease, fatigue= fatigue, allergy= allergy, wheezing= wheezing, 
                         alcohol_consuming= alcohol_consuming, coughing= coughing, sob= sob, swalling_difficulty= swalling_difficulty, 
                         chest_pain= chest_pain )
    en.save()

    return render(request,'lung_cancer.html',{'ans':ans})








