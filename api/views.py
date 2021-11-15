from django.shortcuts import render

# Create your views here.
import numpy as np
import pandas as pd
from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response


class insurancePrediction(APIView):
    def post(self, request):
        data = request.data
        age = data['age']
        sex = data['sex']
        bmi = data['bmi']
        children = data['children']
        smoker = data['smoker']
        if sex == 'male':
            sex = 0
        elif sex == 'female':
            sex = 1
        else:
            return Response("Sex field is invalid", status=400)

        if smoker == 'yes':
            smoker = 1
        elif smoker == 'no':
            smoker = 0
        else:
            return Response("Smoker field is invalid", status=400)    
        lin_reg_model = ApiConfig.model
        insurance_predicted = lin_reg_model.predict([[age,sex,bmi,children,smoker]])[0]
        insurance_predicted = np.round(insurance_predicted, 1)
        #resp=""
        #if insurance_predicted==1:
        #    resp="yes"
        #else:  
        #    resp="no"  
        response_dict = {"Predicted charges (kg)": insurance_predicted}
        return Response(response_dict, status=200)