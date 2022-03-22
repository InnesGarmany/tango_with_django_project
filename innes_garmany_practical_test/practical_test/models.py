from operator import truediv
from django.db import models

class GACourse(models.Model):
    courseTitle = models.CharField(max_length=75, unique = True)
    startDate = models.DateField()
    courseDescription = models.CharField(max_length=1000)

    def __str__(self):
        return self.courseTitle