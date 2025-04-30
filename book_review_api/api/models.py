from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField(default='2023-01-01')  # تحديد تاريخ افتراضي

    def __str__(self):
        return self.title
