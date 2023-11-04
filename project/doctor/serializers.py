from rest_framework import serializers
from models import *

class HospitalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hospital
        fields = '__all__'
        read_only_fields =['id']

class SubjectSerializer(serializers.ModelSerializer):

    class meta:
        model = Subject
        fields ='__all__'

class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields =['id','hospital','subject']

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'
        

class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = '__all__'
        read_only_fields =['id','doctor','patient']