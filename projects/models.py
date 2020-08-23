from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()

    def __str__(self):
        return str(self.title)
    
    
class Waiter(models.Model):
