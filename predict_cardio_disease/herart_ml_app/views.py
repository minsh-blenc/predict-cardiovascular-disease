from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from .Patient import Patient
from .ml_model_utils.cardio_disease_predict import HeartDiseaseModel

# Create your views here.

def index(request):
    template = loader.get_template('herart_ml_app/index.html')
    return HttpResponse(template.render())

def prediction(request):
    template = loader.get_template('herart_ml_app/prediction.html')
    return HttpResponse(template.render())

@csrf_exempt
def result(request):
    if request.method == 'POST':
        new_patient = Patient()
        new_patient.name = request.POST.get('name')
        new_patient.age = request.POST.get('age')
        new_patient.sex = request.POST.get('sex')
        new_patient.cest_pain_type = request.POST.get('cp')
        new_patient.resting_blood_pressure = request.POST.get('trestbps')
        new_patient.cholestrol = request.POST.get('chol')
        new_patient.fasting_blood_sugar = request.POST.get('fbs')
        new_patient.rest_ecg = request.POST.get('restecg')
        new_patient.max_heart_rate = request.POST.get('thalach')
        new_patient.exercise_induced_angina = request.POST.get('exang')
        new_patient.oldpeak = request.POST.get('oldpeak')
        new_patient.slope = request.POST.get('slope')
        new_patient.vessels_colored_by_fluroscopy = request.POST.get('ca')
        new_patient.thallium_stress_test = request.POST.get('thal')
        #new_patient.prediction_result = request.POST.get('age')

    heart_disease_model = HeartDiseaseModel(new_patient)
    prediction_report = heart_disease_model.load_and_predict()
    print(new_patient)
    print(prediction_report)
    template = loader.get_template('herart_ml_app/result.html')
    return HttpResponse(template.render())



