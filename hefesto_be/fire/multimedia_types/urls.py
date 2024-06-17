from django.urls import path

# Views
from hefesto_be.fire.multimedia_types.views import multimedia_type

urlpatterns = [
    path('multimedia_types/', multimedia_type, name='multimedia_types'),
]
