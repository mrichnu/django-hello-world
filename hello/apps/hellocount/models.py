from django.db import models

class Visit(models.Model):
    visit_stamp = models.DateTimeField(auto_now_add=True)
    user_agent = models.CharField(max_length=255)

