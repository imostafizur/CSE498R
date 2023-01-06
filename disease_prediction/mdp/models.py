from django.db import models

# Create your models here.
class SaveDiabetesEnquiry(models.Model):
    pregnancies = models.CharField(max_length=10)
    glucose = models.CharField(max_length=10)
    bp = models.CharField(max_length=10)
    st = models.CharField(max_length=10)
    insulin = models.CharField(max_length=10)
    bmi = models.CharField(max_length=10)
    dpf = models.CharField(max_length=10)
    age = models.CharField(max_length=10)

class SaveHeartEnquiry(models.Model):
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    cp=models.CharField(max_length=10)
    trestbps=models.CharField(max_length=10)
    chol= models.CharField(max_length=10)
    fbs=models.CharField(max_length=10)
    restecg=models.CharField(max_length=10)
    thalach=models.CharField(max_length=10)
    exang=models.CharField(max_length=10)
    oldpeak=models.CharField(max_length=10)
    slope=models.CharField(max_length=10)
    ca=models.CharField(max_length=10)
    thal=models.CharField(max_length=10)

class SavePerkinsonEnquiry(models.Model):
    Fo = models.CharField(max_length=10)
    Fhi = models.CharField(max_length=10)
    Flo = models.CharField(max_length=10)
    Jitter_p = models.CharField(max_length=10)
    Jitter_a = models.CharField(max_length=10)
    RAP = models.CharField(max_length=10)
    PPQ = models.CharField(max_length=10)
    DDP = models.CharField(max_length=10)
    Shimmer = models.CharField(max_length=10)
    Shimmer_db = models.CharField(max_length=10)
    APQ3 = models.CharField(max_length=10)
    APQ5 = models.CharField(max_length=10)
    APQ = models.CharField(max_length=10)
    DDA = models.CharField(max_length=10)
    NHR = models.CharField(max_length=10)
    HNR = models.CharField(max_length=10)
    RPDE = models.CharField(max_length=10)
    DFA = models.CharField(max_length=10)
    spread1 = models.CharField(max_length=10)
    spread2 = models.CharField(max_length=10)
    D2 = models.CharField(max_length=10)
    PPE = models.CharField(max_length=10)

class SaveStrokeEnquiry(models.Model):
    age = models.CharField(max_length=10)
    hypertension = models.CharField(max_length=10)
    heart_disease = models.CharField(max_length=10)
    avg_glucose_level = models.CharField(max_length=10)
    bmi = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    married = models.CharField(max_length=10)

    work_type = models.CharField(max_length=10)
    residence_type = models.CharField(max_length=10)
    smoking_status = models.CharField(max_length=10)

class SaveLungCancerEnquiry(models.Model):
    age = models.CharField(max_length=10)
    smoking = models.CharField(max_length=10)
    yellow_fingers = models.CharField(max_length=10)
    anxiety = models.CharField(max_length=10)
    peer_pressure = models.CharField(max_length=10)
    chronic_disease = models.CharField(max_length=10)
    fatigue= models.CharField(max_length=10)
    allergy = models.CharField(max_length=10)
    wheezing = models.CharField(max_length=10)
    alcohol_consuming = models.CharField(max_length=10)
    coughing = models.CharField(max_length=10)
    sob = models.CharField(max_length=10)
    swalling_difficulty = models.CharField(max_length=10)
    chest_pain = models.CharField(max_length=10)







