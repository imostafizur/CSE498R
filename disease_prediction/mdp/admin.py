from django.contrib import admin
from mdp.models import SaveDiabetesEnquiry,SaveHeartEnquiry,SavePerkinsonEnquiry,SaveStrokeEnquiry,SaveLungCancerEnquiry

class ServiceAdmin1(admin.ModelAdmin):
    list_display = ('pregnancies', 'glucose', 'bp', 'st', 'insulin', 'bmi', 'dpf', 'age') #Diabates

class ServiceAdmin2(admin.ModelAdmin):
    list_display = ('age', 'gender', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach','exang','oldpeak','slope','ca','thal') #Heart

class ServiceAdmin3(admin.ModelAdmin):
    list_display = ('Fo', 'Fhi', 'Flo', 'Jitter_p', 'Jitter_a', 'RAP','PPQ','DDP','Shimmer','Shimmer_db','APQ3','APQ5','APQ','DDA','NHR','HNR',
                    'RPDE','DFA','spread1','spread2','D2','PPE') #Parkinson
 
class ServiceAdmin4(admin.ModelAdmin):
    list_display = ('age', 'hypertension', 'heart_disease', 'avg_glucose_level', 'bmi', 'gender', 'married', 'work_type', 'residence_type',
                         'smoking_status') #BrainStroke
class ServiceAdmin5(admin.ModelAdmin):
    list_display = ('age', 'smoking', 'yellow_fingers', 'anxiety', 'peer_pressure', 'chronic_disease', 'fatigue', 'allergy', 'wheezing',
                    'alcohol_consuming', 'coughing', 'sob' , 'swalling_difficulty', 'chest_pain') #LungCancer
 

# Register your models here.
admin.site.register(SaveDiabetesEnquiry,ServiceAdmin1)
admin.site.register(SaveHeartEnquiry,ServiceAdmin2)
admin.site.register(SavePerkinsonEnquiry,ServiceAdmin3)
admin.site.register(SaveStrokeEnquiry, ServiceAdmin4)
admin.site.register(SaveLungCancerEnquiry, ServiceAdmin5)