from rest_framework import viewsets,filters,generics
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    @action(detail=True, methods=['PATCH'], url_path='update-profile')
    def update_profile(self, request, pk=None):
        doctor = self.get_object()
        serializer = self.get_serializer(doctor, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, methods=['GET'], url_path='all-profiles')
    def all_profiles(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

class PatientListView(generics.ListAPIView):
    serializer_class = PatientSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['reservation__reservation_date', 'reservation__status']
    ordering_fields = ['reservation__reservation_date', 'reservation__status']

    def get_queryset(self):
        queryset = Patient.objects.all()
        return queryset

class ReservationListView(generics.ListAPIView):
    serializer_class = ReservationSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['reservation_date', 'status', 'patient']
    ordering_fields = ['reservation_date', 'status', 'patient']

    def get_queryset(self):
        queryset = Reservation.objects.all()
        return queryset