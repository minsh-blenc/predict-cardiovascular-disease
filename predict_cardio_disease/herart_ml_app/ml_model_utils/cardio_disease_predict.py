import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
from ..Patient import Patient

class HeartDiseaseModel:
    patient_data = Patient()
    def __init__(self, patient_data):
        self.model_path = './prediction_model/heart_disease_prediction_model.pkl'
        self.scaler = None
        self.features = [
            patient_data.age,patient_data.raw_prop_sex,patient_data.raw_prop_cest_pain_type,
            patient_data.resting_blood_pressure,patient_data.cholestrol,
            patient_data.raw_prop_fasting_blood_sugar,patient_data.raw_prop_rest_ecg,
            patient_data.max_heart_rate,patient_data.raw_prop_exercise_induced_angina,
            patient_data.oldpeak,patient_data.raw_prop_slope,
            patient_data.vessels_colored_by_fluroscopy,patient_data.raw_prop_thallium_stress_test
        ]
    
    def get_features_array(self):
        return np.array(self.features).reshape(1, -1)
    

    def load_and_predict(self):
        try:
            print(self.model_path)
            # 2. Load the pickle file
            with open('herart_ml_app\ml_model_utils\prediction_model\heart_disease_prediction_model.pkl', 'rb') as file:
                model = pickle.load(file)
            
            with open('herart_ml_app\ml_model_utils\prediction_model\heart_disease_prediction_scaler.pkl', 'rb') as file:
                self.scaler = pickle.load(file)
        
            # 3. Get input from the patient class and predict
            input_data = self.scaler.transform(self.get_features_array())
            print(self.get_features_array())
            print(input_data)
            prediction = model.predict(input_data)[0]
            print("Prediction:", model.predict(input_data))
            probabilities = model.predict_proba(input_data)[0]
            print("Probability:", model.predict_proba(input_data))
            confidence = probabilities[prediction] * 100

            
            status = "Heart Disease Detected" if prediction == 1 else "Healthy"
            prediction_report = {
                'status': status,
                'score': confidence
            }
            return prediction_report
        
        # except FileNotFoundError:
        #     return "Error: model.pkl file not found."
        except Exception as e:
            return f"An error occurred: {e}"

