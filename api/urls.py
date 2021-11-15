from django.urls import path
from .views import insurancePrediction

urlpatterns = [
    path('insurance/', insurancePrediction.as_view(), name = 'insurance_prediction'),
]