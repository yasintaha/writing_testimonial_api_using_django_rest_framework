from django.db import models

# Create your models here.
class TestimonialModel(models.Model):
    testimonial = models.CharField(max_length=243)
    date = models.DateTimeField(auto_now_add=True)
    