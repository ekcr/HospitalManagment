from django.db import models

# Create your models here.

class Doctors(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    name = models.CharField(db_column='Name', max_length=35)  
    department = models.CharField(db_column='Departmant', max_length=50)  

    def __str__(self) -> str:
        return self.name
    
class Patient(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    name = models.CharField(db_column='Name', max_length=35)  
    gender = models.CharField(db_column='Gender', max_length=35, default=None)  
    age = models.IntegerField(db_column='Age', blank=True)

    def __str__(self) -> str:
        return self.name
    
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE, db_column='Doctor')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='Patient')
    date_time = models.DateTimeField()

    def __str__(self) -> str:
        return self.doctor.name+"--"+self.patient.name
