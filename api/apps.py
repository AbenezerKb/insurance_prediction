from django.apps import AppConfig
import joblib
import os
from django.apps import AppConfig
from django.conf import settings

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    MODEL_FILE = os.path.join(settings.MODELS, "finalized_model.sav")
    model = joblib.load(MODEL_FILE)