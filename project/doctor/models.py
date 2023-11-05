from django.db import models

class Hospital(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100) 
    location = models.CharField(max_length=100) 

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    large_name = models.CharField(max_length=50)  
    detail_name = models.CharField(max_length=50)

class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=[('M', '남성'), ('F', '여성')])
    location = models.CharField(max_length=100)  
    number = models.CharField(max_length=20)  
    photo = models.ImageField(upload_to='doctors/', default='project/image/DefaultDoctor.png') 
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE) 
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE) 

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    birth = models.DateField()
    gender = models.CharField(max_length=1, choices=[('M', '남성'), ('F', '여성')])
    number = models.CharField(max_length=20)  
    height = models.IntegerField()
    weight = models.IntegerField()
    underlying_disease = models.CharField(max_length=100,null=True)  
    location = models.CharField(max_length=100)  

class Reservation(models.Model):
    status = models.CharField(max_length=1, choices=[('w','대기'),('a','확정'),('d','취소'),('c','완료')])  
    visit_for = models.CharField(max_length=100)  
    reservation_date = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE) 
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)