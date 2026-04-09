class Patient:
    def __init__(self, name="Unknown", age=0, sex=0, cest_pain_type=0, 
                 resting_blood_pressure=0, cholestrol=0, fasting_blood_sugar=False, 
                 rest_ecg=0, max_heart_rate=0, exercise_induced_angina=False, 
                 oldpeak=0.0, slope=0, vessels_colored_by_fluroscopy=0, 
                 thallium_stress_test=0, prediction_result=False):
        # Initializing attributes using setters to ensure validation logic is applied
        self.name = name
        self.age = age
        self.sex = sex
        self.cest_pain_type = cest_pain_type
        self.resting_blood_pressure = resting_blood_pressure
        self.cholestrol = cholestrol
        self.fasting_blood_sugar = fasting_blood_sugar
        self.rest_ecg = rest_ecg
        self.max_heart_rate = max_heart_rate
        self.exercise_induced_angina = exercise_induced_angina
        self.oldpeak = oldpeak
        self.slope = slope
        self.vessels_colored_by_fluroscopy = vessels_colored_by_fluroscopy
        self.thallium_stress_test = thallium_stress_test
        self.prediction_result = prediction_result

    # --- Getters and Setters ---

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if 0 <= int(value) <= 120:
            self._age = int(value)
        else:
            raise ValueError("Age must be between 0 and 120")

    @property
    def sex(self):
        sex_value = "Male" if self._sex else "Female"
        return sex_value
    
    @property
    def raw_prop_sex(self):
        return int(self._sex)

    @sex.setter
    def sex(self, value):
        self._sex = bool(int(value))

    @property
    def cest_pain_type(self):
        pain_type = ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic']
        return pain_type[self._cest_pain_type]
    
    @property
    def raw_prop_cest_pain_type(self):
        return self._cest_pain_type

    @cest_pain_type.setter
    def cest_pain_type(self, value):
        if 0 <= int(value) <= 3:
            self._cest_pain_type = int(value)
        else:
            raise ValueError("Chest pain type must be between 0 and 3")

    @property
    def resting_blood_pressure(self):
        return self._resting_blood_pressure

    @resting_blood_pressure.setter
    def resting_blood_pressure(self, value):
        if int(value) >= 0:
            self._resting_blood_pressure = int(value)
        else:
            raise ValueError("Resting blood pressure cannot be negative")

    @property
    def cholestrol(self):
        return self._cholestrol

    @cholestrol.setter
    def cholestrol(self, value):
        if int(value) >= 0:
            self._cholestrol = int(value)
        else:
            raise ValueError("Cholestrol cannot be negative")

    @property
    def fasting_blood_sugar(self):
        is_blood_sugar = "Positive" if self._fasting_blood_sugar else "Negative"
        return is_blood_sugar
    
    @property
    def raw_prop_fasting_blood_sugar(self):
        return int(self._fasting_blood_sugar)

    @fasting_blood_sugar.setter
    def fasting_blood_sugar(self, value):
        self._fasting_blood_sugar = bool(int(value))

    @property
    def rest_ecg(self):
        ecg = ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy']
        return ecg[self._rest_ecg]

    @property
    def raw_prop_rest_ecg(self):
        return self._rest_ecg
    
    @rest_ecg.setter
    def rest_ecg(self, value):
        if 0 <= int(value) <= 2:
            self._rest_ecg = int(value)
        else:
            raise ValueError("Rest ECG must be between 0 and 2")

    @property
    def max_heart_rate(self):
        return self._max_heart_rate

    @max_heart_rate.setter
    def max_heart_rate(self, value):
        if int(value) >= 0:
            self._max_heart_rate = int(value)
        else:
            raise ValueError("Max heart rate cannot be negative")

    @property
    def exercise_induced_angina(self):
        induce_angina = "Yes" if self._exercise_induced_angina else "No"
        return induce_angina
    
    @property
    def raw_prop_exercise_induced_angina(self):
        return int(self._exercise_induced_angina)

    @exercise_induced_angina.setter
    def exercise_induced_angina(self, value):
        self._exercise_induced_angina = bool(int(value))

    @property
    def oldpeak(self):
        return self._oldpeak

    @oldpeak.setter
    def oldpeak(self, value):
        self._oldpeak = float(value)

    @property
    def slope(self):
        slope_status = ['Upsloping', 'Flat', 'Downsloping']
        return slope_status[self._slope]
    
    @property
    def raw_prop_slope(self):
        return self._slope

    @slope.setter
    def slope(self, value):
        if 0 <= int(value) <= 2:
            self._slope = int(value)
        else:
            raise ValueError("Slope must be between 0 and 2")

    @property
    def vessels_colored_by_fluroscopy(self):
        return self._vessels_colored_by_fluroscopy

    @vessels_colored_by_fluroscopy.setter
    def vessels_colored_by_fluroscopy(self, value):
        if 0 <= int(value) <= 4:
            self._vessels_colored_by_fluroscopy = int(value)
        else:
            raise ValueError("Vessels colored must be between 0 and 4")

    @property
    def thallium_stress_test(self):
        thallium_test = ['Unknown/Other', 'Normal', 'Fixed Defect', 'Reversable Defect']
        return thallium_test[self._thallium_stress_test]
    
    @property
    def raw_prop_thallium_stress_test(self):
        return self._thallium_stress_test

    @thallium_stress_test.setter
    def thallium_stress_test(self, value):
        if 0 <= int(value) <= 3:
            self._thallium_stress_test = int(value)
        else:
            raise ValueError("Thallium stress test must be between 0 and 3")

    @property
    def prediction_result(self):
        result = "Positive" if self._prediction_result else "Negative"
        return result

    @prediction_result.setter
    def prediction_result(self, value):
        self._prediction_result = bool(int(value))

    # --- String Representation ---

    def __str__(self):
        return (f"Patient Record: {self.name}\n"
                f"--------------------------\n"
                f"Age: {self.age}\n"
                f"Sex: {'Male' if self.sex else 'Female'}\n"
                f"Chest Pain Type: {self.cest_pain_type}\n"
                f"Resting BP: {self.resting_blood_pressure}\n"
                f"Cholestrol: {self.cholestrol}\n"
                f"Max Heart Rate: {self.max_heart_rate}\n"
                f"Prediction Result: {'Heart Disease' if self.prediction_result else 'Healthy'}")