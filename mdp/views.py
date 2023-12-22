from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from mdp.models import (
    CreateUserForm,
    SaveDiabetesEnquiry,
    SaveHeartEnquiry,
    SaveParkinsonEnquiry,
    SaveStrokeEnquiry,
    SaveLungCancerEnquiry,
)
from django.contrib.auth import authenticate, login, logout
import joblib
import numpy as np
import os
from django.core.files.storage import FileSystemStorage
import keras
from PIL import Image

media = "media"

# Create your views here.


def home(request):
    return render(request, "index.html")


def diabetes_parameter(request):
    d1 = request.POST.get("Pregnancies")
    d2 = request.POST.get("Glucose")
    d3 = request.POST.get("bp")
    d4 = request.POST.get("st")
    d5 = request.POST.get("Insulin")
    d6 = request.POST.get("bmi")
    d7 = request.POST.get("dpf")
    d8 = request.POST.get("age")

    return render(
        request,
        "diabetes.html",
        {
            "d1": d1,
            "d2": d2,
            "d3": d3,
            "d4": d4,
            "d5": d5,
            "d6": d6,
            "d7": d7,
            "d8": d8,
        },
    )


def heartDisease(request):
    return render(request, "heart disease.html")


def parkinson(request):
    return render(request, "parkinson.html")


def brainStroke(request):
    return render(request, "br_stroke.html")


def lungCancer(request):
    return render(request, "lung_cancer.html")


def tumor(request):
    return render(request, "tumor.html")


def malaria(request):
    return render(request, "malaria.html")


def pneumonia(request):
    return render(request, "pneumonia.html")


def oct(request):
    return render(request, "oct.html")


def showResultOfDiabetes(request):
    # deployment of sav model
    cls = joblib.load("sav model/diabetes_model.sav")
    try:
        list = []
        list.append(request.POST.get("Pregnancies"))
        list.append(request.POST.get("Glucose"))
        list.append(request.POST.get("bp"))
        list.append(request.POST.get("st"))
        list.append(request.POST.get("Insulin"))
        list.append(request.POST.get("bmi"))
        list.append(request.POST.get("dpf"))
        list.append(request.POST.get("age"))
        print(list)
        ans = cls.predict([list])
        print(ans)

    except:
        print("An exception occurred")

    result = ""
    if ans == 0:
        result = "No Diabetes"
    else:
        result = "Diabetes"

    # save data into model
    pregnancies = request.POST.get("Pregnancies")
    glucose = request.POST.get("Glucose")
    bp = request.POST.get("bp")
    st = request.POST.get("st")
    insulin = request.POST.get("Insulin")
    bmi = request.POST.get("bmi")
    dpf = request.POST.get("dpf")
    age = request.POST.get("age")
    en = SaveDiabetesEnquiry(
        pregnancies=pregnancies,
        glucose=glucose,
        bp=bp,
        st=st,
        insulin=insulin,
        bmi=bmi,
        dpf=dpf,
        age=age,
        result=result,
    )
    en.save()
    return render(request, "diabetes_result.html", {"ans": ans})


def showResultOfHeart(request):
    # deployment of sav model or dataset
    cls = joblib.load("sav model/heart_model.sav")
    list = []
    list.append(request.POST.get("age"))
    list.append(request.POST.get("gender"))
    list.append(request.POST.get("cp"))
    list.append(request.POST.get("trestbps"))
    list.append(request.POST.get("chol"))
    list.append(request.POST.get("fbs"))
    list.append(request.POST.get("restecg"))
    list.append(request.POST.get("thalach"))
    list.append(request.POST.get("exang"))
    list.append(request.POST.get("oldpeak"))
    list.append(request.POST.get("slope"))
    list.append(request.POST.get("ca"))
    list.append(request.POST.get("thal"))
    print(list)

    ans = cls.predict([list])

    print(ans)

    result = ""
    if ans == 0:
        result = "No Heart Disease"
    else:
        result = "Heart Disease"

    # save data into model
    age = request.POST.get("age")
    gender = request.POST.get("gender")
    cp = request.POST.get("cp")
    trestbps = request.POST.get("trestbps")
    chol = request.POST.get("chol")
    fbs = request.POST.get("fbs")
    restecg = request.POST.get("restecg")
    thalach = request.POST.get("thalach")
    exang = request.POST.get("exang")
    oldpeak = request.POST.get("oldpeak")
    slope = request.POST.get("slope")
    ca = request.POST.get("ca")
    thal = request.POST.get("thal")
    en = SaveHeartEnquiry(
        age=age,
        gender=gender,
        cp=cp,
        trestbps=trestbps,
        chol=chol,
        fbs=fbs,
        restecg=restecg,
        thalach=thalach,
        exang=exang,
        oldpeak=oldpeak,
        slope=slope,
        ca=ca,
        thal=thal,
        result=result,
    )
    en.save()

    return render(request, "heart_result.html", {"ans": ans})


def showResultOfParkinson(request):
    # deployment of sav model
    cls = joblib.load("sav model/parkinsons_model.sav")

    fo = request.POST.get("fo")
    fhi = request.POST.get("fhi")
    flo = request.POST.get("flo")
    jitter_p = request.POST.get("jitter_p")
    jitter_a = request.POST.get("jitter_a")
    RAP = request.POST.get("RAP")
    PPQ = request.POST.get("PPQ")
    DDP = request.POST.get("DDP")
    shimmer = request.POST.get("shimmer")
    shimmer_db = request.POST.get("shimmer_db")
    APQ3 = request.POST.get("APQ3")
    APQ5 = request.POST.get("APQ5")
    APQ = request.POST.get("APQ")
    DDA = request.POST.get("DDA")
    NHR = request.POST.get("NHR")
    HNR = request.POST.get("HNR")
    RPDE = request.POST.get("RPDE")
    DFA = request.POST.get("DFA")
    spread1 = request.POST.get("spread1")
    spread2 = request.POST.get("spread2")
    D2 = request.POST.get("D2")
    PPE = request.POST.get("PPE")
    pred = cls.predict(
        [
            [
                fo,
                fhi,
                flo,
                jitter_p,
                jitter_a,
                RAP,
                PPQ,
                DDP,
                shimmer,
                shimmer_db,
                APQ3,
                APQ5,
                APQ,
                DDA,
                NHR,
                HNR,
                RPDE,
                DFA,
                spread1,
                spread2,
                D2,
                PPE,
            ]
        ]
    )
    ans = {"ans": pred[0]}

    result = ""
    if ans == 0:
        result = "No Parkinson"
    else:
        result = "Parkinson"

    # save data into model
    en = SaveParkinsonEnquiry(
        fo=fo,
        fhi=fhi,
        flo=flo,
        jitter_p=jitter_p,
        jitter_a=jitter_a,
        RAP=RAP,
        PPQ=PPQ,
        DDP=DDP,
        shimmer=shimmer,
        shimmer_db=shimmer_db,
        APQ3=APQ3,
        APQ5=APQ5,
        APQ=APQ,
        DDA=DDA,
        NHR=NHR,
        HNR=HNR,
        RPDE=RPDE,
        DFA=DFA,
        spread1=spread1,
        spread2=spread2,
        D2=D2,
        PPE=PPE,
        result=result,
    )
    en.save()

    return render(request, "parkinson_result.html", {"ans": ans})


def showResultOfBrainStroke(request):
    # deployment of sav model
    cls = joblib.load("sav model/BrainStroke_prediction_rf.sav")
    try:
        list = []
        list.append(request.POST.get("gender"))
        list.append(request.POST.get("age"))
        list.append(request.POST.get("hypertension"))
        list.append(request.POST.get("heart_disease"))
        list.append(request.POST.get("married"))
        list.append(request.POST.get("work_type"))
        list.append(request.POST.get("residence_type"))
        list.append(request.POST.get("avg_glucose_level"))
        list.append(request.POST.get("bmi"))
        list.append(request.POST.get("smoking_status"))
        print(list)
        ans = cls.predict([list])
        print(ans)

    except:
        print("An exception occurred")

    result = ""
    if ans == 0:
        result = "No Brain Stroke"
    else:
        result = "Have Stroke"

    # save data into model
    gender = request.POST.get("gender")
    age = request.POST.get("age")
    hypertension = request.POST.get("hypertension")
    heart_disease = request.POST.get("heart_disease")
    married = request.POST.get("married")
    work_type = request.POST.get("work_type")
    residence_type = request.POST.get("residence_type")
    avg_glucose_level = request.POST.get("avg_glucose_level")
    bmi = request.POST.get("bmi")
    smoking_status = request.POST.get("smoking_status")
    en = SaveStrokeEnquiry(
        gender=gender,
        age=age,
        hypertension=hypertension,
        heart_disease=heart_disease,
        married=married,
        work_type=work_type,
        residence_type=residence_type,
        avg_glucose_level=avg_glucose_level,
        bmi=bmi,
        smoking_status=smoking_status,
        result=result,
    )
    en.save()
    return render(request, "br_stroke_result.html", {"ans": ans})


def showResultOfLungCancer(request):
    # deployment of sav model
    cls = joblib.load("sav model/lung_ada_model.sav")

    age = request.POST.get("age")
    smoking = request.POST.get("smoking")
    yellow_fingers = request.POST.get("yellow_finger")
    anxiety = request.POST.get("anxiety")
    peer_pressure = request.POST.get("pressure")
    chronic_disease = request.POST.get("chronic_disease")
    fatigue = request.POST.get("fatigue")
    allergy = request.POST.get("allergy")
    wheezing = request.POST.get("wheezing")
    alcohol_consuming = request.POST.get("alcohol_consuming")
    coughing = request.POST.get("coughing")
    sob = request.POST.get("sob")
    swalling_difficulty = request.POST.get("swalling_difficulty")
    chest_pain = request.POST.get("chest_pain")

    ans = cls.predict(
        [
            [
                age,
                smoking,
                yellow_fingers,
                anxiety,
                peer_pressure,
                chronic_disease,
                fatigue,
                allergy,
                wheezing,
                alcohol_consuming,
                coughing,
                sob,
                swalling_difficulty,
                chest_pain,
            ]
        ]
    )

    result = ""
    if ans == 0:
        result = "No Lung Cancer"
    else:
        result = "Lung Cancer"

    # save data into model
    en = SaveLungCancerEnquiry(
        age=age,
        smoking=smoking,
        yellow_fingers=yellow_fingers,
        anxiety=anxiety,
        peer_pressure=peer_pressure,
        chronic_disease=chronic_disease,
        fatigue=fatigue,
        allergy=allergy,
        wheezing=wheezing,
        alcohol_consuming=alcohol_consuming,
        coughing=coughing,
        sob=sob,
        swalling_difficulty=swalling_difficulty,
        chest_pain=chest_pain,
        result=result,
    )
    en.save()

    return render(request, "lung_cancer_result.html", {"ans": ans})


# Medical Imaging Part
def makePrediction(path, model):
    print("File Path:", path, model)
    image = Image.open(path)
    image = image.resize((224, 224))  # , 224,224

    if len(np.array(image).shape) < 4:
        rgb_img = Image.new("RGB", image.size)
        rgb_img.paste(image)
    else:
        rgb_img = image

    rgb_img = np.array(rgb_img, dtype=np.float32)
    rgb_img = rgb_img.reshape(1, 224, 224, 3)

    prediction = model.predict(rgb_img)

    print("Prediction:", prediction)
    # if prediction > 0.5:  # yhat[0]
    #     print("Prediction: yes")
    # else:
    #     print("Prediction: no")

    return prediction


def showResultOfImage(request):
    if request.method == "POST":
        if "tumor" in request.FILES:
            f = request.FILES["tumor"]
            if f == "":
                err = "No files Selected"
                return render(request, "imaging_result.html", {"err": err})

            fss = FileSystemStorage()
            file = fss.save(f.name, f)
            file_url = fss.url(file)
            model = keras.models.load_model("models/brain_tumor.h5")
            tumorPred = makePrediction(os.path.join(media, file), model)

            # Perform logic based on the tumor prediction
            if tumorPred > 0.5:
                result = "Tumor detected."
            elif tumorPred < 0.5:
                result = "NO Tumor detected."
            else:
                result = ""

            return render(
                request, "imaging_result.html", {"result": result, "file_url": file_url}
            )

        elif "malaria" in request.FILES:
            f = request.FILES["malaria"]
            if f == "":
                err = "No files Selected"
                return render(request, "imaging_result.html", {"err": err})

            fss = FileSystemStorage()
            file = fss.save(f.name, f)
            file_url = fss.url(file)
            print(file_url)
            model = keras.models.load_model("models/malaria_resnet50.h5")
            malariaPred = makePrediction(os.path.join(media, file), model)

            # Perform logic based on the malaria prediction
            if malariaPred > 0.5:
                result = "Malaria detected."
            elif malariaPred < 0.5:
                result = "NO Malaria detected."
            else:
                result = ""

            return render(
                request, "imaging_result.html", {"result": result, "file_url": file_url}
            )

        elif "pneumonia" in request.FILES:
            f = request.FILES["pneumonia"]
            if f == "":
                err = "No files Selected"
                return render(request, "imaging_result.html", {"err": err})

            fss = FileSystemStorage()
            file = fss.save(f.name, f)
            file_url = fss.url(file)
            print(file_url)
            model = keras.models.load_model("models/Pneumonia.h5")
            PneumoniaPred = makePrediction(os.path.join(media, file), model)

            # Perform logic based on the malaria prediction
            if np.all(PneumoniaPred) > 0.5:
                result = "Pneumonia detected."
            elif np.all(PneumoniaPred) < 0.5:
                result = "NO Pneumonia detected."
            else:
                result = ""

            return render(
                request, "imaging_result.html", {"result": result, "file_url": file_url}
            )
        elif "oct" in request.FILES:
            f = request.FILES["oct"]
            if f == "":
                err = "No files Selected"
                return render(request, "imaging_result.html", {"err": err})

            fss = FileSystemStorage()
            file = fss.save(f.name, f)
            file_url = fss.url(file)
            print(file_url)
            model = keras.models.load_model("models/Pneumonia.h5")
            octPred = makePrediction(os.path.join(media, file), model)

            # Perform logic based on the malaria prediction
            if np.all(octPred) > 0.5:
                result = "Optical Issue is detected."
            elif np.all(octPred) < 0.5:
                result = "NO Optical Issue is detected."
            else:
                result = ""

            return render(
                request, "imaging_result.html", {"result": result, "file_url": file_url}
            )

        else:
            err = "No Images Selected"
            return render(request, "imaging_result.html", {"err": err})

    else:
        return render(request, "imaging_result.html")


# Registration, Login, logout and User Information


def register_user(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "register.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, "login.html")

    return render(request, "login.html")


def logoutUser(request):
    logout(request)
    return redirect("/login")


def userInfo(request):
    diabetesUserDetails = SaveDiabetesEnquiry.objects.all()
    heartDiseaseUserDetails = SaveHeartEnquiry.objects.all()
    parkinsonUserDetails = SaveParkinsonEnquiry.objects.all()
    brainStrokeUserDetails = SaveStrokeEnquiry.objects.all()
    lungCancerUserDeatails = SaveLungCancerEnquiry.objects.all()
    return render(
        request,
        "user_information.html",
        {
            "data1": diabetesUserDetails,
            "data2": heartDiseaseUserDetails,
            "data3": parkinsonUserDetails,
            "data4": brainStrokeUserDetails,
            "data5": lungCancerUserDeatails,
        },
    )
