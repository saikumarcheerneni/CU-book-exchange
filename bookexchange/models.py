from django.db import models

class Textbook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    edition = models.CharField(max_length=50, null=True, blank=True)  
    condition_choices = [
        ('new', 'New'),
        ('used', 'Used'),
        ('worn', 'Worn'),
    ]
    condition = models.CharField(max_length=10, choices=condition_choices)
    course_code = models.CharField(max_length=10)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} by {self.author} ({self.condition})"

