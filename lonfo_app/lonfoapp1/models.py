from django.db import models


class Lonfoapp1(models.Model):
    
    content = models.CharField(max_length=140)
    posted_date = models.DateTimeField(auto_now_add=True)
