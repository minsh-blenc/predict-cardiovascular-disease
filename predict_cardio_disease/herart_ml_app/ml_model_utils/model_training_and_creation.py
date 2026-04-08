import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

from datetime import datetime
import json

class HeartDiseaseModelTrain:
    def __init__(self):
        self.data_path = "./dataset/heart.csv"
        self.model = RandomForestClassifier(n_estimators=400, random_state=42)
        self.scaler = StandardScaler()
        self.data_set_df = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def load_and_preprocess(self):
        """Load data and split into features (X) and target (y)."""
        self.data_set_df = pd.read_csv(self.data_path)
        
        # Define features and target 
        X = self.data_set_df.drop('target', axis=1) 
        y = self.data_set_df['target']
        
        # Split into training and testing sets (80/20)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42)
        
        # Scale features for better performance
        self.X_train = self.scaler.fit_transform(self.X_train)
        self.X_test = self.scaler.transform(self.X_test)
        

    def train(self):
        """Train the Random Forest model."""
        self.model.fit(self.X_train, self.y_train)
        print("Model training complete.")

    def evaluate(self):
        """Predict and evaluate model performance."""
        y_pred = self.model.predict(self.X_test)
        
        print(f"Accuracy Score: {accuracy_score(self.y_test, y_pred):.2f}")
        print("\nClassification Report:\n", classification_report(self.y_test, y_pred))
        print("\nConfusion Matrix:\n", confusion_matrix(self.y_test, y_pred))
        confus_matrix = pd.DataFrame(confusion_matrix(self.y_test, y_pred))
        confus_matrix = confus_matrix.to_dict(orient='records')

        model_specs = {
            'Model Training Date': str(datetime.now()),
            'Model Accuracy': f"Accuracy Score: {accuracy_score(self.y_test, y_pred):.2f}",
            'Model Classification Report': classification_report(
                self.y_test, y_pred, output_dict=True),
            'Model Confusion Matrix' : confus_matrix
        }

        with open("./prediction_model/model_specs.json", "w") as file:
            json.dump(model_specs, file)

    def create_model(self):
        with open('./prediction_model/heart_disease_prediction_model.pkl', 'wb') as f:
            pickle.dump(self.model, f)

    def execute_model_training(self):
        print("---Executing Model Training---")
        self.load_and_preprocess()
        self.train()
        self.evaluate()
        self.create_model()
        print("--- Model Training has been Completed ---")


        
