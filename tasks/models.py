from django.db import models

class Status(models.Model):
    id = models.AutoField(primary_key=True)
    type_status = models.CharField(max_length=200,unique=True)
    
    def __str__(self):
        return self.type_status

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(unique=True,max_length=200)
    description = models.CharField(max_length=500)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="status", default=1)
    is_finished = models.BooleanField(default=False)
    
    
    

