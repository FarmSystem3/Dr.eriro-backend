from django.urls import path,include
from .views import *
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'doctor'

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)

urlpatterns = [

    path('api/', include(router.urls)),
    path('patients/', views.PatientListView.as_view(), name='patient-list'),
    path('reservations/', views.ReservationListView.as_view(), name='reservation-list'),
]