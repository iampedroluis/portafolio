from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    
    
