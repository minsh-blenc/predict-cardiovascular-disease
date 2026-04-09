from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from .Patient import Patient
from .ml_model_utils.cardio_disease_predict import HeartDiseaseModel

import json
from datetime import datetime
import pandas as pd

# views utils functions
def model_spec_json_obj():
    with open('herart_ml_app\ml_model_utils\prediction_model\model_specs.json', 'r') as file:
        json_data = json.load(file)
    print(json_data)
    json_data['model_training_date']
    model_specs = {
        'model_training_date' : datetime.strptime(
            json_data['model_training_date'], 
            "%Y-%m-%d %H:%M:%S.%f"
        ),
        'model_accuracy': float(json_data['model_accuracy'])*100,
        'model_classification_report': pd.DataFrame(
            json_data['model_classification_report']
        ).transpose(),
        'model_confusion_matrix': pd.DataFrame(json_data['model_confusion_matrix'])
    }

    return model_specs

# Create your views here.

def index(request):
    model_specs_context = model_spec_json_obj()
    template = loader.get_template('herart_ml_app/index.html')
    return HttpResponse(template.render(context=model_specs_context))

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
    context = {
        'patient_details':{
            'name':new_patient.name,
            'age': new_patient.age,
            'gender': new_patient.sex,
            'chest_pain_type': new_patient.cest_pain_type,
            'rest_bp': new_patient.resting_blood_pressure,
            'chol': new_patient.cholestrol,
            'max_heart_rate': new_patient.max_heart_rate
        },
        'prediction_status': prediction_report['status'],
        'prediction_score': prediction_report['score']
    }
    template = loader.get_template('herart_ml_app/result.html')
    return HttpResponse(template.render(context=context))



