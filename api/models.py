from django.db import models

# Create your models here.
class Note(models.Model):
    body=models.TextField(blank=False,null=False)
    date_updated=models.DateTimeField(auto_now=True)
    date_created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.body[0:10]