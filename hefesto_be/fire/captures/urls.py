""" Capture URLs module."""
from django.urls import path

# Views
from hefesto_be.fire.captures.views import (
    capture_detail, capture_list, camera_calibrate)

urlpatterns = [
    path('captures/', capture_list, name='captures'),
    path('captures/<int:pk>', capture_detail, name='captures'),
    path('camera_calibration/<int:capture_id>', camera_calibrate, name='camera_calibration'),
]
