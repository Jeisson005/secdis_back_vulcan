from django.urls import path

# Views
from hefesto_be.fire.detections.views import DetectionViewSet

detection_list = DetectionViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
detection_detail = DetectionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update'
})
urlpatterns = [
    path('detections/', detection_list, name='detections'),
    path('detections/<int:pk>', detection_detail, name='detections'),
]
