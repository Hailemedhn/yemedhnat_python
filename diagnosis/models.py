from django.db import models

# Create your models here.


    
class BodyParts(models.Model):
    
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Symptom(models.Model):
    name = models.CharField(max_length=50)
    part = models.ForeignKey(BodyParts,on_delete=models.CASCADE,related_name="part_in_pain")
    def __str__(self):
        return self.name

class Disease(models.Model):
    name = models.CharField(max_length=50)
    symptom = models.ManyToManyField(Symptom,related_name="symptom_name")

    def __str__(self):
        return self.name