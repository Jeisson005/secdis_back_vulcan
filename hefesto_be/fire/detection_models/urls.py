from django.urls import path

# Views
from .views import detection_model_list, detection_model_detail

urlpatterns = [
    path('detection_models/', detection_model_list, name='detection_models'),
    path('detection_models/<int:pk>', detection_model_detail, name='detection_models'),
]
