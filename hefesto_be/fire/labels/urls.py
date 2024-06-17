from django.urls import path

# Views
from hefesto_be.fire.labels.views import label_list, label_detail

urlpatterns = [
    path('labels/', label_list, name='labels'),
    path('labels/<int:pk>', label_detail, name='labels'),
]
